import sqlite3


conn = sqlite3.connect('db.sqlite3')


cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Таблицы:", tables)


cursor.execute("SELECT * FROM main_app_infoforpage;")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Закрываем соединение
conn.close()
