import pyodbc
conn_str = 'Driver={SQL Server};Server=DESKTOP-PMFB2J2\SQLEXPRESS;Database=furniture;Trusted_Connection=yes;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute('SELECT * FROM Customer')
rows = cursor.fetchall()
print(rows)
conn.close()

