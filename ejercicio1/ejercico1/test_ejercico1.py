from unittest import TestCase
import unittest
from ejercico1 import ejercicio1


__author__ = 'manuel'


class TestEjercico1(TestCase):
  def test_negative_discr(self):

      s = ejercicio1

      self.assertEqual(s.ejercico(10,0), [7,0])


