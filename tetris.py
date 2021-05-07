

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
        display, mouse, init, event, \
        draw, quit


SCREENRECT = Rect(0, 0, 640, 480)



class TColor(Enum):

    ONE         = 204, 219, 220
    TWO         = 154, 209, 212
    THREE       = 128, 206, 215
    FOUR        = 0, 126, 167
    BG          = 0, 50, 73




class Grid:


    def __init__(self, x,y):
        
        self.x      = x
        self.y      = y



    def __call__(self, screen)-> None:
    
        block_size = 20 #Set the size of the grid block
        
        for x in range(150, SCREENRECT.size[0]+5, block_size):
        
            for y in range(5, SCREENRECT.size[1]+5, block_size):
            
                rect = Rect(x, y, block_size, block_size)
                draw.line(screen, TColor.ONE.value, (x*block_size, 10), (300,300))
            print(f"{x} ","") 
            # import sys, sys.exit

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
