import pgzrun
import random
TITLE = "Alien shooting"
WIDTH = 500
HEIGHT = 500
alien  = Actor("alien.png")
alien.pos = (WIDTH /2, HEIGHT /2)
msg = ""
def draw():
    screen.fill("Purple")
    alien.draw()
    
    screen.draw.text(msg, center = (WIDTH / 2, 10), fontsize = 30 )

def on_mouse_down(pos):
    global msg 
    if alien.collidepoint(pos):
        msg = "Good shot!"
        alien.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    else:
        msg = "Miss!"
        
    


pgzrun.go()