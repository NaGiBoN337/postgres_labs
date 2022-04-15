import pandas as pd
import psycopg2
connection = psycopg2.connect(database="students",
 user="postgres",
 password="Qazwsxedcf1-",
 host="127.0.0.1",
 port="5432")

cursor = connection.cursor()
for i in connection.get_dsn_parameters():
    print(i,":", connection.get_dsn_parameters()[i])
sql = "SELECT * FROM jobs " # запрос SQL
df = pd.read_sql_query("SELECT * FROM jobs ", connection)
print(df)
