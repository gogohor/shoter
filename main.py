from pygame import*
from button import Button

window = display.set_mode((500,500))
clock = time.Clock()

game = True
btn_start = Button(200,200,100,50,"pngwing.com.png")
btn_exit = Button(200,100,100,50,"xit.png")

run = False


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

        if i.type == KEYDOWN:
            run = False


    if run:
        window.fill((255,0,0))

    else:
        window.fill((0,0,0))
        if btn_start.draw(window):
            run = True
        if btn_exit.draw(window):
            game = False
        
    

    display.update()
    clock.tick(60)


