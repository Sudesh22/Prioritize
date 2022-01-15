import sqlite3, datetime
def create_table():
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE tasks(
        task_name text,
        description text,
        date_created timestamp,
        due timestamp,
        pending int        
    )
    """)
    conn.commit()
    conn.close()

def sort():
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("SELECT pending FROM customers ORDER BY last_name DESC")

    conn.commit()

    # Query the database order by
    # c.execute("SELECT rowid,* FROM customers")# Typesof datatypes in sqlite3: null, int, real, text, blob

    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our commands
    conn.commit()

    conn.close()

def delete_table(name):
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("DROP TABLE " + name)
    conn.commit()
    conn.close()

def add_data(task, desc):
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES (?,?,?,?,?)", (task, desc, datetime.datetime.now(), ))
    print("Command executed sucessfully...")
    conn.commit()
    conn.close()

def delete(name,id):
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("DELETE from " + name + " WHERE rowid = ?", (id,))
    conn.commit()

def deleteAll(name):
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    num = c.execute("SELECT rowid, * FROM " + name).fetchall()
    for i in range(len(num)+1):
        c.execute("DELETE from " + name + " WHERE rowid = ?", (i,))
    conn.commit()

def print_data(name):
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM " + name)
    items = c.fetchall()
    # print(items[1][1])
    for item in items:
        # for i in enumerate(item, start=1):
            # print(item[1])
            print(item)

def print_tables():
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'ORDER BY name;")
    items = c.fetchall()
    # print(items[1][1])
    for item in items:
        # for i in enumerate(item, start=1):
            # print(item[1])
            print(item)

def check_table(name):
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    table = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + name + "'").fetchall()
    if table==[]:
        print("No such table exists!")
    else:
        print("Table exists!")

def t_n_list():
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    t_name = c.execute("SELECT task_name FROM tasks").fetchall()
    for i in range(len(t_name)):
        print(t_name[i][0])

def adding():
    i = int(input())
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    for j in range(i):
        t = str(input())
        d = str(input())
        y = str(input())
        m = str(input())
        d = str(input())
        M = str(input())
        h = str(input())
        c.execute("INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?)", (t, d, y, m, d, M, h, 1))
        conn.commit()
    conn.close()
        
def update():
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET due_y = 2021 WHERE rowid = 1")
    conn.commit()
    conn.close()

def sort():
    conn = sqlite3.connect('Prioritize.db')
    c = conn.cursor()

    # c.execute("SELECT rowid,* FROM tasks WHERE pending=1 ORDER BY due_y")
    # conn.commit()
    # c.execute("SELECT rowid,* FROM tasks WHERE pending=1 ORDER BY due_m")
    # conn.commit()
    # c.execute("SELECT rowid,* FROM tasks WHERE pending=1 ORDER BY due_d")
    # conn.commit()
    # c.execute("SELECT rowid,* FROM tasks WHERE pending=1 ORDER BY due_hour")
    # conn.commit()
    c.execute("SELECT rowid,* FROM tasks ORDER BY due DESC")
    items = c.fetchall()
    # print(items[1][1])
    # for item in items:
    for item in enumerate(items, start=1):
            # print(item[1])
            a = c.execute("SELECT * FROM tasks WHERE rowid = " + str(item[1][0]))
            print(item)
    conn.commit()
    conn.close()
# select * from myTable
# if Password != NULL then Password = 'Yes'
# else Password = 'No'

# create_table()
# delete_table('tasks')
# add_data('hi', 'jsv x jcbsd ')
# delete("tasks",16)
# deleteAll("tasks")
# print_data("tasks")
# print_tables()
# t_n_list()
# adding()
# update()
sort()
# -----> SELECT * FROM Table ORDER BY dateColumn DESC Limit 1

# check_table("personal_info")

# conn = sqlite3.connect('Prioritize.db')
# c = conn.cursor()
# record = c.execute("SELECT rowid, * FROM tasks WHERE rowid = ?", (str(5))).fetchall()

# tasks_e = c.execute("SELECT rowid, * FROM tasks").fetchall()
# n_t_id = enumerate(tasks_e)
# print(num) 
# print(record[0])
# name = record[0][1]
# print(name)

# conn =  sqlite3.connect('Prioritize.db')
# c = conn.cursor()
# t_name = c.execute("SELECT task_name FROM tasks").fetchall()
# print(type(t_name))

# rad_but = []
# for i in range(0,len(t_name)):
#     r = '_r'
#     t_name[i]
#     rad_but.append(t_name[i][0] + r)
# print(rad_but)
# today = datetime.datetime.now().strftime("%Y-%m-%d")
# next = int(today[8:10])+1
# week = int(today[8:10])+7
# if week<10:
#     week = "0"+str(week)
# if next<10:
#     next = "0"+str(next)
# week = today[0:8] + str(week)
# next = today[0:8] + str(next)
# # print(today, next, week)

# current_date = datetime.datetime.now().strftime("%Y-%m-%d")
# current_date_temp = datetime.datetime.strptime(current_date, "%Y-%m-%d")
# newdate = str(current_date_temp + datetime.timedelta(days=30))
# # print(current_date, newdate[0:10])

# today = datetime.datetime.now().strftime("%Y-%m-%d")
# tod_temp = datetime.datetime.strptime(today, "%Y-%m-%d")
# next = str(tod_temp + datetime.timedelta(days=1))
# week = str(tod_temp + datetime.timedelta(days=7))
# month = str(tod_temp + datetime.timedelta(days=30))
# print(today, next[0:10], week[0:10], month[0:10])