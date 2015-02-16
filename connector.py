import MySQLdb

db = MySQLdb.connect(
    host="mysql.server",
    user="humantrashcan",
    passwd="pyth0n",
    db="humantrashcan$default")
	
#setup cursor
cursor = db.cursor()

#add currency pairs to currency pair table
#cursor.execute("INSERT INTO currency(currency_pair) VALUES('GBPEUR')")
#cursor.commit()

#cursor.execute("SELECT * FROM currency")
#rows = cursor.fetchall()
#
#for row in rows:
#    print row

