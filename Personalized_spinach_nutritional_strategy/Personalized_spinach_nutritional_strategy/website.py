import csv
from array import array
from flask import Flask, render_template, flash, request, session, Response, url_for, send_from_directory, current_app, send_file, redirect

import ar_master
import os
from datetime import datetime
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
mm=ar_master.master_flask_code()
no_of_days_apsent=1
@app.route("/")
def homepage():
    return render_template('index.html')
# @app.route("/admin", methods = ['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         un = request.form['username']
#         pa = request.form['password']
#         usern = mm.select_direct_query("select * from admin_details where username='" + str(un) + "' and password='" + str(pa) + "'")
#         if usern:
#             session['username'] = usern
#             return render_template('admin_home.html', flash_message=True,data="Login Success")
#         else:
#             return render_template('admin.html', flash_message=True,data="Login Failed")
#     return render_template('admin.html')

@app.route("/user_home", methods = ['GET', 'POST'])
def user_home():
    folder_path = 'train'
    all_items = os.listdir(folder_path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(folder_path, item))]
    return render_template('user_home.html',items=directories,result="")

@app.route("/login", methods = ['GET', 'POST'])
def student():
    if request.method == 'POST':
        un = request.form['username']
        pa = request.form['password']
        usern = mm.select_direct_query("select * from user_details where name='" + str(un) + "' and password='" + str(pa) + "'")
        if usern:
            session['username'] = un
            # return render_template("user_home.html")
            # return render_template('user_home.html', flash_message=True,data="Login Success")
            return  redirect("/user_home")
        else:
            return render_template('student.html', flash_message=True,data="Login Failed")
    return render_template('student.html')
# @app.route("/admin_home", methods = ['GET', 'POST'])
# def admin_home():
#     return render_template('admin_home.html')



@app.route("/user_home_1", methods = ['GET', 'POST'])
def user_home_1():
    folder_path = 'train'
    all_items = os.listdir(folder_path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(folder_path, item))]
    if request.method == 'POST':
        type = request.form['select']
        state = request.form['select2']
        file = os.path.join("train",type,str(type+".csv"))
        result=""
        with open(file) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                if state == row['Stages']:
                    result=row
                    print(result)
                    return render_template('user_home.html',result=result,items=directories)
        return render_template('user_home.html',result=result,items=directories)
