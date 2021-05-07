

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
        draw, quit, time, key

from pygame.locals import *

SCREENRECT = Rect(0, 0, 700, 500)



class TColor(Enum):

    ONE         = Color(204, 219, 220)
    TWO         = Color(154, 209, 212)
    THREE       = Color(128, 206, 215)
    FOUR        = Color(0, 126, 167)
    BG          = Color(0, 50, 73)
    TEAL        = Color(0, 174, 158)




blocks_filled = set()

class Block:

    
    block_size = 20

    
    def __init__(self, M: int, N: int):

        self.M      = M
        self.N      = N


    def show(self, screen: Surface)-> None:
        print(self.M, self.N)        
        blocks_filled.add((self.M, self.N))
        a = 120+(self.M*20)
        b = 120+(self.N*20)
        draw.rect(screen, 
                TColor.THREE.value, 
                Rect(a,b, 20,20)
        )
        


    def move(self, screen: Surface, direction: int)-> None:
           
        blocks_filled.remove((self.M, self.N))
        
        if direction == 2:
            self.M += 1 
        if direction == 3:
            self.N += 1
        if direction == 4:
            self.M -= 1

        self.show(screen)
            
        
    



class Grid:


    def __init__(self):
        ...


    def __call__(self, screen: Surface)-> None:
    
        block_size = 20 #Set the size of the grid block


        for x in range(120, 480, 20):
            draw.line(screen, TColor.ONE.value, (120,x), (380,x), 2)

        for y in range(120, 400, 20):
            draw.line(screen, TColor.TEAL.value, (y,120), (y,460), 2)


                

a = Block(3,3)

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
        
        events = event.get() or [event.Event(-100_000)]
        
        for e in events: 
            if e.type == QUIT:
                quit()
        
        screen.fill(TColor.BG.value)
        

        #Call the grid
        grid = Grid()
        grid(screen)

                
        a.show(screen)
       
        
        # Get User Input
        pressed_key = key.get_pressed()
        if events[0].type == KEYDOWN:
            if pressed_key[K_RIGHT]: a.move(screen, 2)
            if pressed_key[K_LEFT]:  a.move(screen, 4)
            if pressed_key[K_DOWN]:  a.move(screen, 3)



        display.flip()
        display.update()



    return 0


if __name__ == "__main__":
    
    init()
    exit(main())
