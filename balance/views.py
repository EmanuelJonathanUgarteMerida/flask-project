# pondremos las rutas y lo que se va hacer al llegar a ellas

from balance.models import ListaMovimientos, Movimiento
from . import app
from flask import render_template, request


@app.route('/')
def inicio():
    listaMovimientos = ListaMovimientos()
    listaMovimientos.leer_archivo()
    return render_template('inicio.html', movs=listaMovimientos.movimientos)


@app.route('/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        return render_template('alta.html')
    else:
        movimiento = Movimiento(request.form)
        lm = ListaMovimientos()
        lm.leer_archivo()
        lm.movimientos.append(movimiento)
        lm.escribir_archivo()
        return request.form
