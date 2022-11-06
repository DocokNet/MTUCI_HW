import requests
from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == '' or password == '':
        return render_template('empty_error.html', empty_error='Some authorisation fields are empty!')
    else:   
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if records == []:
            return render_template('missing_user.html', missing_user_error='There is no such user registrated!')
        else:
            return render_template('account.html', full_name=f'{records[0][1]}', login_pass=f'Login = {records[0][2]}, password = {records[0][3]}')


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

