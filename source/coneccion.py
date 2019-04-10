import pymysql
# Open database connection
#db = pymysql.connect("127.0.0.1",3306,"root","admin1sql","practicapython" )
db = pymysql.connect(
    host="127.0.0.1", port=3306, user="root",
    passwd="admin1sql", db="practicapython"
)
# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)
