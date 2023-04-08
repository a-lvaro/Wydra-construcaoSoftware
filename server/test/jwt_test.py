import unittest
from jose import jwt
from datetime import datetime, timedelta
from time import sleep

from core.security import JWTHandler
from core.security.jwt import JWTDecodeError, JWTExpiredError

class TestJWTHandler(unittest.TestCase):
    """
    Testa se os dados decodificados correspondem aos 
    dados originais
    """
    def test_encoding(self):
        payload = {"key": "value"}
        encoded = JWTHandler.encode(payload)
        decoded = JWTHandler.decode(encoded)

        for key in payload.keys():
            self.assertEqual(payload[key], decoded[key])

    """
    Testa se é levantado um erro de decodificação ao tentar 
    decodificar um token inválido
    """
    def test_decode_error(self):
        invalid_token = "i am not a valid jwt token"

        with self.assertRaises(JWTDecodeError):
            decoded = JWTHandler.decode(invalid_token)

    """
    Cria um token através do módulo jose com uma data de expiração
    no passado e testa se é levantado um erro de token expirado.
    """
    def test_expired_error(self):
        payload = {"value": "i am expired"}
        exp = datetime.utcnow() - timedelta(minutes=JWTHandler.expire_minutes)
        payload.update({"exp": exp})

        encoded = jwt.encode(
            payload, JWTHandler.secret_key, algorithm=JWTHandler.algorithm
        )

        with self.assertRaises(JWTExpiredError):
            decoded = JWTHandler.decode(encoded)