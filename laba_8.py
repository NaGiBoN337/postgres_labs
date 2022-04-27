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

    sql = """
    select department_name,sum(salary) from employees 
    join departments d on employees.department_id = d.department_id
    group by employees.department_id,d.department_name;"""

    df2 = pd.read_sql_query(sql, connection)

    return df1,df2


def sql_select_location():
    sql = """
     select city,count(employee_id) from locations l 
     join employees e on e.location_id  = l.location_id
     group by city;"""
    df1 = pd.read_sql_query(sql, connection)
    return df1

def sql_call_f():
    sql = """SELECT * FROM select_dif_salary2(30,6000);"""
    df1 = pd.read_sql_query(sql, connection)
    sql = """SELECT * FROM sum_salary_departments(5000,30000);"""
    df2 = pd.read_sql_query(sql, connection)
    print(df1)
    print(df2)
    return df1,df2


def my_plt_show_vert(df,title):
    colors = ["red" if i % 2 == 0 else "blue" for i in range(len(df[df.columns[1]]))]
    plt.title(title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.bar(df[df.columns[0]], height=df[df.columns[1]], color=colors)
    plt.show()

def my_plt_show_hor(df,title):
    colors = ["orange" if i % 2 == 0 else "purple" for i in range(len(df[df.columns[1]]))]
    fig, ax = plt.subplots()
    ax.barh( df[df.columns[0]],df[df.columns[1]], align='center',color=colors)
    ax.set_yticks(df[df.columns[0]])
    ax.set_yticklabels(df[df.columns[0]])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_title(title)
    plt.show()

df1, df2 = sql_selects()

my_plt_show_vert(df1, "Разница между зарплатой начальников и средней зарплатой их подчиненных")
my_plt_show_vert(df2, "Отдел и сумма зарплат")

my_plt_show_hor(df1,"Разница между зарплатой начальников и средней зарплатой их подчиненных")
my_plt_show_hor(df2,"Отдел и сумма зарплат")

df3 = sql_select_location()
my_plt_show_hor(df3, "Количество сотрудников в разных городах")

sql_call_f()