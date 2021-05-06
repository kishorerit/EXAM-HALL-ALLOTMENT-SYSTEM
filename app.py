from flask import Flask, render_template, request
from flask import Flask, render_template, json, request
#from flask_mysqldb import MySQL
#from werkzeug import generate_password_hash, check_password_hash
import pymysql
import sys
import pymysql.cursors
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
from flask import flash
#from werkzeug import secure_filename
from flask import Flask, session, redirect, url_for, escape, request
#from settings import PROJECT_ROOT
import os
import datetime
#import mysql.connector
#import mysql.connector
app = Flask(__name__)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='hallallotment',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def student():
    return render_template('home.html')


@app.route('/subclick', methods=['POST', 'GET'])
def subclick():
    try:
        if request.method == 'POST':
            sid = request.form["sid"]
            sname = request.form["sname"]
            cid = request.form["cid"]
            det = request.form["det"]

            # validate the received values
            if sid and sname:

                try:
                    with connection.cursor() as cursor:
                        # _hashed_password = generate_password_hash(pwd)
                        # Read a single record
                        sql = "INSERT INTO subject VALUES (%s, %s, %s, %s)"
                        cursor.execute(sql, (sid, sname, cid, det))
                        connection.commit()
                except Exception as e:
                    print(str(e))
                finally:
                    connection.close()
                    return "Saved successfully."
                data = cursor.fetchall()

            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})

    finally:
        # cursor.close()
        return render_template("adminhome.html")
    connection.close()



@app.route('/courseclick', methods=['POST', 'GET'])
def courseclick():
        try:
            if request.method == 'POST':
                p1 = request.form["fname"]
                p2 = request.form["lname"]
                p3 = request.form["addr"]
                p4 = request.form["ph"]
                p5 = request.form["email"]
                p6 = request.form["log"]
                p7 = request.form["pwd"]

                # validate the received values
                if p1 and p2:


                    with connection.cursor() as cursor:
                        # _hashed_password = generate_password_hash(pwd)
                        # Read a single record
                        sql = "INSERT INTO allotment VALUES (null, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (p1, p2, p3, p4, p5, p6, p7))
                        connection.commit()
                        sql = "select * from allotment"
                        cursor.execute(sql)
                        res = cursor.fetchall()
                        connection.commit()
                        return render_template("adminentry.html", data1=res)
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})
        finally:
            cursor.close()
            return render_template("adminentry.html", data1=res)


@app.route('/adeletecourse/<int:id>',methods = ['POST', 'GET'])
def adeletecourse(id):
    try:
       if request.method == 'GET':
          # validate the received values
          if id:
              try:
                  connection = pymysql.connect(host='localhost',
                                               user='root',
                                               password='',
                                               db='hallallotment',
                                               charset='utf8mb4',
                                               cursorclass=pymysql.cursors.DictCursor)
                  with connection.cursor() as cursor1:
                      # Read a single record
                      sql = "delete from allotment where id=%s"
                      cursor1.execute(sql, (id))
                      connection.commit()
                      sql = "select * from allotment"
                      cursor1.execute(sql)
                      data12 = cursor1.fetchall()
                      connection.commit()
                      return render_template("adminentry.html", data1=data12, eid=0)
                      #return render_template("adminviewusers.html", data=data, eid=0)
              except Exception as e:
                  print(str(e))
          else:
              return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
       return json.dumps({'error': str(e)})


@app.route('/feesclick', methods=['POST', 'GET'])
def feesclick():
    try:
        if request.method == 'POST':
            tid = request.form["tid"]
            vname = request.form["vname"]
            from1 = request.form["from"]
            to = request.form["to"]
            fees = request.form["fees"]
            # validate the received values
            if tid and vname:

                try:
                    with connection.cursor() as cursor:
                        # _hashed_password = generate_password_hash(pwd)
                        # Read a single record
                        sql = "INSERT INTO transport VALUES (%s, %s, %s, %s, %s)"
                        cursor.execute(sql, (tid, vname, from1, to, fees))
                        connection.commit()
                except Exception as e:
                    print(str(e))
                finally:
                    connection.close()
                    return "Saved successfully."
                data = cursor.fetchall()

            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})

    finally:
        # cursor.close()
        return render_template("adminhome.html")
    connection.close()


@app.route('/regclick', methods=['POST', 'GET'])
def regclick():
    try:
        if request.method == 'POST':
            p1 = request.form["fname"]
            p2 = request.form["lname"]
            p3 = request.form["addr"]
            p4 = request.form["ph"]
            p5 = request.form["email"]
            p6 = request.form["log"]
            p7 = request.form["pwd"]
            # validate the received values
            if p1 and p2:

                try:
                    with connection.cursor() as cursor:
                        # _hashed_password = generate_password_hash(pwd)
                        # Read a single record
                        sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (p1, p2, p3, p4, p5, p6, p7))
                        connection.commit()
                except Exception as e:
                    print(str(e))
                finally:
                    connection.close()
                    return "Saved successfully."
                data = cursor.fetchall()

            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})

    finally:
        # cursor.close()
        return render_template("login.html")
    connection.close()


