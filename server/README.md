# Wydra API

## Dependencies
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- tmdbsimple

## Running
```sh
    uvicorn main:wydra --reload
```
O servidor poderá ser acessado em http://localhost:8000/

## Documentation
Execute o comando acima e navegue para http://localhost:8000/docs

## Architecture & File Structure
### Model
Código para acessar o banco de dados, acessar APIs externas, e modelos de respostas da API.

### Control 
Controladores para classes do domínio, como usuário, obra, etc.

### Services
Serviços oferecidos pela API, como autenticação e funcionalidades de alto nível.
