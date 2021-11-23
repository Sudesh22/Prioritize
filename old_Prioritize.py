import sys, sqlite3, datetime, os, time, getpass
from os.path import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtSvg, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QStackedWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QScrollArea, QGridLayout, QGroupBox, QRadioButton, QFrame, QCalendarWidget, QMessageBox, QProgressBar
from PyQt5.QtCore import *
from PyQt5.QtGui import QCursor, QIcon, QPixmap

USER_NAME = getpass.getuser()
curr_path = os.path.dirname(os.path.realpath(__file__))
print(curr_path)
class get_started_(QMainWindow):
    def __init__(self):
        super(get_started_, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\start1.ui'), self)
        self.setWindowTitle("Welcome")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label.setText('<img src="Images\page1.svg" width=401 height=301></img>')

        def show_():
            self.get_started_ = login()
            self.get_started_.show()
            self.close()
        
        self.get_started.clicked.connect(show_)
        self.get_started.setStyleSheet("""QPushButton{ font: 13pt "SansSerif";color: black;text-align: center;background-color:rgb(255, 0, 255);border-radius: 25px;}QPushButton:hover{ border : 2px solid black;} QPushButton:focus{outline: 0;}""")
        self.close_.clicked.connect(sys.exit)
        self.close_.setStyleSheet("""QPushButton{ font: 15pt "SansSerif";text-align: center; background-color: rgba(0, 0, 0, 0);border-radius:20px;}QPushButton:focus{ outline: 0;}""")

class error(QMainWindow):
    def __init__(self):
        super(error, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\_error.ui'), self)
        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal)  
        self.label.setText("Oops you didn't tell us your name")
        self.back.setText("Back")
        self.back.setStyleSheet("""QPushButton{font: 11pt 'SansSerif';color: black;text-align: center;background-color:rgb(255, 255, 255); border-radius: 20px;}QPushButton:hover{border : 2px solid black;}""")
        self.back.clicked.connect(self.close)


class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\_login.ui'), self)
        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        def show_(self):
            if self.name.text() != '':
                conn = sqlite3.connect('Prioritize\Databases\Prioritize.db')
                c = conn.cursor()
                table = c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='personal_info'""").fetchall()

                if table==[]:
                    c.execute("""CREATE TABLE IF NOT EXISTS personal_info(
                                name text,
                                gender int)
                            """)
                    conn.commit()

                    c.execute("INSERT INTO personal_info VALUES (?,?)", (self.name.text(), gen))
                    conn.commit()
                    conn.close()
                else:
                    self.login = Window()
                    self.login.show()
                    self.close()
            else:
                self.login = error()
                self.login.show()
                # self.close()

        self.label.setText('<img src="Images\_m_login.svg" width=651 height=473></img>')
        self.male.clicked.connect(lambda: self.check(self.male))
        self.female.clicked.connect(lambda: self.check(self.female))
        self.dash.clicked.connect(lambda: show_(self))
        self.dash.setStyleSheet("""QPushButton{font: 11pt 'SansSerif';color: black;text-align: center;background-color:rgb(255, 255, 255); border-radius: 20px;}QPushButton:hover{border : 2px solid black;} QPushButton:focus{outline: 0;}""")

    def check(self, b):
        if self.male.isChecked():
            self.label.setText('<img src="Images\_m_login.svg" width=651 height=473></img>')
            global gen
            gen = 1
            print(gen)
        else:
            self.label.setText('<img src="Images\_f_login.svg" width=651 height=473></img>')
            gen = 0
            print(gen)

class create_nt(QMainWindow):
    def __init__(self):
        super(create_nt, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\_new_task.ui'), self)
        self.setWindowTitle("Create new Task")
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal) 

        def abc(due) :
            date = datetime.datetime.strptime(due, '%d-%m-%Y %H:%M')
            print(date.strftime("%Y-%m-%d %H:%M"))

        def add_data(task, desc, due):
            date = datetime.datetime.strptime(due, '%d-%m-%Y %H:%M')
            # raw_date = due
            # dd = raw_date[:2]
            # mm = raw_date[3:5]
            # yyyy = raw_date[6:10]
            # hh = raw_date[11:13]
            # MM = raw_date[14:16]
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            # c.execute("INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)", (task, desc, yyyy, mm, dd, MM, hh, 1))
            c.execute("INSERT INTO tasks VALUES (?,?,?,?)", (task, desc, date, 1))
            print("Command executed sucessfully...")
            
            conn.commit()
            conn.close()
            self.task_name.setText("")
            self.task_desc.setText("")
            self.due_on.setDate(datetime.date.today())
            self.due_on.setTime(datetime.time())

            self.close()

        def close_win():
            self.task_name.setText("")
            self.task_desc.setText("")
            self.due_on.setDate(datetime.date.today())
            self.due_on.setTime(datetime.time())
            self.close()
        
        self.save.setStyleSheet("QPushButton{font: 9pt 'SansSerif';color: black;text-align: center;background-color:rgba(0, 0, 0, 0.1); border-radius: 15px;}QPushButton:hover{border : 2px solid black;} QPushButton:focus{outline: 0;border: 2px solid black;}")
        self.discard.setStyleSheet("QPushButton{font: 9pt 'SansSerif';color: black;text-align: center;background-color:rgba(0, 0, 0, 0.1); border-radius: 15px;}QPushButton:hover {border : 2px solid black;} QPushButton:focus {outline: 0;border: 2px solid black;}")

        self.due_on.setMinimumDateTime(datetime.datetime.now())
        self.due_on.setDisplayFormat('dd-MM-yyyy hh:mm')
        # self.due_on.setDisplayFormat('yyyy-MM-dd hh:mm')
        self.save.clicked.connect(lambda: add_data(self.task_name.text(), self.task_desc.text(), self.due_on.text()))
        # self.save.clicked.connect(lambda: abc(self.due_on.text()))
        self.discard.clicked.connect(lambda: close_win())

    def enterEvent(self, event):
        print("Mouse Entered")
        return super(create_nt, self).enterEvent(event)

    def leaveEvent(self, event):
        print("Mouse Left")
        return super(create_nt, self).enterEvent(event)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor)) #Change the mouse icon
        
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

class show_task(QMainWindow):
    def __init__(self):
        super(show_task, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\_new_task.ui'), self)
        self.setWindowTitle("Create new Task")
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal) 
        file = open("demofile.txt", "a")
        file.write(os.path.join(curr_path,'.ui\_new_task.ui'))
        def abc(due) :
            date = datetime.datetime.strptime(due, '%d-%m-%Y %H:%M')
            print(date.strftime("%Y-%m-%d %H:%M"))

        def add_data(task, desc, due):
            date = datetime.datetime.strptime(due, '%d-%m-%Y %H:%M')
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            print(curr)
            # print("")
            c.execute("""UPDATE tasks SET
                        task_name = :task,
                        description = :desc,
                        due = :due
                        WHERE oid = :oid""",
                        {   'task': task,
                            'desc': desc,
                            'due': date,
                            'oid': curr
                        })
            print("""UPDATE tasks SET
                        task_name = :task,
                        description = :desc,
                        due = :due
                        WHERE oid = :oid""",
                        {   'task': task,
                            'desc': desc,
                            'due': date,
                            'oid': curr
                        })
            # c.execute("UPDATE tasks SET description = '{str(desc)}' WHERE rowid = (?)", int(curr))
            # c.execute("UPDATE tasks SET due = '{str(due)}' WHERE rowid = (?)", int(curr))
            # print("Command executed sucessfully...")
            
            conn.commit()
            conn.close()
            self.task_name.setText("")
            self.task_desc.setText("")
            # self.due_on.setDate(datetime.date.today())
            # self.due_on.setTime(datetime.time())

            self.close()

        def close_win():
            self.task_name.setText("")
            self.task_desc.setText("")
            # self.due_on.setDate(datetime.date.today())
            # self.due_on.setTime(datetime.time())
            self.close()
        
        self.save.setStyleSheet("QPushButton{font: 9pt 'SansSerif';color: black;text-align: center;background-color:rgba(0, 0, 0, 0.1); border-radius: 15px;}QPushButton:hover{border : 2px solid black;} QPushButton:focus{outline: 0;border: 2px solid black;}")
        self.discard.setStyleSheet("QPushButton{font: 9pt 'SansSerif';color: black;text-align: center;background-color:rgba(0, 0, 0, 0.1); border-radius: 15px;}QPushButton:hover {border : 2px solid black;} QPushButton:focus {outline: 0;border: 2px solid black;}")

        # self.due_on.setMinimumDateTime(datetime.datetime.now())
        self.due_on.setDisplayFormat('dd-MM-yyyy hh:mm')
        # self.due_on.setDisplayFormat('yyyy-MM-dd hh:mm')
        self.save.clicked.connect(lambda: add_data(self.task_name.text(), self.task_desc.text(), self.due_on.text()))
        # self.save.clicked.connect(lambda: abc(self.due_on.text()))
        self.discard.clicked.connect(lambda: close_win())

    def enterEvent(self, event):
        print("Mouse Entered")
        return super(show_task, self).enterEvent(event)

    def leaveEvent(self, event):
        print("Mouse Left")
        return super(show_task, self).enterEvent(event)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor)) #Change the mouse icon
        
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\_todo_dash_alt.ui'), self)
        self.setWindowTitle("Prioritize")
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        app.focusWindowChanged.connect(lambda: on_focusChanged())
        conn =  sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tasks(
        task_name text,
        description text,
        due text,
        pending int        
        )
        """)
        conn.commit()
        conn.close()
        conn =  sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE pending=1 ORDER BY due DESC")
        global t_name
        t_name = c.execute("SELECT task_name FROM tasks WHERE pending=1").fetchall()

        global rad_but
        rad_but = []
        for i in range(0,len(t_name)):
            r = '_r'
            t_name[i]
            rad_but.append(t_name[i][0] + r)

        global del_but
        del_but = []
        for i in range(0,len(t_name)):
            d = '_d'
            t_name[i]
            del_but.append(t_name[i][0] + d)

        global frames
        frames = []
        for i in range(0,len(t_name)):
            f = '_f'
            t_name[i]
            frames.append(t_name[i][0] + f)

        global h_lay
        h_lay = []
        for i in range(0,len(t_name)):
            h = '_h'
            t_name[i]
            h_lay.append(t_name[i][0] + h)
        conn.close()

        def new():
            self.window = create_nt()
            self.window.show()       

        def show_info(i):
            # print(i)
            win = show_task()
            win.show()

            for i in range(self.verticalLayout.count()):
                if info[i].isChecked():
                    conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                    c = conn.cursor()
                    c.execute("SELECT rowid,* FROM tasks ORDER BY due DESC")
                    items = c.fetchall()
                    for item in enumerate(items, start=1):
                        if item[0]==(i+1):
                            var = c.execute("SELECT rowid,* from tasks WHERE rowid = ?", (item[1][0],)).fetchall()
                            print(var)
                            conn.commit()
                            conn.close()
                            win.task_name.setText(var[0][1])
                            win.task_desc.setText(var[0][2])
                            # print(var[0][0])
                            global curr
                            curr = int(var[0][0])
                            print(curr)
                            a = datetime.datetime.strptime(var[0][3], "%Y-%m-%d %H:%M:%S")
                            win.due_on.setDateTime(datetime.datetime.strptime(a.strftime("%d-%m-%Y %H:%M"), "%d-%m-%Y %H:%M"))

        def on_focusChanged():
            if self.isActiveWindow():
                remove_()
                load()

        def search():
            self.search_b.setFocus()

        def update_(t_id):
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            val = c.execute("SELECT pending FROM tasks WHERE rowid = " + str(t_id)).fetchall()
            if val[0][0] == 1:
                print("1")
                c.execute("UPDATE tasks SET pending = 0 WHERE rowid = ?", (t_id,))
                conn.commit()
                conn.close()
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            val = c.execute("SELECT pending FROM tasks WHERE rowid = " + str(t_id)).fetchall()
            print(val[0][0])
            conn.commit()
            conn.close()

        def checked():
            for i in range(self.verticalLayout.count()):
                if rad_but[i].isChecked():
                    found = rad_but[i].text()
                    print(found)
                    update_(i+1)

        def delete(i):
            for i in range(self.verticalLayout.count()):
                if del_but[i].isChecked():
                    found = rad_but[i].text()
                    print(found)
                    del_but[i].setChecked(False)
                    print(i+1)
                    conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                    c = conn.cursor()
                    c.execute("SELECT rowid,* FROM tasks ORDER BY due DESC")
                    items = c.fetchall()
                    for item in enumerate(items, start=1):
                        if item[0]==(i+1):
                            print(item[1][0])
                            c.execute("DELETE from tasks WHERE rowid = ?", (item[1][0],))
                            conn.commit()
                            conn.close()
            remove_()
            load()

        def remove_():
            for i in reversed(range(self.verticalLayout.count())): 
                self.verticalLayout.itemAt(i).widget().deleteLater()

        def load():
            conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
            c = conn.cursor()
            tasks_e = c.execute("SELECT rowid, * FROM tasks WHERE pending = 1 ORDER BY due DESC").fetchall()
            t_name = c.execute("SELECT task_name FROM tasks WHERE pending = 1 ORDER BY due DESC").fetchall()
            
            c.execute("SELECT rowid, * FROM tasks WHERE pending=1 ORDER BY due DESC")

            global rad_but
            rad_but = []
            for i in range(0,len(t_name)):
                r = '_r'
                t_name[i]
                rad_but.append(t_name[i][0] + r)

            global del_but
            del_but = []
            for i in range(0,len(t_name)):
                d = '_d'
                t_name[i]
                del_but.append(t_name[i][0] + d)

            global info
            info = []
            for i in range(0,len(t_name)):
                d = '_d'
                t_name[i]
                info.append(t_name[i][0] + d)

            global frames
            frames = []
            for i in range(0,len(t_name)):
                f = '_f'
                t_name[i]
                frames.append(t_name[i][0] + f)

            global h_lay
            h_lay = []
            for i in range(0,len(t_name)):
                h = '_h'
                t_name[i]
                h_lay.append(t_name[i][0] + h)

            if tasks_e==[]:
                conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                c = conn.cursor()
                name = c.execute("SELECT name FROM personal_info").fetchall()
                self.hello_l.setText("Hello " + name[0][0] + "! You have no tasks scheduled for today!")
                conn.close()
                global cont
                cont = QFrame()
                global h_layout
                h_layout = QHBoxLayout()
                cont.setStyleSheet("""*{background-color: rgb(255,255,255);}""")
                cont.setFixedHeight(358)
                cont.setLayout(h_layout)
                label = QLabel("<center>Create new task</center>\n<center>New tasks are displayed here</center>")
                label.setStyleSheet("""font: 10pt "SansSerif";color: rgb(0, 0, 0);""")
                h_layout.addWidget(label)
                self.verticalLayout.setAlignment(Qt.AlignHCenter)
                self.verticalLayout.addWidget(cont)
            else:
                if (len(t_name)==1):
                    conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                    c = conn.cursor()
                    name = c.execute("SELECT name FROM personal_info").fetchall()
                    self.hello_l.setText("Hello " + name[0][0] + "! You have " + str(len(t_name)) + " task scheduled for today!")
                    conn.close()
                else:
                    conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                    c = conn.cursor()
                    name = c.execute("SELECT name FROM personal_info").fetchall()
                    self.hello_l.setText("Hello " + name[0][0] + "! You have " + str(len(t_name)) + " tasks scheduled for today!")
                    conn.close()
                
                if(self.search_b.text() == ""):
                    for i in range(len(t_name)):
                        name = t_name[i][0]
                        frames[i] = QFrame()
                        h_lay[i] = QHBoxLayout()

                        rad_but[i] = QRadioButton()
                        rad_but[i].setText(name)
                        rad_but[i].setAutoExclusive(False)
                        rad_but[i].toggled.connect(checked)

                        info[i] = QPushButton()
                        info[i].setIcon(QIcon(os.path.join(curr_path,'Images\_info.png')))
                        info[i].setIconSize(QSize(25, 25))
                        info[i].setFixedSize(40, 40)
                        info[i].setCheckable(True)
                        info[i].clicked.connect(show_info)
                        del_but[i] = QPushButton()
                        del_but[i].setIcon(QIcon(os.path.join(curr_path,'Images\_trash.png')))
                        del_but[i].setIconSize(QSize(25, 25))
                        del_but[i].setFixedSize(40, 40)
                        del_but[i].setCheckable(True)
                        del_but[i].clicked.connect(delete)

                        frames[i].setStyleSheet("""*{background-color: rgb(255, 221, 0);height: 20px;color: rgb(0, 0, 0);border-radius: 20px;font: 10pt "SansSerif";padding: 20px;} QRadioButton::indicator{width: 17px; height: 17px;} QFrame{padding: 1px;}""")
                        frames[i].setFixedHeight(90)

                        h_lay[i].addWidget(rad_but[i])
                        h_lay[i].addWidget(info[i])
                        h_lay[i].addWidget(del_but[i])
                        frames[i].setLayout(h_lay[i])

                        self.verticalLayout.setAlignment(Qt.AlignTop)
                        self.verticalLayout.addWidget(frames[i])       
                else:
                    key = self.search_b.text()
                    conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                    c = conn.cursor()
                    t_name = c.execute(f"SELECT task_name FROM tasks WHERE task_name LIKE '%{key}%' ORDER BY due DESC").fetchall()
                    conn.close()
                    remove_()

                    for i in range(len(t_name)):
                        name = t_name[i][0]
                        frames[i] = QFrame()
                        h_lay[i] = QHBoxLayout()

                        rad_but[i] = QRadioButton()
                        rad_but[i].setText(name)
                        rad_but[i].setAutoExclusive(False)
                        rad_but[i].toggled.connect(checked)

                        info[i] = QPushButton()
                        info[i].setIcon(QIcon(os.path.join(curr_path,'Images\_info.png')))
                        info[i].setIconSize(QSize(25, 25))
                        info[i].setFixedSize(40, 40)
                        info[i].setCheckable(True)
                        info[i].clicked.connect(show_info)
                        del_but[i] = QPushButton()
                        del_but[i].setIcon(QIcon(os.path.join(curr_path,'Images\_trash.png')))
                        del_but[i].setIconSize(QSize(25, 25))
                        del_but[i].setFixedSize(40, 40)
                        del_but[i].setCheckable(True)
                        del_but[i].clicked.connect(delete)

                        frames[i].setStyleSheet("""*{background-color: rgb(255, 221, 0);height: 20px;color: rgb(0, 0, 0);border-radius: 20px;font: 10pt "SansSerif";padding: 20px;} QRadioButton::indicator{width: 17px; height: 17px;} QFrame{padding: 1px;}""")
                        frames[i].setFixedHeight(90)

                        h_lay[i].addWidget(rad_but[i])
                        h_lay[i].addWidget(info[i])
                        h_lay[i].addWidget(del_but[i])
                        frames[i].setLayout(h_lay[i])

                        self.verticalLayout.setAlignment(Qt.AlignTop)
                        self.verticalLayout.addWidget(frames[i]) 
                
        self.search_b.setPlaceholderText("  Search Tasks")
        self.search_b.textChanged[str].connect(load)
        self.close.clicked.connect(sys.exit)
        self.new_task.setIcon(QIcon(os.path.join(curr_path,'Images\_new_task.png')))
        self.new_task.setIconSize(QSize(35, 35))
        self.search_bu.setIcon(QIcon(os.path.join(curr_path,'Images\search.png')))
        self.search_bu.setIconSize(QSize(35, 35))
        self.search_bu.clicked.connect(search)
        self.calendarWidget.setSelectionMode(QCalendarWidget.NoSelection)
        self.Logo.setText('<img src="Images\logo.svg" width=75 height=75></img>')
        
        def suffix(d):
            return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

        def custom_strftime(format, t):
            return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

        # date = '{S} %B, %Y', custom_strftime(datetime.datetime.now())

        self.today_date.setText("Today is,\n" + custom_strftime('{S} %B, %Y', datetime.datetime.now()))

        conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
        c = conn.cursor()
        img = c.execute("SELECT gender FROM personal_info").fetchall()
        name = c.execute("SELECT name FROM personal_info").fetchall()
        # self.hello_l.setText("Hello " + name[0][0] + "!")
        if img[0][0] == 1:
            self.profile.setIcon(QIcon(os.path.join(curr_path,'Images\_male.svg')))
            self.profile.setIconSize(QSize(50, 50))
            self.profile.setText(name[0][0])
            self.profile.setStyleSheet("""*{font: 9pt "SansSerif";text-align: left;padding: 5px left;border-radius: 10px;} QPushButton:focus{ outline: 0;}""")
        else:
            self.profile.setIcon(QIcon(os.path.join(curr_path,'Images\_female.svg')))
            self.profile.setIconSize(QSize(50, 50))
            self.profile.setText(name[0][0])
            self.profile.setStyleSheet("""*{font: 9pt "SansSerif";text-align: left;padding: 5px left;border-radius: 10px;} QPushButton:focus{ outline: 0;}""")
        conn.commit()
        conn.close()

        self.new_task.clicked.connect(new)
        self.scrollArea.setStyleSheet("*{background-color: rgba(255, 255, 255, 0);} QScrollArea{border: none;} QScrollBar{width: 12px; background : rgba(0, 0, 0, 0.1); border-radius: 6px;}QScrollBar::handle{background : orange; width: 10px; border-radius: 6px;}QScrollBar::handle::pressed{background : orange;}QScrollBar::sub-line:vertical{background: none;}QScrollBar::add-line:vertical {background: none;}")
        load()        

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor)) #Change the mouse icon
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
class ProgressBar_(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximum(100)
        self._active = False

    def updateBar(self, i):
        while True:
            time.sleep(0.01)
            value = i
            self.setValue(value)
            QApplication.processEvents()
            break              

    def changeColor(self, color):
        css = """
            ::chunk {{
                background: {0};
            }}
        """.format(color)
        self.setStyleSheet(css)

class Loading(QMainWindow):
    def __init__(self):
        super(Loading, self).__init__()
        loadUi(os.path.join(curr_path,'.ui\loading.ui'), self)
        self.setWindowTitle("Prioritize")
        self.setWindowIcon(QIcon(os.path.join(curr_path,'Images\img.ico')))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label1 = ProgressBar_()
        self.label1.setFixedWidth(500)

        self.label2 = ProgressBar_()
        self.label2.setFixedWidth(500)

        self.label3 = ProgressBar_()
        self.label3.setFixedWidth(500)

        self.label4 = ProgressBar_()
        self.label4.setFixedWidth(500)

        scene1 = QtWidgets.QGraphicsScene(self.graphicsView1)
        self.graphicsView1.setScene(scene1)
        proxy1 = QtWidgets.QGraphicsProxyWidget()

        scene2 = QtWidgets.QGraphicsScene(self.graphicsView2)
        self.graphicsView2.setScene(scene2)
        proxy2 = QtWidgets.QGraphicsProxyWidget()

        scene3 = QtWidgets.QGraphicsScene(self.graphicsView3)
        self.graphicsView3.setScene(scene3)
        proxy3 = QtWidgets.QGraphicsProxyWidget()

        scene4 = QtWidgets.QGraphicsScene(self.graphicsView4)
        self.graphicsView4.setScene(scene4)
        proxy4 = QtWidgets.QGraphicsProxyWidget()

        proxy1.setWidget(self.label1)
        proxy2.setWidget(self.label2)
        proxy3.setWidget(self.label3)
        proxy4.setWidget(self.label4)
        proxy1.setTransformOriginPoint(proxy1.boundingRect().center())
        proxy2.setTransformOriginPoint(proxy2.boundingRect().center())
        proxy3.setTransformOriginPoint(proxy3.boundingRect().center())
        proxy4.setTransformOriginPoint(proxy4.boundingRect().center())
        scene1.addItem(proxy1)
        proxy1.setRotation(315)
        scene2.addItem(proxy2)
        proxy2.setRotation(45)
        scene3.addItem(proxy3)
        proxy3.setRotation(135)
        scene4.addItem(proxy4)
        proxy4.setRotation(225)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgressBar)
        self.timer.start(35)

        self.label1.setStyleSheet("""QProgressBar {background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 0);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 12px;background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop: 1 rgba(170, 85, 255, 255));}""")
        self.label2.setStyleSheet("""QProgressBar {background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 0);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 12px;background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop: 1 rgba(170, 85, 255, 255));}""")
        self.label3.setStyleSheet("""QProgressBar {background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 0);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 12px;background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop: 1 rgba(170, 85, 255, 255));}""")
        self.label4.setStyleSheet("""QProgressBar {background-color: rgba(0, 0, 0, 0); color: rgba(0, 0, 0, 0);border-style: none;border-radius: 10px;text-align: center;}QProgressBar::chunk{border-radius: 12px;background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop: 1 rgba(170, 85, 255, 255));}""")
        self.loading_screen.setText('<img src="Images\_load1.svg" width=430 height=430></img>')

        self.load1.setText("")
        self.load2.setText("")
        self.load3.setText("")
        self.load4.setText("")
        self.load5.setText("")

    def updateProgressBar(self):
        val = 0
        times = 0
        created = False
        for i in range(1, 101):
            time.sleep(0.05)
            val = val + 10
            self.label1.updateBar(i)
            self.label2.updateBar(i)
            self.label3.updateBar(i)
            self.label4.updateBar(i)

            if val%160 == 0 and times<6:
                if times == 0:
                    self.load1.setText("Loading Resources")
                    self.loading_screen.setText('<img src="Images\_load1.svg" width=430 height=430></img>')
                if times == 1:
                    self.load1.setText("Resources loaded")
                    self.loading_screen.setText('<img src="Images\_load2.svg" width=430 height=430></img>')
                    if os.path.isfile('Prioritize\Databases\Prioritize.db'):
                        self.load2.setText("Locating Databases")
                    else:
                        created = True
                        self.load2.setText("Creating Databases")
                        conn =  sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
                        c = conn.cursor()
                        c.execute("""CREATE TABLE IF NOT EXISTS tasks(
                        task_name text,
                        description text,
                        due text,
                        pending int        
                        )
                        """)
                        conn.commit()
                        conn.close()
                if times == 2:
                    if created:
                        self.load2.setText("Databases Created")
                    else:
                        self.load2.setText("Databases Located")
                    self.loading_screen.setText('<img src="Images\_load3.svg" width=430 height=430></img>')
                    self.load3.setText("Finding your tasks")
                if times == 3:
                    self.load3.setText("Tasks found")
                    self.loading_screen.setText('<img src="Images\_load4.svg" width=430 height=430></img>')
                    self.load4.setText("Sorting them")
                if times == 4:
                    self.load4.setText("Sorting Completed")
                    self.loading_screen.setText('<img src="Images\_load5.svg" width=430 height=430></img>')
                    self.load5.setText("Creating UI")
                if times == 5:
                    self.load5.setText("UI Created")
                    self.loading_screen.setText('<img src="Images\_load6.svg" width=430 height=430></img>')
                times+=1
        conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
        c = conn.cursor()
        tasks_t = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'").fetchall()
        profile_t = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='personal_info'").fetchall()
        if os.path.isfile(os.path.join(curr_path,'Databases\Prioritize.db')) and tasks_t!=[] and profile_t!=[]:
            w = Window()
            w.setFixedSize(1300, 900)
            w.show()        
        else:
            g = get_started_()
            g.show()
        self.close()
        self.timer.stop()
                
def main():
    global app
    app = QApplication(sys.argv)

    def add_to_startup():
        import win32com.client
        import pythoncom
        path = 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\notification.lnk' % USER_NAME
        target = os.path.join(curr_path, 'Programs\\_notification.exe')
        icon = os.path.join(curr_path, 'Images\\img.ico') 

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.IconLocation = icon
        shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
        shortcut.save()

    if os.path.isfile('C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\notification.lnk' % USER_NAME):
        pass
    else:
        add_to_startup()

    s = Loading()
    s.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()