@app.route('/adminlogin', methods=['POST', 'GET'])
def adminlogin():
    return render_template("adminlogin.html")


@app.route('/adminhome', methods=['POST', 'GET'])
def adminhome():
    return render_template("adminhome.html")



@app.route('/adminentry1', methods=['POST', 'GET'])
def adminentry1():
    try:
        with connection.cursor() as cursor:
            sql1 = "select * from allotment"
            cursor.execute(sql1)
            data1 = cursor.fetchall()
            connection.commit()
            #return data1 # render_template("addcourse.html", data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        #connection.close()
        return render_template("adminentry.html", data1=data1)




@app.route('/addfees', methods=['POST', 'GET'])
def addfees():
    return render_template("addtransport.html")


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    return render_template("register.html")


@app.route('/studentlogin', methods=['POST', 'GET'])
def studentlogin():
    return render_template("login.html")


@app.route('/shome', methods=['POST', 'GET'])
def shome():
    return render_template("studenthome.html")


@app.route('/asigninclick', methods=['POST', 'GET'])
def asigninclick():
    if request.method == 'POST':
        try:
            email = request.form["email"]
            pwd = request.form["pwd"]
            # validate the received values
            if email and pwd:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='hallallotment',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    # res = "select * from signup where email=%s and pwd=%s"
                    sql = "select * from adminlogin where uname=%s and pwd=%s"
                    cursor.execute(sql, (email, pwd))
                    res = cursor.fetchall()
                    if len(res) == 1:
                        connection.commit()
                        connection.close()
                        return render_template('adminhome.html')

                    else:
                        flash('Invalid', 'success')
                        error = "Invalid login"
                        connection.commit()
                        connection.close()
                        return "Invalid login"

        except Exception as e:
            return json.dumps({'error': str(e)})


@app.route('/usigninclick1', methods=['POST', 'GET'])
def usigninclick1():
    if request.method == 'POST':
        try:
            email = request.form["email"]
            pwd = request.form["pwd"]

            # validate the received values
            if email and pwd:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='hallallotment',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    # res = "select * from signup where email=%s and pwd=%s"
                    sql = "select * from student where user=%s and pwd=%s"
                    cursor.execute(sql, (email, pwd))
                    res = cursor.fetchall()
                    if len(res) == 1:
                        connection.commit()
                        connection.close()
                        session['username'] = email
                        return render_template('userhome.html')

                    else:
                        error = "Invalid login"
                        connection.commit()
                        connection.close()
                        return "Invalid login"


        except Exception as e:
            return json.dumps({'error': str(e)})


@app.route('/viewstudent', methods=['POST', 'GET'])
def viewstudent():
    try:
        with connection.cursor() as cursor:
            sql = "select * from student"
            cursor.execute(sql)
            data = cursor.fetchall()
            return render_template("adminview.html", data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/viewallott', methods=['POST', 'GET'])
def viewallott():
    try:
        eam=session['username']
        with connection.cursor() as cursor:
            sql = "select * from allotment where name=%s"
            cursor.execute(sql, eam)
            data = cursor.fetchall()
            return render_template("userviewbooks.html", data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/udeletecomp/<int:id>', methods=['POST', 'GET'])
def udeletecomp(id):
    try:
        if request.method == 'POST':
            # validate the received values
            if id:
                try:
                    connection = pymysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 db='hallallotment',
                                                 charset='utf8mb4',
                                                 cursorclass=pymysql.cursors.DictCursor)
                    with connection.cursor() as cursor:
                        # Read a single record
                        sql = "delete from course where id=%s"
                        cursor.execute(sql, (id))
                        # return redirect("deleted")
                except Exception as e:
                    print(str(e))
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})


def viewcourse1():
    try:
        with connection.cursor() as cursor:
            sql = "select * from course"
            cursor.execute(sql)
            data = cursor.fetchall()
            return data  # render_template("addcourse.html", data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/viewsubject', methods=['POST', 'GET'])
def viewsubject():
    try:
        with connection.cursor() as cursor:
            sql = "select * from subject"
            cursor.execute(sql)
            data = cursor.fetchall()
            return render_template("viewsubject.html", data=data)
    except Exception as e:
        return json.dumps({'error': str(e)})




if __name__ == '__main__':
    app.secret_key = 'lfjsdlkfjdklsjfkl1'
    app.run(port=5009)

