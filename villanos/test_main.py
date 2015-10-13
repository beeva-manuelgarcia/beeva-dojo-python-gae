from unittest import TestCase
from main import esVillano, generarVillanos2
__author__ = 'manuel'


class TestMain(TestCase):
#  def test_main(self):
#    self.fail()

  def test_generar_villanos2(self):
    s=generarVillanos2

    self.assertEqual(len(s(1)), 1)

  def test_es_villano(self):
    s=esVillano
    v1=['A', 10, 1000, 10, 1]
    self.assertEqual(s(v1), True)