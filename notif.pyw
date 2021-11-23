import sys, sqlite3, datetime, os, time, getpass
from os.path import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import operator

USER_NAME = getpass.getuser()
if getattr(sys, 'frozen', False):
        curr_path = os.path.dirname(sys.executable)
elif __file__:
        curr_path = os.path.dirname(__file__)
# print(curr_path)

conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
c = conn.cursor()
c.execute("SELECT * FROM tasks ORDER BY due DESC LIMIT 1")
due = c.execute("SELECT rowid,due FROM tasks WHERE due BETWEEN '2021-11-05 00:00:00' AND '2021-11-05 23:59:59'").fetchall()
# sorted(due, key=operator.itemgetter(1))
# print(due)
today = datetime.datetime.now().strftime("%Y-%m-%d")
print("SELECT rowid,due FROM tasks WHERE due BETWEEN '"+today+" 00:00:00' AND '"+today+" 23:59:59'")

def Secondary():
    while 1:
        import numpy as np
        conn = sqlite3.connect(os.path.join(curr_path,'Databases\Prioritize.db'))
        c = conn.cursor()
        
        c.execute("SELECT * FROM tasks ORDER BY due DESC LIMIT 1")
        # today = datetime.datetime.now().strftime("%Y-%m-%d")
        due = c.execute("SELECT due FROM tasks ORDER BY due DESC LIMIT 1").fetchone()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        executed = np.ones((1,len(due)))
        print(executed)
        print(now + " : " + due[0])
        if due[0] == now:
            print("Due!!!")
        #     main()
        # if i>=len(due):    
        time.sleep(0.5)
# Secondary()
# print(int("6 "))
import logging
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logging.debug(now)

def has_executed(executed, due):
    n=0
    with open("test.log") as fp:
        for line in fp:
            line = fp.readline()
            if line.startswith(due[line][0], 11):
                n+=1
                line[]