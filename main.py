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

"""cursor.execute('''CREATE TABLE if not exists locations
                 (location_id int PRIMARY KEY,
                city varchar(30),
                postal_code varchar(12)
                ); ''')
connection.commit()
"""
sql =""" INSERT INTO locations VALUES ( 2,'Venice','10934');
INSERT INTO locations VALUES ( 3,'Tokyo', '1689');
INSERT INTO locations VALUES ( 4,'Hiroshima','6823');
INSERT INTO locations VALUES ( 5,'Southlake', '26192');
INSERT INTO locations VALUES ( 6,'South San Francisco', '99236');
INSERT INTO locations VALUES ( 7,'South Brunswick','50090');
INSERT INTO locations VALUES ( 8,'Seattle','98199');
INSERT INTO locations VALUES ( 9,'Toronto','M5V 2L7');
INSERT INTO locations VALUES ( 10,'Whitehorse','YSW 9T2');

"""
#cursor.execute(sql)
#connection.commit()
table_locations = pd.read_sql_query("SELECT * FROM locations ", connection)
print(table_locations)


postgresql_func = """
CREATE OR REPLACE FUNCTION select_data1(id_dept int) RETURNS
SETOF departments AS $$
SELECT * FROM departments WHERE departments.department_id > id_dept;
$$ LANGUAGE SQL;
"""
#cursor.execute(postgresql_func)
#connection.commit()


#sql ="ALTER TABLE hr.employees ADD location_id int4 NULL;"
sql = "ALTER TABLE employees ADD CONSTRAINT mgr_emp_fkey FOREIGN KEY (location_id) REFERENCES locations  (location_id);"
#cursor.execute(sql)
#connection.commit()
import random
for i in range(54):
    sql = "UPDATE hr.employees SET location_id=" + str(random.randint(1,10)) + " WHERE employee_id=" + str(i) + ";"
    cursor.execute(sql)
    connection.commit()

connection.close()
cursor.close()