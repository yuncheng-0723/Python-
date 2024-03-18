class Box(object):
    def __init__( self, pygame, canvas, name, rect, color):
        self.pygame = pygame    #   pygame    : pygame.
        self.canvas = canvas    #   canvas    : 畫布.
        self.name = name        #   name    : 物件名稱.
        self.rect = rect        #   rect      : 位置、大小.
        self.color = color      #   color     : 顏色.
        self.visivle = True
        
    def update(self):
        if(self.visivle):
            self.pygame.draw.rect( self.canvas, self.color, self.rect)