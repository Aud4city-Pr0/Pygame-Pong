# The ball script
# Created by: Zach D
# Creation Date: 6/6/25

# File imports
import pygame
from pygame.sprite import Sprite

# The main ball class
class Ball(Sprite):
	def __init__(self, size: tuple, image_path: str, move_speed: int, position: tuple, game_screen: pygame.Surface):
		# Basic setup
		super().__init__()
		# TODO: replace this with asset loader script later on
		self.image = pygame.transform.scale(pygame.image.load(image_path), (size))
		self.rect = self.image.get_rect()
		self.rect.centerx = position[0]
		self.rect.centery = position[1]
		self.game_area = game_screen.get_rect()
	
	def update(self):
		pass
