@app.route("/pago")
def pago():
    return render_template("pago.html")

@app.route("/descargas")
def descargas():
    return render_template("descargas.html")
