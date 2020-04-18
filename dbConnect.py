# pip install MySQL-python
# pip install MySQL-python-connector

import MySQLdb 
  
db = MySQLdb.connect("localhost","testuser","testpassword","gfgdb" ) # Open database connection 
  
cursor = db.cursor() 
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")     # Drop table if it already exist using execute() 
  
db.close()                                          # disconnect from server 



#>>> cursor.execute('select * from books')
#>>> cursor.fetchall()
#(('Py9098', 'Programming With Python', 100L, 50L), ('Py9099', 'Programming With Python', 100L, 50L))
