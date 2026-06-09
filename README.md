Este projeto implementa uma API de gerenciamento de livros utilizando FastAPI, com integração ao Redis para cache, visando melhorar o desempenho das requisições.

## Tecnologias utilizadas

- Python 3.13
- FastAPI
- Redis
- Docker
- Kubernetes
- Poetry
- Pytest
- GitHub Actions
  
## Funcionalidades

- Criar livros
- Listar livros
- Atualizar livros
- Deletar livros
- Cache com Redis no endpoint `/listar`

## Executando com Docker

### Subir os containers

```bash
docker-compose up --build
```

### Acessar a API

Swagger:

```text
http://localhost:8000/docs
```

## Executando localmente

### Instalar dependências

```bash
pip install fastapi uvicorn redis
```

### Iniciar Redis

```bash
docker run -d -p 6379:6379 redis
```

### Executar a API

```bash
uvicorn main:app --reload
```

## Executando com Kubernetes

### Criar Deployment

```bash
kubectl apply -f deployment.yaml
```

### Criar Service

```bash
kubectl apply -f service.yaml
```

### Verificar recursos

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

## Endpoints

| Método | Rota | Descrição |
|---------|---------|---------|
| GET | `/listar` | Lista todos os livros |
| POST | `/criar` | Cria um livro |
| PUT | `/atualizar/{id}` | Atualiza um livro |
| DELETE | `/deletar/{id}` | Remove um livro |

## CI/CD com GitHub Actions    

O projeto utiliza também GitHub Actions para integração contínua.  

A cada push na branch principal:  

- Instala as dependências com Poetry  
- Executa os testes automatizados com Pytest  
- Valida a integridade da aplicação  
