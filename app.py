from flask import Flask, render_template, request, jsonify
import psycopg2 #pip install psycopg2 
import psycopg2.extras
  
app = Flask(__name__)
  
app.secret_key = "skillchen-secret_key"  

DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "dba"
      
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) 
 
@app.route('/')
def index(): 
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select * from emp01 order by id desc")
    emplist = cur.fetchall()
    return render_template('index.html',emplist=emplist)
  
@app.route("/delete",methods=["POST","GET"])
def delete():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for getid in request.form.getlist('checkdelete'):
        print(getid)
        cur.execute('DELETE FROM employee WHERE id = {0}'.format(getid))
        conn.commit()      
    cur.close()
    return jsonify('Records deleted successfully')  

     
if __name__ == "__main__":
    app.run(debug=True)