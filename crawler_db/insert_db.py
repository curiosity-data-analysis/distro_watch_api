import MySQLdb
import csv

db = MySQLdb.connect(host="localhost",
	user="distrowatch",
	passwd="distrowatch",
	db="distrowatch")

'''
function that performs the population of the database with the data collected from the DistroWatch
'''
def insert_ranking_db():
	cursor = db.cursor()
	csv_12_months = csv.reader(file('file_12_months.csv'))
	csv_6_months = csv.reader(file('file_6_months.csv'))
	csv_3_months = csv.reader(file('file_3_months.csv'))
	csv_1_months = csv.reader(file('file_1_months.csv'))
	for row in csv_12_months:
		cursor.execute('INSERT INTO ranking_12_months(ranking,distribution,hit_ranking)' \
			'VALUES("%s", "%s", "%s")', 
			row)
	for row in csv_6_months:
		cursor.execute('INSERT INTO ranking_6_months(ranking,distribution,hit_ranking)' \
			'VALUES("%s", "%s", "%s")', 
			row)
	for row in csv_3_months:
		cursor.execute('INSERT INTO ranking_3_months(ranking,distribution,hit_ranking)' \
			'VALUES("%s", "%s", "%s")', 
			row)
	for row in csv_1_months:
		cursor.execute('INSERT INTO ranking_1_months(ranking,distribution,hit_ranking)' \
			'VALUES("%s", "%s", "%s")', 
			row)
	db.commit()
	cursor.close()
	print "Done"

if __name__ == '__main__':
	insert_ranking_db()