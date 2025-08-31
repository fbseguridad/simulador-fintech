from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = "static/files"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    apps = [
        {"name":"Mercado Pago", "amount":5000},
        {"name":"Naranja X", "amount":5000},
        {"name":"BNA Cuenta DNI", "amount":5000},
        {"name":"Ualá", "amount":5000},
        {"name":"Brubank", "amount":5000},
        {"name":"Rebanking", "amount":5000},
        {"name":"Personal Pay", "amount":5000},
        {"name":"MODO", "amount":5000},
        {"name":"Galaxy Pay", "amount":5000},
        {"name":"PayPal", "amount":5000}
    ]
    return render_template("index.html", apps=apps)

@app.route("/descargas")
def descargas():
    files = os.listdir(DOWNLOAD_FOLDER)
    return render_template("descargas.html", files=files)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
