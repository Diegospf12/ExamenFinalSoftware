from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pytest
from fastapi.testclient import TestClient
from api import app, Cuenta, BD
from datetime import datetime

client = TestClient(app)

def test_pagar_exitoso():
    # Caso de prueba: Pago exitoso
    response = client.post("/billetera/pagar", params={"minumero": "21345", "numerodestino": "123", "valor": 50})
    assert response.status_code == 200
    assert response.json() == "Realizado en " + datetime.now().strftime("%d/%m/%Y")

def test_pagar_saldo_insuficiente():
    # Caso de prueba: Pago fallido debido a saldo insuficiente
    response = client.post("/billetera/pagar", params={"minumero": "21345", "numerodestino": "123", "valor": 300})
    assert response.status_code == 200
    assert response.json() != "Saldo insuficiente"

def test_pagar_cuenta_inexistente():
    # Caso de prueba: Pago fallido debido a cuenta inexistente
    response = client.post("/billetera/pagar", params={"minumero": "99999", "numerodestino": "123", "valor": 50})
    assert response.status_code == 200
    assert response.json() == "Cuenta inexistente"

def test_historial_cuenta_inexistente():
    # Caso de prueba: Historial fallido debido a cuenta inexistente
    response = client.get("/billetera/historial", params={"minumero": "99999"})
    assert response.status_code == 200
    assert response.json() == "Cuenta inexistente"