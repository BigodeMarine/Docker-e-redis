from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio
import redis
import json
import os

# FastAPI
app = FastAPI()

# conexão com Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

# função para deletar cache
async def deletar_livros_redis():
    redis_client.delete("livros")

# modelo de dados
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int

# função para salvar no Redis
async def salvar_livros_redis(livros: List[Livro]):
    # converte objetos para dict
    livros_dict = [livro.model_dump() for livro in livros]

    # salva como JSON
    redis_client.set("livros", json.dumps(livros_dict))

    # define TTL
    redis_client.expire("livros", 60)

# "banco de dados" em memória
livros: List[Livro] = []

# função para listar os livros
@app.get("/listar", response_model=List[Livro])
async def listar_livros():
    await asyncio.sleep(1.0)

    # tenta pegar do Redis
    cache = redis_client.get("livros")

    if cache:
        print("📦 Dados vindo do CACHE")
        return json.loads(cache)

    # se não tiver cache, pega do "banco"
    print("🐢 Dados vindo da LISTA")

    # salva no Redis
    await salvar_livros_redis(livros)

    return livros

# função para criar os livros
@app.post("/criar", response_model=Livro)
async def criar_livro(livro: Livro):
    await asyncio.sleep(0.1)

    for l in livros:
        if l.id == livro.id:
            raise HTTPException(status_code=400, detail="Livro já existe")

    livros.append(livro)

    # limpa cache
    await deletar_livros_redis()

    return livro

# função para atualizar os livros
@app.put("/atualizar/{id}", response_model=Livro)
async def atualizar_livro(id: int, livro_atualizado: Livro):
    await asyncio.sleep(0.1)

    for index, livro in enumerate(livros):
        if livro.id == id:
            livros[index] = livro_atualizado

            await deletar_livros_redis()
            return livro_atualizado

    raise HTTPException(status_code=404, detail="Livro não encontrado")

# função para deletar os livros
@app.delete("/deletar/{id}")
async def deletar_livro(id: int):
    await asyncio.sleep(0.1)

    for index, livro in enumerate(livros):
        if livro.id == id:
            livros.pop(index)

            await deletar_livros_redis()
            return {"mensagem": "Livro deletado com sucesso"}

    raise HTTPException(status_code=404, detail="Livro não encontrado")