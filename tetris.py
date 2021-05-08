

#TODO:
#Tetris
#create a tile object
#create tetrinomes
#create grid 
#move tetrinome in grid [left, right, down]
#rotate the tetrinome   

# imports

from enum import Enum
from typing import List
import time as T
from random import choice

from pygame import Rect, Surface, QUIT,\
        Color, sprite, display, mouse, \
        init, event, draw, quit, time, key

from pygame.locals import *

SCREENRECT  = Rect(0, 0, 700, 500)
GROUPS      = list()

COLOR_DICT = {} # "GROUP": TColor


class TColor(Enum):

    ONE         = Color(204, 219, 220)
    TWO         = Color(154, 209, 212)
    THREE       = Color(128, 206, 215)
    FOUR        = Color(0, 126, 167)
    BG          = Color(0, 50, 73)
    BLOCKS      = [Color(0, 174, 158), Color(0, 255, 0), Color(255, 0, 0), Color(0, 128, 255)]


class Block(sprite.Sprite):
    
    LAST_DROP = int(T.time())
    block_size = 20
    
    
    def __init__(self, M: int, N: int) -> None:
        
        sprite.Sprite.__init__(self)

        self.M          = M
        self.N          = N
   


    def show(self, screen: Surface, color: Color) -> None:

        a = 120+(self.M*20)
        b = 120+(self.N*20)
        draw.rect(screen, 
                color,
                Rect(a,b, 20,20)
        )
        
        
        
        #print(self.M, self.N)


    def move(self, screen: Surface, direction: int)-> str:
        #return the new index location

       
        #player can't got up in tetris
        #   pass
        #player move right
        if direction == 2:
            if self.M >=12:     self.M = 12
            else:               self.M += 1 
        #player move to the bottom
        if direction == 3:
            if self.N >=16:     self.N = 16
            else:               self.N += 1
        #player move to the left
        if direction == 4:
            if self.M <=0:      self.M = 0
            else:               self.M -= 1

        STACK_4(Block(self.M, self.N))
        return self.M, self.N


class Tetriminos(Enum):

    A = sprite.Group( Block(0,0), Block(0,1), Block(0,2), Block(0,3) )
    B = sprite.Group( Block(0,0), Block(0,1), Block(1,0), Block(1,1) )
    C = sprite.Group( Block(0,0), Block(1,0), Block(2,0), Block(2,1) )
    D = sprite.Group( Block(0,0), Block(1,0), Block(1,1), Block(2,1) )
    E = sprite.Group( Block(0,0), Block(0,1), Block(0,2), Block(1,1) )
    

    @staticmethod
    def get_random() -> List[str]:
        return choice([f"Tetriminos.{chr(i)}.value" \
                for i in range(65, 70, 1)])



the_list = []
class STACK_4(sprite.Group):

    

    def __init__(self, block: Block):

        if 'the_list' in dir():
            if len(the_list) < 5:
                the_list.append(block)
            
            else:
                GROUPS.append(sprite.Group(*the_list))            
                the_list = []
            
 




class Grid:


    def __init__(self):
        ...


    def __call__(self, screen: Surface)-> None:
    
        #Set the size of the grid block
        block_size = 20

        for x in range(120, 480, 20):
            draw.line(screen, TColor.ONE.value, (120,x), (380,x), 2)

        for y in range(120, 400, 20):
            draw.line(screen, TColor.FOUR.value, (y,120), (y,460), 2)


                

tet_1 = Tetriminos.get_random()
FGroup = sprite.Group(*eval(tet_1))
COLOR_DICT[FGroup] = choice(TColor.BLOCKS.value)
GROUPS.append(FGroup)

def main()-> int:
    
    #init screen
    
    screen = display.set_mode(SCREENRECT.size)
    display.set_caption("tetris by olamide142")
    
    mouse.set_visible(0)

        
    background = Surface(SCREENRECT.size)
    background.fill(TColor.BG.value)
    
    screen.blit(background, (0,0))
   
    
    #GAME LOOP
    running = True 
    while running:
        
        #get list of events
        events = event.get() or [event.Event(-100_000)]
        
        #if user tries to quit        
        for e in events: 
            if e.type == QUIT:
                quit()
        
        # paint screen 
        screen.fill(TColor.BG.value)
        

        #Call the grid
        grid = Grid()
        grid(screen)
        
        
        for g in GROUPS:
            for block in g:
                block.show(screen, COLOR_DICT.get(g) or Color(0,255,0))
            
        # to get every block in a tetrinome
        # dropping at the same time
        if (int(T.time()) - Block.LAST_DROP) > 0.9:
            if 16 not in [_.N for _ in GROUPS[-1]]:
                _ = [i.move(screen, 3) for i in GROUPS[-1]] 
            else:
                a = Tetriminos.get_random()
                FGroup = sprite.Group(*eval(a))
                COLOR_DICT[FGroup] = choice(TColor.BLOCKS.value)
                GROUPS.append(FGroup)

            Block.LAST_DROP = int(T.time())
               
       
        
        # Get User Input
        pressed_key = key.get_pressed()
            
        if events[0].type == KEYDOWN:
            
            if pressed_key[K_RIGHT]: 
            
                if 12 not in [_.M for _ in GROUPS[-1]]:
                    _ = [i.move(screen, 2) for i in GROUPS[-1]]
                
            if pressed_key[K_LEFT]:
                #check that other none of the member 
                #is touching a wall
                if 0 not in [_.M for _ in GROUPS[-1]]:
                    _ = [i.move(screen, 4) for i in GROUPS[-1]]
                
            if pressed_key[K_DOWN]: 
                if 16 not in [_.N for _ in GROUPS[-1]]:
                     _ = [i.move(screen, 3) for i in GROUPS[-1]]
                    
                        


        display.flip()
        display.update()



    return 0


if __name__ == "__main__":
    
    init()
    exit(main())
