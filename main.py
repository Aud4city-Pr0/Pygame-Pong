# A simple pong game in python using pygame
# Created by: Zach D
# Creation date: 5/21/25

#project imports
import pygame
import os
pygame.init()

# Gameobject and scripts imports
from Assets.GameObjects.player_object import PlayerController, PlayerType
from Assets.Scripts.group_manager import GroupManagerController
from Assets.GameObjects.ball_object import Ball

# the main game class
class GameWindow:
    def __init__(self, size: tuple, background: tuple, fps: int, name: str) -> None:
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(name)
        self.bg = background
        self.FPS = fps
        self.group_manager = GroupManagerController(self.screen)
        self.player1 = PlayerController((45, 250), (240, 170, 174), 9, (70, 560), self.screen, PlayerType.PLAYER_1)
        self.player2 = PlayerController((45, 250), (138, 185, 235), 9, (1845, 560), self.screen, PlayerType.PLAYER_2)
        self.ball = Ball((50, 50), os.path.join(os.getcwd() + "/Assets/Images/", "Ball.png"), 4, (1150, 560), self.screen)
        self.group_manager.add_group("Player Group", self.player1, self.player2)
        self.group_manager.add_group("Ball Group",  self.ball)
    
    # Starts and runs the main game loop
    def run_game(self):
        running = True
        while running:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            self.screen.fill(self.bg)
            self.group_manager.update_groups()
            pygame.display.update()
        pygame.quit()



if __name__ == "__main__":
    game = GameWindow((1900, 1100), (47, 50, 56), 30, "Pygame Pong")
    game.run_game()
