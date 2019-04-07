from flask import Flask, redirect, url_for, request, render_template
import time
import socket

app = Flask(__name__)

@app.route('/success')
def success():
   return 'You have registered...'

@app.route('/registration_failed')
def failed():
   return 'Oh Snap! There is something wrong'

@app.route('/attendance_failed')
def failed_att():
   return 'Oh Snap! There is something wrong'

@app.route('/attendence_success')
def attendence_success():
   return 'Attendence taken...'

@app.route('/register',methods = ['POST', 'GET'])

def login():
   if request.method == 'POST':
       port = 12345
       #Extracking information from the page
       name = request.form['name']
       name01 = name.replace(" ","_")
       roll_no = request.form['r_no']

       student_info = "r_"+roll_no+"_"+name01

       # connect to the server on
       # local computer
       s = socket.socket()
       s.connect(('10.4.120.55', port))
       s.send(student_info.encode('utf-8'))
       status_msg = s.recv(1024).decode('utf-8')
       if status_msg == 'ok':
           s.close()
           return redirect(url_for('success'))
       else:
           s.close()
           return redirect(url_for('failed'))



   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


@app.route('/take_attendence', methods=['POST', 'GET'])
def attendence():
    if request.method == 'POST':
        port = 12345
        # Extracking information from the page
        course_code = request.form['coursecode']
        class_id = request.form['classid']

        attendence_info = "t_"+course_code+ "_" +class_id

        # connect to the server on
        # local computer
        s = socket.socket()
        s.connect(('10.4.120.55', port))
        s.send(attendence_info.encode('utf-8'))
        status_msg01 = s.recv(1024).decode('utf-8')
        if status_msg01 == 'ok':
            s.close()
            return redirect(url_for('attendence_success'))
        else:
            s.close()
            return redirect(url_for('failed_att'))


    else:
        user = request.args.get('nm')
        return redirect(url_for('attendence_success', name=user))

if __name__ == '__main__':
   app.run(debug = True)

