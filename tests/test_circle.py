from unittest import TestCase

from shapes.shape import Shape
from shapes.circle import Circle

class TestCircle(TestCase):
  def test_is_instance(self):
    circle = Circle(10)
    self.assertIsInstance(circle, Shape)

  def test_init_raises_value_error(self):
    with self.assertRaises(ValueError):
      circle = Circle(-1)
