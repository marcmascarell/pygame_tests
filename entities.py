#-*- coding: UTF-8 -*-
from math import sqrt
import random
import pygame
from pygame.constants import SRCALPHA
from pygame import transform

__author__ = 'franki'


class DisplayObject(object):
    def __init__(self, screen, src_surface):
        self.screen = screen
        self.src_surface = src_surface
        self.x = float(0)
        self.y = float(0)
        self.w = float(src_surface.get_width())
        self.h = float(src_surface.get_height())
        self.aspect_ratio = float(self.w) / float(self.h)
        self.surface = pygame.Surface((self.w, self.h), SRCALPHA)
        self.surface.blit(src_surface, (0, 0))

    def render(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def frame(self, cursor, left_click):
        pass

    def get_rect(self):
        return self.x, self.y, self.w, self.h

    def get_rect_int(self):
        return int(round(self.x)), int(round(self.y)), int(round(self.w)), int(round(self.h))

    def resize(self, scale):
        self.w *= scale
        self.h *= scale
        self.surface = transform.scale(self.src_surface, (int(round(self.w)), int(round(self.h))))


class Character(DisplayObject):
    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self.energy = 1
        self.speed = 5

    def kill(self):
        pass

    def hit(self, position):
        hit_x = position[0] - self.x
        hit_y = position[1] - self.y
        self.energy -= 1
        if self.energy:
            pygame.draw.circle(
                self.surface,
                (200,0,0),
                (int(round(hit_x)), int(round(hit_y))),
                 5,
                 1
            )
        else:
            self.kill()

    def frame(self, cursor, left_click):
        super(Character, self).frame(cursor, left_click)
        if left_click and cursor.colliderect(self.get_rect()):
            self.hit(cursor.center)

        cursor_x = cursor.center[0]
        cursor_y = cursor.center[1]

        d = sqrt((self.x + self.w / 2 - cursor_x) ** 2 + (self.y + self.h / 2 - cursor_y) ** 2)
        self.speed = max(.1, 10 - d / 20)

        self.x += self.speed if cursor_x < self.x + self.w / 2 else -self.speed
        self.y += self.speed if cursor_y < self.y + self.h / 2 else -self.speed

        self.x = max(0, min(self.screen.get_width() - self.w, self.x))
        self.y = max(0, min(self.screen.get_height() - self.h, self.y))


class Zombie(Character):

    def __init__(self, *args, **kwargs):
        super(Zombie, self).__init__(*args, **kwargs)
        self.x = random.randrange(450)
        self.y = random.randrange(20, 450)
        self.resize(random.uniform(.5, 1))
        self.energy = 3

    def test(self, a):
        print "pipo: " + str(a)

    def kill(self):
        super(Zombie, self).kill()
        self.__init__(self.screen, self.src_surface)




