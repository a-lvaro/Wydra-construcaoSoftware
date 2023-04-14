# Wydra API
## TO-DO

- [ ] Melhorar autenticação
- [ ] Testes

## Running

```sh
    poetry run uvicorn main:wydra --reload
```
O servidor poderá ser acessado em http://localhost:8000/

## Documentation

Execute o comando acima e navegue para http://localhost:8000/docs

## Architecture & File Structure

### App

Funcionalidade geral da API.
- **controlers**: Controladores para entidades do domínio
- **models**: Modelos para tabelas do banco de dados
- **schemas**: Classes pydantic para validação de dados

### API

Interface da API para o cliente.

### Core

Funcionalidades básicas, como acesso ao banco de dados e segurança.
