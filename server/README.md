# Wydra API

## Dependencies
- Python
- FastAPI
- Uvicorn

## Running
```sh
    uvicorn main:wydra --reload
```
O servidor podera ser acessado em http://localhost:8000/

## Documentation
Execute o comando acima e navegue para http://localhost:8000/docs

## Architecture & File Structure
### Domain
Classes pertinentes ao domínio da aplicação, como usuários, obras, etc., e seus controladores.

### Data Abstraction Layer (DAL)
Código para acesso aos bancos de dados e outros recursos.


