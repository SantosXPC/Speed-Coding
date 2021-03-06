import pygame as py
 
class Maceta(object):
	"""Objeto decorativo dentro del juego.
		Parámetros:
			_bounds -- Posición donde se dibujará la maceta."""
	def __init__(self, _bounds):
		self.bounds = py.Rect(_bounds)
		self.img = py.image.load("resources/graphics/sprites/espinaca/espinaca.png").convert_alpha()
		self.img = py.transform.scale(self.img, (2 * self.img.get_width(), 2 * self.img.get_height()))

		self.bounds.width, self.bounds.height = self.img.get_width(), self.img.get_height()
		self.bounds.y -= self.bounds.height

	def render(self, _screen):
		"""Dibuja la imagen de la maceta en la pantalla.
			Parámetros:
				_screen -- Pantalla donde se dibujará la maceta"""
		_screen.blit(self.img, self.bounds)