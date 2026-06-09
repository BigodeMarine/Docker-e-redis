 API de Livros com FastAPI + Redis

Este projeto implementa uma API de gerenciamento de livros utilizando FastAPI, com integração ao Redis para cache, visando melhorar o desempenho das requisições.

 Tecnologias utilizadas  
Python 3.13  
FastAPI  
Redis  
Docker   
Funcionalidades  
Criar livros  
Listar livros  
Atualizar livros  
Deletar livros  
Cache com Redis no endpoint de listagem (/listar)  
Uso do Redis (Cache)  

A API utiliza o Redis para armazenar temporariamente a lista de livros.  

Estratégia utilizada: Cache Aside  
A API verifica se os dados estão no Redis  
Se estiverem → retorna diretamente do cache  
Se não → busca da lista em memória e salva no Redis  
Qualquer alteração (POST, PUT, DELETE) remove o cache  
📁 Estrutura do projeto  
.  
├── main.py  
├── Dockerfile  
├── docker-compose.yml  
├── deployment.yaml  
├── service.yaml  
└── README.md  

🐳 Executando com Docker
1. Subir os containers
docker-compose up --build
2. Acessar a API
Swagger:
http://localhost:8000/docs

💻 Executando localmente (sem Docker)
1. Instalar dependências
pip install fastapi uvicorn redis

☸️ Executando com Kubernetes
Este projeto também pode ser executado em um cluster Kubernetes utilizando os manifestos deployment.yaml e service.yaml.

Aplicando os recursos

Criar o Deployment:

kubectl apply -f deployment.yaml

Criar o Service:

kubectl apply -f service.yaml
Verificando os recursos

Listar Deployments:

kubectl get deployments

Listar Pods:

kubectl get pods

Listar Services:

kubectl get services

2. Iniciar o Redis
✔️ Usando Docker:
docker run -d -p 6379:6379 redis

3. Rodar a API
uvicorn main:app --reload
📌 Endpoints
Método	Rota	Descrição
GET	/listar	Lista todos os livros
POST	/criar	Cria um livro
PUT	/atualizar/{id}	Atualiza um livro
DELETE	/deletar/{id}	Remove um livro

Execute duas vezes:

curl http://localhost:8000/listar
1ª vez → dados vêm da memória
2ª vez → dados vêm do Redis
🔍 Verificando dados no Redis

Abra outro terminal:

redis-cli

Depois:

GET livros

Se estiver funcionando, você verá os dados em formato JSON.

🔄 Invalidação do cache

O cache é removido automaticamente quando:

Um livro é criado (POST)
Um livro é atualizado (PUT)
Um livro é deletado (DELETE)
📌 Métodos principais implementados

salvar_livros_redis:Responsável por armazenar a lista de livros no Redis com TTL.

deletar_livros_redis:Responsável por remover os dados do Redis quando houver alterações.
