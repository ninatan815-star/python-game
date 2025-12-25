# main.py
import random
import math

WIDTH = 800
HEIGHT = 600
GRAVITY = 0.5

state = "menu"
music_on = True
sound_on = True

class AnimatedSprite:
    def __init__(self, x, y, frames, speed):
        self.x = x
        self.y = y
        self.frames = frames
        self.current_frame = 0
        self.frame_delay = speed
        self.frame_counter = 0
        
    def update_animation(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def get_frame(self):
        return self.frames[self.current_frame]

class Hero(AnimatedSprite):
    def __init__(self, x, y):
        super().__init__(x, y, ["hero_idle1", "hero_idle2"], 15)
        self.walk_frames = ["hero_walk1", "hero_walk2"]
        self.vy = 0
        self.vx = 0
        self.grounded = False
        self.is_moving = False
        self.w = 40
        self.h = 50
        
    def update(self):
        self.vy += GRAVITY
        self.y += self.vy
        
        if self.y >= 500:
            self.y = 500
            self.vy = 0
            self.grounded = True
        else:
            self.grounded = False
            
        self.x += self.vx
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.w:
            self.x = WIDTH - self.w
            
        if self.is_moving:
            self.frames = self.walk_frames
        else:
            self.frames = ["hero_idle1", "hero_idle2"]
        self.update_animation()
        
    def jump(self):
        if self.grounded:
            self.vy = -12
            if sound_on:
                sounds.jump.play()

class Enemy(AnimatedSprite):
    def __init__(self, x, y, left_bound, right_bound):
        super().__init__(x, y, ["enemy_idle1", "enemy_idle2"], 20)
        self.walk_frames = ["enemy_walk1", "enemy_walk2"]
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.spd = 1.5
        self.dir = 1
        self.w = 40
        self.h = 40
        
    def update(self):
        self.x += self.spd * self.dir
        
        if self.x <= self.left_bound or self.x >= self.right_bound:
            self.dir *= -1
            
        self.frames = self.walk_frames
        self.update_animation()

player = Hero(100, 400)
baddies = [
    Enemy(300, 510, 250, 450),
    Enemy(600, 510, 550, 750)
]

btn_start = Rect(300, 200, 200, 50)
btn_music = Rect(300, 280, 200, 50)
btn_exit = Rect(300, 360, 200, 50)

def draw():
    screen.clear()
    screen.fill((135, 206, 235))
    
    if state == "menu":
        screen.draw.text("PLATFORM GAME", (250, 100), fontsize=60, color="white")
        screen.draw.filled_rect(btn_start, (100, 150, 100))
        screen.draw.text("Start Game", (330, 215), fontsize=30, color="white")
        
        txt = "Music: ON" if music_on else "Music: OFF"
        screen.draw.filled_rect(btn_music, (100, 100, 150))
        screen.draw.text(txt, (320, 295), fontsize=30, color="white")
        
        screen.draw.filled_rect(btn_exit, (150, 100, 100))
        screen.draw.text("Exit", (360, 375), fontsize=30, color="white")
    elif state == "playing":
        screen.draw.filled_rect(Rect(0, 540, WIDTH, 60), (100, 200, 100))
        screen.draw.filled_rect(Rect(player.x, player.y, player.w, player.h), (50, 150, 250))
        
        for baddie in baddies:
            screen.draw.filled_rect(Rect(baddie.x, baddie.y, baddie.w, baddie.h), (250, 50, 50))
            
        screen.draw.text("Position: " + str(int(player.x)), (10, 10), fontsize=30, color="white")
    elif state == "win":
        screen.draw.text("You Win!", (250, 250), fontsize=60, color=(50, 200, 50))
        screen.draw.text("Press SPACE to restart", (220, 350), fontsize=40, color="white")
    elif state == "lose":
        screen.draw.text("Game Over!", (250, 250), fontsize=60, color=(200, 50, 50))
        screen.draw.text("Press SPACE to restart", (220, 350), fontsize=40, color="white")

def update():
    global state
    
    if state == "playing":
        player.update()
        
        for baddie in baddies:
            baddie.update()
            
        player_box = Rect(player.x, player.y, player.w, player.h)
        for baddie in baddies:
            baddie_box = Rect(baddie.x, baddie.y, baddie.w, baddie.h)
            if player_box.colliderect(baddie_box):
                state = "lose"
                
        if player.x >= WIDTH - 100:
            state = "win"
            
        player.is_moving = False
        if keyboard.left:
            player.vx = -4
            player.is_moving = True
        elif keyboard.right:
            player.vx = 4
            player.is_moving = True
        else:
            player.vx = 0

def on_key_down(key):
    global state, player, baddies
    
    if state == "playing":
        if key == keys.SPACE or key == keys.UP:
            player.jump()
    elif state == "win" or state == "lose":
        if key == keys.SPACE:
            player = Hero(100, 400)
            baddies = [Enemy(300, 510, 250, 450), Enemy(600, 510, 550, 750)]
            state = "playing"

def on_mouse_down(pos):
    global state, music_on
    
    if state == "menu":
        if btn_start.collidepoint(pos):
            state = "playing"
            if music_on:
                music.play("background")
        elif btn_music.collidepoint(pos):
            music_on = not music_on
            if music_on:
                music.play("background")
            else:
                music.stop()
        elif btn_exit.collidepoint(pos):
            exit()

if music_on:
    music.play("background")
