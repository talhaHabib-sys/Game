import pygame


pygame.init()


win = pygame.display.set_mode((500,400))
speed=30
pygame.display.set_caption("Game")
WaRight=[pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R1.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R2.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R3.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R4.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R5.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R6.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R7.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R8.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\R9.png')]
WaLeft=[pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E1.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E2.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E3.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E4.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E5.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E6.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E7.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E8.png'),pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\E9.png')]
bg=pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\bg1.jpg')
bgx=0
bgx2=bg.get_width()
char=pygame.image.load('C:\\Users\\Talha Habib\\Desktop\\G\\standing.png')
clock=pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width,height):
        self.x = x
        self.y=y
        self.width=width
        self.height=height
        self.vel =10
        self.jumpCount=10
        self.isjump=True
        self.right=False
        self.left=False
        self.walkcount=0


        
    def draw(self,win):
        if self.walkcount +1 >=27:
            self.walkcount=0
        elif self.left:
            win.blit(WaLeft[self.walkcount//3],(self.x,self.y))
            self.walkcount+=1
        elif self.right:
            win.blit(WaRight[self.walkcount//3],(self.x,self.y))
            self.walkcount+=1
        else:
            win.blit(char,(self.x,self.y))


def Wind():
    win.blit(bg,(bgx,0))
    win.blit(bg,(bgx2,0))
    man.draw(win)
    pygame.display.update()
        
#main loop
man=player(150,300,64,64)
run=True
while run == True:
                    Wind()
                    clock.tick(speed)
                    bgx-=1.4
                    bgx2-=1.4
                    if bgx < bg.get_width() * -1:
                        bgx=bg.get_width()
                    if bgx2 < bg.get_width() * -1:
                        bgx2=bg.get_width()                    
                        
                    for events in pygame.event.get():
                            if events.type == pygame.QUIT:
                                run=False
                            
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_d] and man.x > man.vel:
                            man.x+=man.vel
                            man.right=True
                            man.left=False
                    elif keys[pygame.K_a] and man.x < 500-man.vel-man.width:
                            man.x-=man.vel
                            man.left=True
                            man.right=False
                    else:
                            man.left=False
                            man.right=False
                            man.walkcount=0
                    if not(man.isjump):    
                            if keys[pygame.K_UP]:
                                man.isjump=True
                    else:
                            if man.jumpCount >= -10:
                                neg=1
                                if man.jumpCount < 0:
                                    neg=-1
                                man.y-=(man.jumpCount **2) * 0.5 * neg
                                man.jumpCount-=1
                            else:
                                man.isjump=False
                                man.jumpCount=10
                        
                    
    
        
    

            
            
        


            
