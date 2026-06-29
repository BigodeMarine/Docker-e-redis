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
- ELK Stack
  
## Funcionalidades

- Criar livros
- Listar livros
- Atualizar livros
- Deletar livros
- Cache com Redis no endpoint `/listar`

## Observabilidade com ELK Stack

A aplicação pode enviar logs para o Elasticsearch através do Logstash.

Fluxo:

FastAPI → Logstash → Elasticsearch → Kibana

O Logstash realiza o parsing dos logs, o Elasticsearch armazena os dados e o Kibana permite a visualização e análise.

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

- Checkout do código  
- Instalação das dependências com Poetry  
- Execução dos testes com Pytest  
- Construção da imagem Docker da aplicação  
- Validação da execução do container  

## 📊 Integração do ELK Stack no projeto  

- **FastAPI:** gera logs da aplicação em formato JSON.
- **Logstash:** realiza a leitura dos logs, faz o parsing e envia os dados para o Elasticsearch.
- **Elasticsearch:** armazena e indexa os logs para consultas rápidas.
- **Kibana:** permite visualizar e analisar os logs através de uma interface web.  

### Benefícios da integração  

- Centralização dos logs da aplicação.
- Monitoramento em tempo real.
- Facilidade na identificação de erros.
- Análise de desempenho da aplicação.
- Suporte à observabilidade em ambientes containerizados.