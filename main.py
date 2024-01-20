import pygame as py
from random import randint

py.mixer.pre_init(44100, -16, 1, 512)  # инициализация до py.init()
py.init()



laser_sound = py.mixer.Sound("sounds/laser_gun.wav")
laser_sound.set_volume(0.05)

shot_sound = py.mixer.Sound("sounds/shot.wav")
shot_sound.set_volume(0.5)

move_sound = py.mixer.Sound("sounds/move.wav")
move_sound.set_volume(0.5)
#move_sound.fadeout(500)

WIDTH, HEIGHT = 800, 600
FPS = 60
# Screen and caption 
window = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
py.display.set_caption("Window using Pygame_menu")

font=py.font.SysFont("", 25)


class Bullet:
    def __init__(self, x, y, speed):
        self.px = x
        self.py = y
        self.speed = speed
        bullets.append(self)

    def update(self):
        global scores
        self.py -= self.speed
        if self.py < 0:
            bullets.remove(self)
        for target in targets:
            if target.rect.collidepoint(self.px,self.py):
                targets.remove(target)
                bullets.remove(self)
                scores+=1

    def draw(self):
        py.draw.circle(window, py.Color("yellow"), (self.px, self.py), 5)


class Target:
    def __init__(self):
        global scores
        self.px = randint(0, WIDTH-30)
        self.py = randint(0, 10)
        self.speed = 1+randint(0, 5)+scores/10
        self.rect = py.Rect(self.px, self.py, 30, 30)
        targets.append(self)

    def update(self):
        global scores
        self.py += self.speed
        self.rect.y = self.py
        if self.rect.top > HEIGHT:
            targets.remove(self)


    def draw(self):
        py.draw.rect(window, py.Color("Green"), self.rect)

class Sky:
    def __init__(self, x=0, y=0):
        self.px = x+randint(0, WIDTH)
        self.py = y+randint(0,HEIGHT-100)
        self.speed = 1
        self.rect = py.Rect(self.px, self.py, 10, 10)
        skys.append(self)

    def update(self):
        global mousePX
        global gunPX
        self.py += self.speed
        self.rect.y = self.py
        self.rect.x += (mousePX - gunPX) / 30
        if self.rect.top > HEIGHT:
            skys.remove(self)

    def draw(self):
        py.draw.rect(window, py.Color("Blue"), self.rect, 1)

class Star:
    def __init__(self):
        self.px = randint(0, WIDTH)
        self.py = randint(0,HEIGHT-100)
        self.speed = 0.5
        self.rect = py.Rect(self.px, self.py, 5, 5)
        stars.append(self)

    def update(self):
        global mousePX
        global gunPX
        self.py += self.speed
        self.rect.y = self.py
        self.rect.x += (mousePX - gunPX) / 50
        if self.rect.top > HEIGHT:
            stars.remove(self)

    def draw(self):
        py.draw.rect(window, py.Color("White"), self.rect, 1)

class Gun:
    def __init__(self, gunPX):
        self.px = gunPX
        self.py = HEIGHT - 30
        self.life = 3
        self.rect = py.Rect(self.px-20, self.py, 40, 20)

    def update(self):
        global mousePX
        global play
        self.px += (mousePX - self.px) / 10
        if (self.px - mousePX)/10>10:
            move_sound.play()

        for target in targets:
            if target.rect.collidepoint(gun.px, gun.py):
                targets.remove(target)
                gun.life -= 1
                shot_sound.play()
        if gun.life == 0:
            play = False

    def draw(self):
        py.draw.rect(window, py.Color("Blue"), (self.px-20, self.py, 40, 20))
        py.draw.line(window, py.Color("red"), (self.px, self.py), (self.px, self.py - 10), 20)


gunPX, gunPY = WIDTH // 2, HEIGHT - 30
gun = Gun(gunPX) # создание пушки
bullets = []
targets = []
skys = [] # Звёздное небо
stars = [] # Звейзды
bc=0 #backgroung correction


timer=60
scores=0
play = True
while play:
    for event in py.event.get():
        if event.type == py.QUIT:
            play = False




    # создание мыши
    mousePX, mousePY = py.mouse.get_pos()
    # кнопки мыши
    b1, b2, b3 = py.mouse.get_pressed()

    # плавное смещение пушки
    #gun.px += (mousePX - gun.px) / 10
    gun.update()


    if timer>0 and timer<10:
        if b1:
            b = Bullet(gun.px, gun.py, 10)
            laser_sound.play()
        #плавное смещение цели увеличение сложности
        if scores > 3:
            for target in targets:
                if target.rect.y > HEIGHT // 2 and (target.rect.x - gun.px)>30:
                    target.rect.x -= (target.rect.x - gun.px) // scores // 10
                else:
                    target.rect.x += (gun.px - target.rect.x) / 30

    if timer>0:
        timer-=1 #счётчик времени
    else:
        t = Target()
        s = Sky(50,50)
        st = Star()
        timer=randint(0,30)


    # обновление позиции
    # отработка столкновений
    for bullet in bullets: bullet.update()
    for target in targets: target.update()
    for sky in skys:sky.update()
    for star in stars: star.update()

    window.fill((bc,bc,bc))

    # отрисовка пушки
    gun.draw()
    # отрисовка звейзд
    for star in stars: star.draw()
    # отрисовка неба
    for sky in skys: sky.draw()
    # отрисовка пуль
    for bullet in bullets: bullet.draw()
    # отрисовка целей
    for target in targets: target.draw()

    # отрисовка счета
    text=font.render(f"Score: {scores}", True, py.Color("white"))
    text_life=font.render(f"Life: {gun.life}", True, py.Color("white"))
    window.blit(text, (10, 10))
    window.blit(text_life, (10, 30))
    py.display.update()
    clock.tick(FPS)
py.quit()
