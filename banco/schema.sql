CREATE DATABASE IF NOT EXISTS WYDRA;
USE WYDRA;

-- tabela para usuário
CREATE TABLE
    USUARIO (
        ID_USUARIO INT NOT NULL AUTO_INCREMENT,
        NOME VARCHAR(30) NOT NULL,
        EMAIL VARCHAR(30) NOT NULL,
        SENHA VARCHAR(64) NOT NULL,
        PRIMARY KEY (ID_USUARIO)
    );

-- tabela para obras na estante
CREATE TABLE
	OBRAS_ESTANTE (
		ID_USUARIO INT,
        ID_OBRA INT,
        ESTADO ENUM('Lista de Desejos', 'Em progresso', 'Finalizada', 'Abandonada'),
        FOREIGN KEY (ID_USUARIO) REFERENCES USUARIO(ID_USUARIO),
        PRIMARY KEY (ID_USUARIO, ID_OBRA) # restringe de uma mesma obra constar duas vezes na mesma estante
	);

-- SHA2('senha', 256) -> criptografa a senha
INSERT INTO
    USUARIO (NOME, EMAIL, SENHA)
VALUES (
        'nome',
        'email',
        SHA2('senha', 256)
    );

-- se retornou o registro há o cadastro daquela pessoa e dessa determinada senha
-- caso contrário não está cadastrado ou a senha não está correta
SELECT email, senha
FROM USUARIO
WHERE
    email = 'email'
    AND senha = SHA2('senha', 256);

# atualiza a senha do usuário
UPDATE USUARIO
SET
    senha = SHA2('novaSenha', 256)
WHERE email = 'email';
