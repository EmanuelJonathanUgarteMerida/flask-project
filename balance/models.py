import csv
import datetime
from os import write

from balance import FICHERO
from datetime import date, datetime


class Movimiento:
    def __init__(self, linea):
        # validamos fecha
        """self.errores = []
        ahora = datetime.now()
        try:
            self.fecha = date.fromisoformat(linea['fecha'])
            if self.fecha.strftime('%Y%m%d') > ahora.strftime('%Y%m%d'):
                self.errores.append(
                    'la fecha no puede ser superior al la fecha actual')
        except ValueError:
            self.errores.append('Formato de fecha erróneo')"""
        self.fecha = linea['fecha']
        self.hora = linea['hora']
        self.concepto = linea['concepto']
        self.tipo = linea['tipo']
        self.cantidad = linea['cantidad']


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.movimientos.append(Movimiento(linea))

    def escribir_archivo(self):
        with open(FICHERO, 'w') as fichero:
            writer = csv.DictWriter(
                fichero, self.movimientos[0].__dict__.keys())
            writer.writeheader()
            for mov in self.movimientos:
                writer.writerow(mov.__dict__)
