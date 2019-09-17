from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)

app.config['MYSQL_HOST']='sql12.freemysqlhosting.net'
app.config['MYSQL_USER']='sql12305300'
app.config['MYSQL_PASSWORD']='giUjsZkz3R'
app.config['MYSQL_DB']='sql12305300'
mysql=MySQL(app)

@app.route('/', methods=['GET','POST'])
def register():
	if request.method=='POST':
		d=request.form
		email=d['email']
		password=d['password']
		conn = MySQLdb.connect(host="sql12.freemysqlhosting.net", user = "sql12305300", passwd = "giUjsZkz3R", db = "sql12305300")
		cur = conn.cursor()
		cur.execute("select * from noteligible")
		conn.commit()
		r=cur.fetchall()
		k=list(r)
		c=0
		for i in k:
			if i[1]==email:
				if i[2]==password:
					c=c+1
		if c>=1:
			return redirect("https://keen-davinci-444eed.netlify.com/")
		else:
			return render_template("loginerror.html")
	return render_template("login.html")
if __name__ == '__main__':
	app.run(debug=True)
