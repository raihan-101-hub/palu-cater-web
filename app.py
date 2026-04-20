from flask import Flask, render_template

app = Flask(__name__)

# Ganti localhost dengan alamat dari server database online nanti
app.config['MYSQL_HOST'] = 'mysql-19c16605-afriansyahraihan984-8c4f.g.aivencloud.com'
app.config['MYSQL_PORT'] = 20601
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_5AOsPTeK51vmOtCwXdM'
app.config['MYSQL_DB'] = 'defaultdb'

# --- DATA DUMMY (Simulasi Database) ---

# Data untuk Dashboard (Gambar 1.3)
orders = [
    {"customer": "Kantor Gubernur Sulteng", "wilayah": "Palu Timur", "status": "Proses Dapur", "total": "Rp 2.100.000"},
    {"customer": "Dinas Kesehatan Sigi", "wilayah": "Kab. Sigi", "status": "Pending", "total": "Rp 850.000"},
    {"customer": "Polres Palu", "wilayah": "Palu Selatan", "status": "Pengiriman", "total": "Rp 1.200.000"},
]

# Data untuk Inventaris (Gambar 1.5)
inventory = [
    {"bahan": "Beras Kepala", "stok": 50, "satuan": "Kg", "status": "Aman"},
    {"bahan": "Ayam Potong", "stok": 12, "satuan": "Ekor", "status": "Menipis"},
    {"bahan": "Bumbu Kaledo", "stok": 5, "satuan": "Pack", "status": "Aman"},
    {"bahan": "Minyak Goreng", "stok": 2, "satuan": "Liter", "status": "Kritis"},
]

# Data untuk Logistik (Gambar 1.6)
deliveries = [
    {"tujuan": "Jl. Sam Ratulangi", "kurir": "Andi", "estimasi": "10 Menit", "status": "OTW"},
    {"tujuan": "Kec. Marawola", "kurir": "Budi", "estimasi": "25 Menit", "status": "Packing"},
    {"tujuan": "Tawaeli", "kurir": "Cici", "estimasi": "15 Menit", "status": "OTW"},
]

# --- ROUTES (Navigasi Halaman) ---

@app.route('/login')
def login():
    """Halaman Masuk Sistem (Gambar 1.1)"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Halaman Daftar Akun Baru (Gambar 1.2)"""
    return render_template('register.html')

@app.route('/')
def dashboard():
    """Halaman Utama / Ringkasan Bisnis (Gambar 1.3)"""
    return render_template('dashboard.html', orders=orders)

@app.route('/input-order')
def input_order():
    """Halaman Form Tambah Pesanan (Gambar 1.4)"""
    return render_template('input_order.html')

@app.route('/inventory')
def show_inventory():
    """Halaman Stok Bahan Baku (Gambar 1.5)"""
    return render_template('inventory.html', inventory=inventory)

@app.route('/delivery')
def delivery():
    """Halaman Monitoring Pengiriman (Gambar 1.6)"""
    return render_template('delivery.html', deliveries=deliveries)

@app.route('/report')
def report():
    """Halaman Laporan Grafik Native (Gambar 1.7)"""
    return render_template('report.html')

if __name__ == '__main__':
    # Jalankan aplikasi dengan mode debug aktif
    app.run(debug=True)