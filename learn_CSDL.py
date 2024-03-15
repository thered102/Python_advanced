import pyodbc
connect = pyodbc.connect('Driver={SQL Server};'
                         'Server=LAPTOP-SATTI01\SQLEXPRESS;'
                         'Database=QL;'
                         'Trusted_Connection=yes')
cursor = connect.cursor()
# cursor.execute("insert into QLNS values ('2023005', 'tran van d', 'sw')") # insert
# cursor.execute("update QLNS set Hoten ='nguyen van tinh' where Magen='2023004'")# update
cursor.execute("delete QLNS where MaGen='2023005'")
cursor.commit()
cursor.execute('select * from QLNS')
for i in cursor:
    print(i)