import psycopg2
from python.db.credentials import credentials

db_name=credentials.DB_NAME
db_user=credentials.DB_USER
db_pass=credentials.DB_PASS
db_host=credentials.DB_HOST

try:
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                        password=db_pass, host=db_host)
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("INSERT INTO test (ID, NUM, DATA) VALUES (2, 12, 'name12')")
conn.commit()

cur.execute("SELECT * from test")
print("Результат", cur.fetchall())
conn.close()
cur.close()