# The group manager script
# Created by: Zach D
# Creation date: 5/22/25

# File imports
from pygame.sprite import Group, Sprite
import pygame

# The group manager class
class GroupManagerController:
    def __init__(self, display_to_draw_on: pygame.Surface):
        self.groups = []
        self.drawing_canvas = display_to_draw_on
    
    def add_group(self, name: str, *group_sprites: Sprite):
        new_group = GameObjectGroup(name)
        for sprite in group_sprites:
            new_group.add(sprite)
        self.groups.append(new_group)
    
    def is_groups_colliding(self, group_1_name: str, group_2_name: str):
        group1 = self.find_group_by_name(group_1_name)
        group2 = self.find_group_by_name(group_2_name)
        if pygame.sprite.groupcollide(group1, group2, False, False):
            return True
        else:
            return False

    def find_group_by_name(self, group_name: str):
        for group in self.groups:
            if group.name == group_name:
                return group

    def update_groups(self):
        for group in self.groups:
            group.draw(self.drawing_canvas)
            group.update()
    
# The game object group class
class GameObjectGroup(Group):
    def __init__(self, group_name):
        super().__init__()
        self.name = group_name
