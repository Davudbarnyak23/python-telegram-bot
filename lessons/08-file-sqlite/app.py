import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()


#cur.execute(" CREATE TABLE user(name, year, title);")
# cur.execute(''' CREATE TABLE user_all(
#         id INTEGER PRIMARY KEY,
#         name TEXT DEFAULT 'NN',
#         year INTEGER DEFAULT 0,
#         title TEXT NOT NULL
#     );''')
# con.commit()

 cur.execute("INSERT INTO user_all (name, year, title) VALUES ('non', 2000, 'tttt');")
 con.commit()


con.close()