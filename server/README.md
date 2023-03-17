# Wydra API
## Dependencies
- Python
- FastAPI
- Uvicorn

## Running
```sh
    uvicorn main:wydra --reload
```
O servidor poderá ser acessado em http://localhost:8000/

## Documentation
Execute o comando acima e navegue para http://localhost:8000/docs

## Architecture & File Structure
### Model
Código para acessar o banco de dados, classes orm, e schemas de respostas da api.

### Control 
Controladores para classes do domínio, como usuário, obra, etc.


