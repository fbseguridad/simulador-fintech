@app.route("/pago")
def pago():
    return render_template("pago.html")

@app.route("/descargas")
def descargas():
    return render_template("descargas.html")
import os
from flask import Flask

app = Flask(__name__)

# Aquí van tus rutas y lógica

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto
    app.run(host="0.0.0.0", port=port)
