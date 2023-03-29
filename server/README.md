# Wydra API

## TO-DO
- [ ] Refatoração
    - [x] Reestruturar código para ORM e modelos
    - [x] Mover código de autenticação para core/security
    - [x] Mover o resto do código do módulo services para os módulos api e app
    - [ ] Exception handling
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

### Control 
Controladores para classes do domínio, como usuário, obra, etc.

### Services
Serviços oferecidos pela API, como autenticação e funcionalidades de alto nível.
