import sqlite3

def table_init():
    con = sqlite3.connect('mydb.db')
    cur = con.cursor()
    # Initialize table
    try:
        cur.execute('''CREATE TABLE history
                (id INTEGER PRIMARY KEY,
                time varchar(40) NOT NULL,
                statement varchar(100) NOT NULL)''')
    except:
        pass
    print('Database Initialized.')

def add_to_history(time, st):
    print(time, st)
    con = sqlite3.connect('mydb.db')
    cur = con.cursor()
    # Initialize table
    try:
        cur.execute('''CREATE TABLE history
                (id INTEGER PRIMARY KEY,
                time varchar(40) NOT NULL,
                statement varchar(100) NOT NULL)''')
    except:
        pass

    cur.execute("INSERT INTO history(time, statement) VALUES ('"+time+"', '"+st+"');")
    # cur.execute("INSERT INTO history(time, statement) VALUES ('24-06-2222', 'statement - 1');")

    # data = cur.execute("SELECT * FROM history;")
    # for row in data:
    #     print(row)

    # cur.execute('''drop table history'''); print('table deleted.')

    con.commit()

# add_to_history('23-10-2021 17:54:08', '2021-10-23 : 0')