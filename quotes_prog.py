from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('back.png'), (700, 500))

clock = time.Clock()
FPS = 60

racket1 = Player("racket.png", 10, 250, 20, 80, 5)
racket2 = Player("racket.png", 670, 250, 20, 80, 5)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    window.blit(background, (0, 0))
    racket2.reset()
    racket1.reset()
    racket1.update()
    racket2.update2()

    display.update()
    clock.tick(FPS)