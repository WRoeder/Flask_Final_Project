from flask import Flask,redirect,url_for,request,render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enterproduct')
def new_product():
    return render_template('product.html')

@app.route('/addrecord',methods = ['POST','GET'])
def addrecord():
    if request.method == 'POST':
        try:
            pn = request.form['pn']
            pc = request.form['pc']
            pd = request.form['pd']
            pq = request.form['pq']
            cd = request.form['cd']

            with sql.connect("databasefinal.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO products (productname,category,description,quantity,checkdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(pn,pc,pd,pq,cd))
                con.commit()
                msg = "Record successfully added."
        except:
            con.rollback()
            msg = "Error in insert operation."

        finally:
            return render_template("result.html",msg = msg)

@app.route('/viewinventory')
def viewinventory():
    con = sql.connect("databasefinal.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()
    return render_template("inventory.html", rows = rows)

if __name__ == '__main__':
    app.run(debug = True)