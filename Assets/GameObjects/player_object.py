# The player object class and code
# Created by: Zach D
# Creation date: 5/21/25

# File imports
import pygame
from pygame.sprite import Sprite
from enum import Enum

# The player type enum
class PlayerType(Enum):
    PLAYER_1 = 0,
    PLAYER_2 = 1

# The player class
class PlayerController(Sprite):
    def __init__(self, size: tuple, color: tuple, move_speed: int, position: tuple, game_screen: pygame.Surface, player_type: PlayerType) -> None:
        # Basic setup
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = move_speed
        self.rect.centerx = position[0]
        self.rect.centery = position[1]
        self.game_area = game_screen.get_rect()
        self.player_value = player_type
    
    def update(self):
        # Moving the player
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.player_value == PlayerType.PLAYER_2 or pressed_keys[pygame.K_w] and self.player_value == PlayerType.PLAYER_1:
            self.rect.move_ip(0, -self.speed)
        elif pressed_keys[pygame.K_DOWN] and self.player_value == PlayerType.PLAYER_2 or pressed_keys[pygame.K_s] and self.player_value == PlayerType.PLAYER_1:
            self.rect.move_ip(0, self.speed)
        
        self.rect.clamp_ip(self.game_area)
