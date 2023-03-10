CREATE DATABASE IF NOT EXISTS WYDRA;

USE WYDRA;

-- tabela para usuário

CREATE TABLE
    USUARIO (
        ID_USUARIO INT NOT NULL AUTO_INCREMENT,
        NOME VARCHAR(30) NOT NULL,
        EMAIL VARCHAR(30) NOT NULL,
        SENHA VARCHAR(64) NOT NULL,
        CAMINHO_IMAGEM VARCHAR(100) NULL,
        PRIMARY KEY (ID_USUARIO)
    );

-- tabela para obras na estante

CREATE TABLE
    OBRAS_ESTANTE (
        ID_USUARIO INT,
        ID_OBRA INT,
        ESTADO ENUM(
            'Lista de Desejos',
            'Em progresso',
            'Finalizada',
            'Abandonada'
        ),
        FOREIGN KEY (ID_USUARIO) REFERENCES USUARIO(ID_USUARIO),
        PRIMARY KEY (ID_USUARIO, ID_OBRA) # restringe de uma mesma obra constar duas vezes na mesma estante
    );

-- SHA2('senha', 256) -> criptografa a senha

INSERT INTO
    USUARIO (
        NOME,
        EMAIL,
        SENHA,
        CAMINHO_IMAGEM
    )
VALUES (
        'nome',
        'email',
        SHA2('senha', 256),
        'caminho da imagem'
    );

-- se retornou o registro há o cadastro daquela pessoa e dessa determinada senha

-- caso contrário não está cadastrado ou a senha não está correta

SELECT email, senha
FROM USUARIO
WHERE
    email = 'email'
    AND senha = SHA2('senha', 256);

# atualizar email do usuario
UPDATE USUARIO
SET email = 'novoEmail'
WHERE email = 'email';

# atualiza a senha do usuário
UPDATE USUARIO
SET
    senha = SHA2('novaSenha', 256)
WHERE email = 'email';

# atualizar o nome do usuário
UPDATE USUARIO
SET nome = 'novoNome'
WHERE email = 'email';