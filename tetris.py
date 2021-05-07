

#TODO:
#Tetris
#create a tile object
#create tetrinomes
#create grid
#move tetrinome in grid [left, right, down]
#rotate the tetrinome   

# imports

from enum import Enum

from pygame import Rect, Surface, QUIT,\
        Color, display, mouse, init, event, \
        draw, quit


SCREENRECT = Rect(0, 0, 700, 500)



class TColor(Enum):

    ONE         = Color(204, 219, 220)
    TWO         = Color(154, 209, 212)
    THREE       = Color(128, 206, 215)
    FOUR        = Color(0, 126, 167)
    BG          = Color(0, 50, 73)
    TEAL        = Color(0, 174, 158)






class Block:

    def __init__(self, ):
        ...






class Grid:


    def __init__(self, x,y):
        
        self.x      = x
        self.y      = y



    def __call__(self, screen)-> None:
    
        block_size = 20 #Set the size of the grid block


        for x in range(120, 480, 20):
            draw.line(screen, TColor.ONE.value, (120,x), (380,x), 2)

        for y in range(120, 400, 20):
            draw.line(screen, TColor.TEAL.value, (y,120), (y,460), 2)







def main()-> int:
    
    #init screen
    
    screen = display.set_mode(SCREENRECT.size)
    display.set_caption("tetris by olamide142")
    
    mouse.set_visible(0)

    
    background = Surface(SCREENRECT.size)
    background.fill(TColor.BG.value)
    
    screen.blit(background, (0,0))
   
    
    running = True
    
    while running:
        
        for e in event.get(): 
            if e.type == QUIT:
                quit()
        
        screen.fill(TColor.BG.value)
        

        #Call the grid
        grid = Grid(5,5)
        grid(screen)

        

        display.flip()




    return 0


if __name__ == "__main__":
    
    init()
    exit(main())
