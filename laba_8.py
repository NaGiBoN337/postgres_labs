import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

connection = psycopg2.connect(database="students",
 user="postgres",
 password="Qazwsxedcf1-",
 host="127.0.0.1",
 port="5432")

cursor = connection.cursor()

def sql_selects():
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

    df1 = pd.read_sql_query(sql, connection)
    #print(df1)
    sql = """
    select department_name,sum(salary) from employees 
    join departments d on employees.department_id = d.department_id
    group by employees.department_id,d.department_name;"""

    df2 = pd.read_sql_query(sql, connection)
    #print(df2)
    return df1,df2

def my_plt_show(df,title):
    colors = ["red" if i % 2 == 0 else "blue" for i in range(len(df[df.columns[1]]))]
    plt.title(title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.bar(df[df.columns[0]], height=df[df.columns[1]], color=colors)
    plt.show()

df1, df2 = sql_selects()

print(df1.columns)
print(df2.columns)


my_plt_show(df1, "Разница между зарплатой начальников и средней зарплатой их подчиненных")
my_plt_show(df2, "Отдел и сумма зарплат")