@app.route("/user_register", methods = ['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        student_name = request.form['student_name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']

        password = request.form['password']

        maxin = mm.find_max_id("user_details")
        qq = "insert into user_details values('" + str(maxin) + "','" + str(student_name) + "','" + str(contact) + "','" + str(email) + "','" + str(address) + "','"+str(password)+"')"
        mm.insert_query(qq)
        # return render_template('student_register.html', flash_message=True, data="Registration Successfully")
        return redirect("/login")
    return render_template('student_register.html')
# @app.route("/staff", methods = ['GET', 'POST'])
# def staff():
#     if request.method == 'POST':
#         un = request.form['username']
#         pa = request.form['password']
#         usern = mm.select_direct_query("select * from staff_details where staff_name='" + str(un) + "' and password='" + str(pa) + "'")
#         if usern:
#             session['username'] = un
#             return render_template('staff_home.html', flash_message=True,data="Login Success")
#         else:
#             return render_template('staff.html', flash_message=True,data="Login Failed")
#     return render_template('staff.html')
# @app.route("/staff_home", methods = ['GET', 'POST'])
# def staff_home():
#     return render_template('staff_home.html')
# @app.route("/staff_attendance", methods = ['GET', 'POST'])
# def staff_attendance():
#     data=mm.select_direct_query("select DISTINCT department from student_details")
#     if request.method == 'POST':
#         department = request.form['department']
#         session['department']=department
#         return redirect(url_for("staff_attendance_1"))
#     return render_template('staff_attendance.html',items=data)
# @app.route("/staff_attendance_1", methods = ['GET', 'POST'])
# def staff_attendance_1():
#     department=session['department']
#     data = mm.select_direct_query("select DISTINCT year from student_details where department='" + str(department) + "'")
#     if request.method == 'POST':
#         year = request.form['year']
#         section = request.form['section']
#         hour = request.form['hour']
#         session['year'] = year
#         session['section'] = section
#         session['hour'] = hour
#         data = mm.select_direct_query("select * from student_details where department='" + str(department) + "' and year='"+str(year)+"' and section='"+str(section)+"'")
#         session['reg']=data
#         return render_template('staff_attendance_2.html',items=data)
#     return render_template('staff_attendance_1.html',items=data)
# @app.route("/staff_attendance_update", methods = ['GET', 'POST'])0
# def staff_attendance_update():
#     staff = session['username']
#     department = session['department']
#     hour = session['hour']
#     year = session['year']
#     section = session['section']
#     if request.method == 'POST':
#         reg=session['reg']
#         dict={}
#         email={}
#         for x in reg:
#             did=(request.form.get(x[8]))
#             dict[x[8]]=did
#             email[x[8]]=x[11]
#         qry="insert into attendance values "
#         current_datetime = datetime.now()
#         current_date = current_datetime.date()
#         current_time = current_datetime.time()
#         formatted_datetime = current_datetime.strftime("%H:%M:%S")
#         month = str(current_datetime.month)
#         for x in dict:
#             qry+="('"+str(staff)+"','"+str(department)+"','"+str(year)+"','"+str(section)+"','"+str(current_date)+"','"+str(formatted_datetime)+"','"+str(x)+"','"+str(dict[x])+"','"+str(hour)+"','"+str(month)+"'),"
#         qry = qry[:-1]
#         mm.insert_query(qry)
#         qry = "select reg_no,(count(DISTINCT cdate))>'"+str(no_of_days_apsent)+"' from attendance where status='Apsent' GROUP BY reg_no,status"
#         items = mm.select_direct_query(qry)
#         attendnace = {}
#         for x in items:
#             if x[1]>0:
#                 attendnace[x[0]]=x[1]
#         for id in attendnace:
#             email_id=email[id]
#             msg=str(id)+"-taken more Leave"
#             mm.send_email_without_attachment(email_id,msg)
#     return redirect(url_for("staff_attendance"))
# @app.route("/staff_view_student", methods = ['GET', 'POST'])
# def staff_view_student():
#     data = mm.select_direct_query(
#         "select * from student_details")
#     return render_template('staff_view_student.html',items=data)
# @app.route("/student_report", methods = ['GET', 'POST'])
# def student_report():
#     student=session['username']
#     data = mm.select_direct_query("select * from attendance where reg_no='"+str(student)+"'")
#     return render_template('student_report.html',items=data)
# @app.route("/staff_view_report", methods = ['GET', 'POST'])
# def staff_view_report():
#     data=mm.select_direct_query("select DISTINCT department from student_details")
#     if request.method == 'POST':
#         department = request.form['department']
#         session['department']=department
#         return redirect(url_for("staff_view_report_1"))
#     return render_template('staff_view_report.html',items=data)
# @app.route("/staff_view_report_1", methods = ['GET', 'POST'])
# def staff_view_report_1():
#     department=session['department']
#     data = mm.select_direct_query("select DISTINCT year from student_details where department='" + str(department) + "'")
#     if request.method == 'POST':
#         year = request.form['year']
#         section = request.form['section']
#         hour = request.form['hour']
#         date = request.form['date']
#         qry="select * from attendance where department='" + str(department) + "' and year='" + str(
#                 year) + "' and section='" + str(section) + "' and cdate='"+str(date)+"' and hour='"+str(hour)+"'"
#         data = mm.select_direct_query(qry)
#         return render_template('staff_view_report_2.html', items=data)
#     return render_template('staff_view_report_1.html',items=data)
# @app.route("/admin_view_student", methods = ['GET', 'POST'])
# def admin_view_student():
#     data=mm.select_direct_query("select * from student_details")
#     return render_template('admin_view_student.html',items=data)
# @app.route("/admin_view_staff", methods = ['GET', 'POST'])
# def admin_view_staff():
#     data=mm.select_direct_query("select * from staff_details")
#     return render_template('admin_view_staff.html',items=data)
# @app.route("/admin_view_report", methods = ['GET', 'POST'])
# def admin_view_report():
#     data=mm.select_direct_query("select * from attendance order by cdate DESC")
#    return render_template('admin_view_report.html',items=data)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,host="0.0.0.0")