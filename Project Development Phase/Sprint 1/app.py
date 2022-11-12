import ibm_db
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.debug=True

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhl91628;PWD=vM4lAZjxo4LsBPoJ","","")

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/signup", methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        name = request.form['fname']
        username =name.split(" ")[0]
        email = request.form['femail']
        mobile = request.form['mobile']
        password = request.form['password']
        
        sql = "SELECT * FROM customers WHERE username =? and email=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            return render_template('registered.html')
        else:
            insert_sql = "INSERT INTO customers VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, username)
            ibm_db.bind_param(prep_stmt, 3, email)
            ibm_db.bind_param(prep_stmt, 4, mobile)
            ibm_db.bind_param(prep_stmt, 5, password)
            ibm_db.execute(prep_stmt)
            return render_template('success.html')
    
    return render_template('signup.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signin" , methods=('GET', 'POST'))
def signin():
    if request.method == 'POST':
        femail = request.form['femail']
        fpassword = request.form['password']
        
        sql = "SELECT * FROM customers WHERE email =? and password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,femail)
        ibm_db.bind_param(stmt,2,fpassword)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            return render_template('loginsuccess.html')
        else:
            return render_template('loginfailure.html')
            
    return render_template('signin.html')

if __name__ == '__main__':
    app.run()


    