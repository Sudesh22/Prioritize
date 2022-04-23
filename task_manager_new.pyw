import sys, sqlite3, datetime, os, time, getpass
from os.path import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

USER_NAME = getpass.getuser()
if getattr(sys, 'frozen', False):
        curr_path = os.path.dirname(sys.executable)
elif __file__:
        curr_path = os.path.dirname(__file__)
print(curr_path)

class First(QMainWindow):
    def __init__(self, id):
        super(First, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\_notification.ui'), self)
        self.setWindowTitle("notification")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        s_w = 470
        s_h = 170
        
        def Snooze():
            from datetime import timedelta
            print("Snooze button pressed")
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            due = c.execute("SELECT due FROM tasks WHERE rowid = (?)", (id,)).fetchone()
            date = datetime.datetime.strptime(due[0], '%Y-%m-%d %H:%M:%S')
            date = date + timedelta(minutes=2)
            date = date.strftime("%Y-%m-%d %H:%M:%S")
            print(date)
            c.execute("UPDATE tasks SET due = :due WHERE oid = :oid", {'due': date,'oid': id})
            conn.commit()
            conn.close()
            for i in range(0,s_w, 2):
                QApplication.processEvents()
                time.sleep(0.01)
                self.setGeometry(new + i, height - s_h, s_w, s_h)
            Startup()

        def func2():
            print("Completed button pressed")
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            due = c.execute("SELECT due FROM tasks WHERE rowid = (?)", (id,)).fetchone()
            c.execute("UPDATE tasks SET pending = :pending WHERE oid = :oid", {'pending': 0,'oid': id})
            conn.commit()
            conn.close()
            for i in range(0,s_w, 2):
                QApplication.processEvents()
                time.sleep(0.01)
                self.setGeometry(new + i, height - s_h, s_w, s_h)
            Startup()

        def get_title(id):
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            title = c.execute("SELECT task_name FROM tasks WHERE rowid = (?)", (id,)).fetchone()
            return title[0]

        def disappear():
            for i in range(0,s_w, 2):
                QApplication.processEvents()
                time.sleep(0.01)
                self.setGeometry(new + i, height - s_h, s_w, s_h)
            Startup()

        def appear(self):
            for i in range(0,s_w, 2):
                QApplication.processEvents()
                time.sleep(0.01)
                global new
                new = width - i
                self.setGeometry(new, height - s_h, s_w, s_h)

            for i in range(500):
                QApplication.processEvents()
                time.sleep(0.01)

            for i in range(0,s_w, 2):
                QApplication.processEvents()
                time.sleep(0.01)
                self.setGeometry(new + i, height - s_h, s_w, s_h)

        title = str(get_title(id))
        self.tname.setText(title)
        self.completed.setStyleSheet("QPushButton{font: 9pt 'SansSerif';color: black;text-align: center;background-color:rgb(255, 255, 255); border-radius: 15px;}QPushButton:hover{border : 2px solid black;}")
        self.snoozed.setStyleSheet("QPushButton{font: 9pt 'SansSerif';color: black;text-align: center;background-color:rgb(255, 255, 255); border-radius: 15px;}QPushButton:hover{border : 2px solid black;}")
        self.close.clicked.connect(disappear)
        self.completed.clicked.connect(func2)
        self.snoozed.clicked.connect(Snooze)
        self.appName.setText("Prioritize")
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        height = self.screenRect.height()
        width = self.screenRect.width()
        # print(height, width)
        self.setGeometry(width + s_w, height - s_h, s_w, s_h)
        self.show()
        appear(self)

def main(id):  
    
    app = QApplication(sys.argv)
    main = First(id)
    main.show()

def has_executed(executed, due):
    n=0
    j=0
    print(due)
    with open("test.log") as fp:
            for line in fp:
                if j<len(due):
                    print("has_exec line:",line)
                    print("has_exec",due[j][1],line[11:30])
                    if line.startswith(due[j][1], 11, 30):
                        n+=1
                        j+=1
                        print("has_exec","n:",n,"j:",j)
            for i in range(n):
                executed[0][i] = 0
    print("n:",n,"exec"+str(executed))
    return executed


def has_passed(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return date < datetime.datetime.now()

def is_due(executed,i,old):
    import numpy as np
    while 1:
        conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
        c = conn.cursor()
        c.execute("SELECT * FROM tasks ORDER BY due DESC LIMIT 1")
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        due = c.execute("SELECT rowid,due FROM tasks WHERE due BETWEEN '" + today + " 00:00:00' AND '" + today + " 23:59:59' AND pending = 1").fetchall()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
        try:
            if due[i][1] == now:
                    print("Due!!!")
                    executed[0][i]=0
                    main(due[i][0])
                    time.sleep(0.5)
                    Startup()
            else:
                new = len(due)
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                due = c.execute("SELECT rowid,due FROM tasks WHERE due BETWEEN '" + today +" 00:00:00' AND '"+ today +" 23:59:59' AND pending = 1").fetchall()
                print(now + " : " + due[new-1][1] + " " + str(new))
                if new>old:
                    for j in range(new-old):
                        executed = np.append(executed, 1)
                        break
                    Startup()
                if new<old:
                    print("u got me")
                time.sleep(0.5)
        except:
            Startup()
        time.sleep(0.5)
    
def Startup():
    i=0
    import numpy as np
    conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
    c = conn.cursor()
    
    c.execute("SELECT * FROM tasks ORDER BY due DESC LIMIT 1")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    due = c.execute("SELECT rowid,due FROM tasks WHERE due BETWEEN '" + today +" 00:00:00' AND '" + today + " 23:59:59' AND pending = 1" ).fetchall()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
    executed = np.ones((1,len(due)))
    executed = has_executed(executed, due)
    print(due)
    old = len(due)
    if i==0 and old==0:
        while 1:
            due = c.execute("SELECT rowid,due FROM tasks WHERE due BETWEEN '" + today + " 00:00:00' AND '" + today + " 23:59:59' AND pending = 1").fetchall()
            print("assds", due)
            time.sleep(0.5)
            if len(due)!=0:
                Startup()
    else:
        for i in range(len(due)):
            if i<=old:
                if has_passed(due[i][1]) and executed[0][i]!=0:
                    print(due[i][1], "is passed")
                    executed[0][i]=0
                    print(executed)
                    main(due[i][0])
                elif has_passed(due[i][1]) and executed[0][i]==0:
                    pass
                else:
                    is_due(executed,i,old)
        while 1:
            new = len(due)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            due = c.execute("SELECT rowid,due FROM tasks WHERE due BETWEEN '" + today +" 00:00:00' AND '"+ today +" 23:59:59' AND pending = 1").fetchall()
            print(now + " : " + due[new-1][1] + " " + str(new))
            if new>old:
                for j in range(new-old):
                    executed = np.append(executed, 1)
                    break
                Startup()
            time.sleep(0.5)

if __name__ == '__main__':
    Startup()