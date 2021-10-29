# pondremos las rutas y lo que se va hacer al llegar a ellas

from balance.models import ListaMovimientos, Movimiento
from . import app
from flask import render_template


@app.route('/')
def inicio():
    listaMovimientos = ListaMovimientos()
    listaMovimientos.leer_archivo()
    return render_template('inicio.html', movs=listaMovimientos.movimientos)


@app.route('/alta')
def alta():
    return render_template('alta.html')
