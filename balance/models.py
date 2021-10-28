import csv

from balance import FICHERO
from datetime import date


class Movimiento:
    def __init__(self, linea):
        # validamos fecha
        self.fecha = date.fromisoformat(linea['fecha'])
        self.hora = linea['hora']
        self.concepto = linea['concepto']
        self.tipo = linea['ingreso_gasto']
        self.cantidad = linea['cantidad']


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.movimientos.append(Movimiento(linea))
