import sqlite3

conn = sqlite3.connect("celebrities.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS celebs (
    celebID text PRIMARY KEY,
    firstname text,
    lastname text,
    age text,
    email text,
    photo text,
    bio text
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS members (
    memberID text PRIMARY KEY,
    firstname text,
    lastname text,
    age text,
    email text,
    bio text
)
""")

sql = "insert into celebs values (?,?,?,?,?,?,?)"
data = [
    (1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402021/aj.jpg", ""),
    (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402021/bp.jpg",""),
    (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402021/sw.jpg"
,""),
    (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402021/dv.jpg",""),
    (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402021/ts.jpg"
,""),
    (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402021/bk.jpg", ""),
    (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402021/sg.jpg",""),
    (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402021/sc.jpg", "")
    ]
c.executemany(sql,data)

conn.commit()




