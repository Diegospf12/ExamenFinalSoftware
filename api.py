from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime
from typing import List, Dict

#uvicorn api:app --reload
#source venv/bin/activate
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Operacion:
    def __init__(self, numero_destino: str, valor: int):
        self.numero_destino = numero_destino
        self.fecha = datetime.now().strftime("%d/%m/%Y")
        self.valor = valor

class Cuenta:
    def __init__(self, numero: str, nombre: str, saldo: int, contactos: List[str]):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos
        self.historial = []

    def pagar(self, numero_destino: str, valor: int):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historial.append(Operacion(numero_destino, valor))
            return True
        else:
            return False

    def historial(self):
        return self.historial

BD = []
BD.append(Cuenta("21345", "Arnaldo", 200, ["123", "456"]))
BD.append(Cuenta("123", "Luisa", 400, ["456"]))
BD.append(Cuenta("456", "Andrea", 300, ["21345"]))

@app.get('/billetera/contactos')
async def contactos(minumero: str):
    for cuenta in BD:
        if cuenta.numero == minumero:
            return {contacto: next((c.nombre for c in BD if c.numero == contacto), None) for contacto in cuenta.contactos}
        
@app.post('/billetera/pagar')
async def pagar(minumero: str, numerodestino: str, valor: int):
    for cuenta in BD:
        if cuenta.numero == minumero:
            if cuenta.pagar(numerodestino, valor):
                cuenta.saldo -= valor
                for c in BD:
                    if c.numero == numerodestino:
                        c.saldo += valor
                        c.historial.append(f'Pago recibido de {valor} de {cuenta.nombre} en {datetime.now().strftime("%d/%m/%Y")}')
                return "Realizado en " + datetime.now().strftime("%d/%m/%Y")
            else:
                return "Saldo insuficiente"

@app.get('/billetera/historial')
async def historial(minumero: str):
    for cuenta in BD:
        if cuenta.numero == minumero:
            return {"saldo": cuenta.saldo, "historial": cuenta.historial}
