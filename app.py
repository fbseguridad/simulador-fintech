import os
from flask import Flask, render_template, request, redirect, send_from_directory, url_for

app = Flask(__name__)

# Carpeta para archivos estáticos
app.static_folder = "static"

# Contadores simulados (visitas y descargas)
visitas = 12345
descargas = 6789

# Ruta principal
@app.route("/")
def index():
    global visitas
    visitas += 1  # cada visita suma
    return render_template("index.html", visitas=visitas)

# Ruta descargas
@app.route("/descargas")
def descargas_page():
    global descargas
    descargas += 2  # simulación de descargas cada vez que entran
    return render_template("descargas.html", descargas=descargas)

# Ruta de pago simulada
@app.route("/pago")
def pago():
    return render_template("pago.html")

# Servir archivos de static/files si los necesitan
@app.route("/files/<filename>")
def serve_file(filename):
    return send_from_directory(os.path.join(app.static_folder, "files"), filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto
    app.run(host="0.0.0.0", port=port, debug=True)
