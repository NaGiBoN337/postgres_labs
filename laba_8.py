import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

connection = psycopg2.connect(database="students",
 user="postgres",
 password="Qazwsxedcf1-",
 host="127.0.0.1",
 port="5432")

cursor = connection.cursor()


sql = """
 select tab2.manager_name,salary_manager - avg_sub as "difference_salary"  
from 
	(select manager_id, avg(salary) as "avg_sub"  from employees e
	
	group by e.manager_id
	) tab1
join
	(select employee_id, salary as "salary_manager", concat(first_name,'\n',last_name) as "manager_name"  
	from employees e2
	) tab2

on tab1.manager_id = tab2.employee_id
order by 2;"""

df = pd.read_sql_query(sql, connection)
print(df)

colors = ["red" if i % 2 == 0 else "blue" for i in range(len(df['manager_name'])) ]

plt.title("Разница между зарплатой начальников и средней зарплатой их подчиненных")
plt.xlabel("manager_name")
plt.ylabel("difference_salary")
plt.bar(df['manager_name'], height=df['difference_salary'], color=colors)
plt.show()