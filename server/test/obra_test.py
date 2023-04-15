import unittest
from unittest.mock import MagicMock

from app.schemas import Obra, ObraNota, TipoObra
from app.models import Obra as ormObra
from app.controllers import ControladorObra

class TestControladorObra(unittest.TestCase):
    def setUp(self):
        """ 
        Inicializa um mock para simular uma seção com o banco
        de dados, e cria um controlador.
        """
        self.mock = MagicMock()
        self.controlador = ControladorObra(self.mock)

    def test_create(self):
        """
        Testa se a obra é criada na seção.
        """
        obra = ObraNota(id=1) 
        new_obra = self.controlador.create(obra)

        self.mock.add.assert_called_once_with(ormObra(id=1, tipo=TipoObra.filme, nota=0))

    def test_get(self):
        """
        Testa se a seção é consultada para buscar uma obra.
        """
        obra = self.controlador.get(1)

        self.mock.query.assert_called_once_with(ormObra)




        
