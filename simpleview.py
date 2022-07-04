#!/usr/bin/python

import psycopg2
from flask import Flask,abort,request,render_template,render_template_string

app = Flask(__name__,template_folder='.')

def get_database(site):
	try:
		conn = psycopg2.connect(
			host="10.10.94.129",
			port="7777",
			database="gsm_check",
			user="postgres",
			password="postgres")

		cur = conn.cursor()
		cur.execute("select * from %s" % site)
		data=cur.fetchall()
		conn.close()
		return data
	except:
		abort(404)

@app.errorhandler(404)
def page_not_found(e):
	return render_template_string('Site not found {{ errorCode }}', errorCode='404'), 404

@app.route('/get',methods=['GET'])
def index():
	args = request.args
	site = args.get('site')
	data = get_database(site)
	return render_template('bootstrap_table.html',title="GSM Check",data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)	