import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
print("TABLES:", [r[0] for r in cur.fetchall()])

cur.execute("SELECT id, name, price FROM shop_product")
print("PRODUCTS:", cur.fetchall())

cur.execute("SELECT id, title, slug FROM shop_category")
print("CATEGORIES:", cur.fetchall())

cur.execute("SELECT id, title, slug, sub_headline, body_text FROM shop_pagecontent")
print("PAGES:", cur.fetchall())

conn.close()
