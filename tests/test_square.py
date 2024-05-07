from unittest import TestCase

from shape import Shape
from square import Square

class TestSquare(TestCase):
  def test_is_instance(self):
    square = Square(10)
    self.assertIsInstance(square, Shape)

  def test_init_raises_value_error(self):
    with self.assertRaises(ValueError):
      square = Square(-1)
