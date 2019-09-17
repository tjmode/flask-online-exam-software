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
	ans=[]
	if request.method=='POST':
		mark=0
		d=request.form
		name=d['username']
		for i in range(1,30):
			a=d[str(i)]
			ans.append(a)
		print(ans)
		ans1=["c","c","b","b","b","a","c","a","a","c","a","d","c","b","c","a","c","d","c","b","b","a","a","c","c","b","c","b","a","b"]
		for j in range(len(ans1)-1):
			if ans[j]==ans1[j]:
				mark=mark+1
		conn = MySQLdb.connect(host="sql12.freemysqlhosting.net", user = "sql12305300", passwd = "giUjsZkz3R", db = "sql12305300")
		cur = conn.cursor()
		cur.execute("update noteligible set mark=%s where email=%s",[mark,name])
		conn.commit()
		cur.execute("select *from noteligible")
		r=cur.fetchall()
		k=list(r)		
		# a1=d['1']
		# a2=d['2']
		# a3=d['3']
		# a4=d['4']
		# a5=d['5']
		# a6=d['6']
		# a7=d['7']
		# a8=d['8']
		# a9=d['9']
		# a10=d['10']
		# a11=d['11']
		# a12=d['12']
		# a13=d['13']
		# a14=d['14']
		# a15=d['15']
		# a16=d['16']
		# a17=d['17']
		# a18=d['18']
		# a19=d['19']
		# a20=d['20']
		# a21=d['21']
		# a22=d['22']
		# a23=d['23']
		# a24=d['24']
		# a25=d['25']
		# a26=d['26']
		# a27=d['27']
		# a28=d['28']
		# a29=d['29']
		# a30=d['30']
		# ans.append(a1)
		# ans.append(a2)
		# ans.append(a3)
		# ans.append(a4)
		# ans.append(a5)
		# ans.append(a6)
		# ans.append(a7)
		# ans.append(a8)
		# ans.append(a9)
		# ans.append(a10)
		# ans.append(a11)
		# ans.append(a12)
		# ans.append(a13)
		# ans.append(a14)
		# ans.append(a15)
		# ans.append(a16)
		# ans.append(a17)
		# ans.append(a18)
		# ans.append(a19)
		# ans.append(a20)
		# ans.append(a21)
		# ans.append(a22)
		# ans.append(a23)
		# ans.append(a24)
		# ans.append(a25)
		# ans.append(a26)
		# ans.append(a27)
		# ans.append(a28)
		# ans.append(a29)
		# ans.append(a30)
		# print(ans)
		print(mark)

	return render_template("newqp.html")
if __name__ == '__main__':
	app.run(debug=True)