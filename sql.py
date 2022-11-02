import sqlite3 as sql

boglash = sql.connect("sql_top.db")

malumot = boglash.cursor()

malumot = boglash.execute(""" 
CREATE TABLE IF NOT EXISTS Student(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)
""")

malumot = boglash.execute("""
CREATE TABLE IF NOT EXISTS Programist(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)
""")

malumot = boglash.execute("""
CREATE TABLE IF NOT EXISTS Bekorchilar(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)
""")

malumot = boglash.execute("""
CREATE TABLE IF NOT EXISTS SHifokor(
ism TEXT,
fam TEXT,
yosh INTEGER
)

""")

malumot = boglash.execute("""
CREATE TABLE IF NOT EXISTS Quruvchi(
ism TEXT,
fam TEXT,
yosh INTEGER
)

""")

malumot = boglash.execute("""
CREATE TABLE IF NOT EXISTS Tadbirkor(
ism TEXT,
fam TEXT,
yosh INTEGER
)

""")