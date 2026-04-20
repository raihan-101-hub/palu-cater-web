from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'katering_smp26_sigi' # Kunci rahasia untuk session

# Konfigurasi Database Aiven
app.config['MYSQL_HOST'] = 'mysql-19c16605-afriansyahraihan984-8c4f.g.aivencloud.com'
app.config['MYSQL_PORT'] = 20601
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_5AOsPTeK51vmOtCwXdM'
app.config['MYSQL_DB'] = 'defaultdb'

mysql = MySQL(app)

# 1. Halaman Utama (Sekarang Login, bukan Dashboard)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['loggedin'] = True
            session['username'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            return "Login Gagal! Username atau Password salah."
    
    return render_template('login.html')

# 2. Halaman Dashboard (Hanya bisa dibuka kalau sudah login)
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT customer_name, wilayah, status, total_bayar FROM orders")
        data_orders = cursor.fetchall()
        cursor.close()
        return render_template('dashboard.html', username=session['username'], orders=data_orders)
    
    return redirect(url_for('login'))

# 3. Fitur Logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
