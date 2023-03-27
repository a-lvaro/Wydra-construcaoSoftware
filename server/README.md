# Wydra API

## TO-DO
- [ ] Refatoração
    - [x] Reestruturar código para ORM e modelos
    - [ ] Mover código de autenticação para core/security
    - [ ] Mover o resto do código do módulo services para o módulo api
- [ ] Melhorar autenticação

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

### Services 
Serviços oferecidos pela API, como autenticação e funcionalidades de alto nível.
