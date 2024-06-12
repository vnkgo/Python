from pymysql import connect
conn=connect(host='localhost',port=3306,user='root',password='root')
cursor=conn.cursor()
conn.select_db('myworld')
cursor.execute("select * from student")0


