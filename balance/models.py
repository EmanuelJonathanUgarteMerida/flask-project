import csv

from balance import FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.movimientos.append(Movimiento(
                    linea['fecha'], linea['concepto'], linea['ingreso_gasto'], linea['cantidad']))
