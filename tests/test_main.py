import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from main import app, livros

client = TestClient(app)


def setup_function():
    livros.clear()


def test_listar_livros():
    response = client.get("/listar")

    assert response.status_code == 200
    assert response.json() == []


def test_criar_livro():
    response = client.post(
        "/criar",
        json={
            "id": 1,
            "titulo": "O sacrificio",
            "autor": "Edson",
            "ano": 2025
        }
    )

    assert response.status_code == 200
    assert response.json()["titulo"] == "O sacrificio"


def test_atualizar_livro():
    client.post(
        "/criar",
        json={
            "id": 1,
            "titulo": "o sacrificio",
            "autor": "Edson",
            "ano": 2025
        }
    )

    response = client.put(
        "/atualizar/1",
        json={
            "id": 1,
            "titulo": "noventa sacrificios",
            "autor": "Edson",
            "ano": 2026
        }
    )

    assert response.status_code == 200
    assert response.json()["titulo"] == "noventa sacrificios"


def test_deletar_livro():
    client.post(
        "/criar",
        json={
            "id": 1,
            "titulo": "o sacrificio",
            "autor": "Edson",
            "ano": 2025
        }
    )

    response = client.delete("/deletar/1")

    assert response.status_code == 200
    assert response.json()["mensagem"] == "Livro deletado com sucesso"