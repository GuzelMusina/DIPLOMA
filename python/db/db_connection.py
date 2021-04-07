import psycopg2
from python.db.credentials import credentials
import pandas as pd

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
# cur.execute("INSERT INTO test (ID, NUM, DATA) VALUES (2, 12, 'name12')")
# conn.commit()
# data = pd.read_csv(r'..\..\data\Logs_1.csv')
data = open('..\..\data\Logs_1.csv', 'r')

# cur.copy_from(data, "moodle_log", columns=('id', 'component', 'action', 'target',
#                                            'objecttable', 'userid', 'courseid', 'timecreated',
#                                            'movements', 'date', 'date_and_time'), sep=',')
conn.commit()
conn.close()
cur.close()