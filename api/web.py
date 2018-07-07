import flask, MySQLdb, time
from flask_mysqldb import MySQL
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import json
from flask import jsonify

app = Flask(__name__)
mysql = MySQL(app)
app.config['JSON_AS_ASCII'] = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'distrowatch'
app.config['MYSQL_PASSWORD'] = 'distrowatch'
app.config['MYSQL_DB'] = 'distrowatch'
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ranking_12_months')
def ranking_12_months():
    cur = mysql.connection.cursor()
    cur.execute("select * from ranking_12_months")
    row_headers=[x[0] for x in cur.description] 
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify({'ranking_12_months': json_data})


if __name__ == '__main__':
	app.run(
    host="localhost",
    port=int("5000"),
    debug=True
	)