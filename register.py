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
		username=d['username']
		email=d['email']
		password=d['password']
		mark=0
		conn = MySQLdb.connect(host="sql12.freemysqlhosting.net", user = "sql12305300", passwd = "giUjsZkz3R", db = "sql12305300")
		cur = conn.cursor()
		cur.execute("select * from noteligible")
		conn.commit()
		#cur.execute("INSERT INTO noteligible(username,email,password,mark) VALUES(%s, %s,%s,%s)",(username,email,password,mark))
		#cur.execute("select * from eligible")
		#conn.commit()
		#cur.close()
		c=0
		r=cur.fetchall()
		k=list(r)
		print(k)
		for i in k:
			if i[1]==email:
				c=c+1
		if c>=1:
			return render_template("signuperror.html")
		else:
			cur.execute("INSERT INTO noteligible(username,email,password,mark) VALUES(%s, %s,%s,%s)",(username,email,password,mark))
			conn.commit()
			cur.close()
			return render_template("veralevel.html")
	return render_template("register.html")
if __name__ == '__main__':
	app.run(debug=True)
