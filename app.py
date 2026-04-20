from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi Database Aiven
app.config['MYSQL_HOST'] = 'mysql-19c16605-afriansyahraihan984-8c4f.g.aivencloud.com'
app.config['MYSQL_PORT'] = 20601
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_5AOsPTeK51vmOtCwXdM' # Password sesuai gambar kamu
app.config['MYSQL_DB'] = 'defaultdb'

mysql = MySQL(app)

@app.route('/')
def dashboard():
    # 1. Hubungkan ke Database
    cursor = mysql.connection.cursor()
    
    # 2. Ambil data dari tabel 'orders' yang kamu buat di HeidiSQL tadi
    cursor.execute("SELECT customer_name, wilayah, status, total_bayar FROM orders")
    
    # 3. Simpan hasil query ke variabel 'data_orders'
    data_orders = cursor.fetchall()
    
    # 4. Tutup koneksi
    cursor.close()
    
    # 5. Kirim data ke file HTML (templates/dashboard.html)
    return render_template('dashboard.html', orders=data_orders)

if __name__ == '__main__':
    app.run(debug=True)
