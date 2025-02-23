import math
import random
import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (175, 175, 175)
        self.radius = 10
        self.velocity_x = 0
        self.velocity_y = 4
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )
        
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        
    def check_collision_with_paddle(self, paddle):
        if (self.y + self.radius >= paddle.y and
                self.y - self.radius <= paddle.y + paddle.height and
                paddle.x <= self.x <= paddle.x + paddle.width):

            relative_hit = (self.x - paddle.x) / paddle.width
            self.velocity_y = -abs(self.velocity_y)

            max_angle = 60
            angle = (relative_hit - 0.5) * max_angle

            angle_radians = math.radians(angle)
            speed = 7
            self.velocity_x = speed * math.sin(angle_radians)
            self.velocity_y = -speed * math.cos(angle_radians)
    def check_collision_with_walls(self, width):
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.velocity_x = -self.velocity_x
        if self.y - self.radius <= 0:
            self.velocity_y = -self.velocity_y
    def check_collision_with_bricks(self, bricks):
        for brick in bricks:
            if (brick.x <= self.x <= brick.x + brick.width and
                    brick.y <= self.y <= brick.y + brick.height):
                bricks.remove(brick)
                self.velocity_y = -self.velocity_y
                break
     
    def reset_ball(self):
        self.x = 640 // 2
        self.y = 480 // 2 - 30
        self.velocity_x = 0
        self.velocity_y = 4