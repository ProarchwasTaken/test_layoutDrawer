import pygame,sys

# This script is very valuable thanks to what I learned from it.
# I learned how to create infinite instances of a class and how to activate a function on every instance of said class.
# Finally I managed to learn how to draw a layout from a string and how to make it into a grid like effect.

# General Stuff
pygame.init()
clock = pygame.time.Clock()

# Screen stuff
screenWidth, screenHeight = 480, 400
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pygame Gameboard Generation")

#Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Important Variables
tile_size = 40 # Decides the size of the tiles.

tiles_list = [] # This is the variable that will allow the game to create as many tile instances as it needs to draw the layout.

layout = [
    # Layout is based on what is shown on this text drawing
    # X = White
    "XXXXXXXXXXXX",
    "X          X",
    "X XX    XX X",
    "X X      X X",
    "X    XX    X",
    "X    XX    X",
    "X X      X X",
    "X XX    XX X",
    "X          X",
    "XXXXXXXXXXXX"
]

class Tile():
    objs = [] #List that contains every instance created from the class.
    
    def __init__(self, x_pos, y_pos, width, height):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        # This adds all newly created instances to the objs list. Which would then be used later.
        Tile.objs.append(self)
        
    @classmethod
    def update(cls):
        # For each frame, every instance that's stored in objs, will draw itself on the screen.
        for obj in cls.objs:
            pygame.draw.rect(screen, white, obj)
               
# This is used to calulate where each Tile instance will be drawn. The info that will be used to calculate is from the layout.
for row_index,row in enumerate(layout):
    for col_index,col in enumerate(row):
        if col == "X":
            x = col_index * tile_size
            y = row_index * tile_size
            # This will created a new instance of Tile and assign the x and y values obtained from col and row index times tile_size. 
            tiles_list.append(Tile(x, y, tile_size - 2, tile_size - 2)) # 2 is being subtracted from tilesize to create grid like effect.

print(f"{len(tiles_list)} tiles have been created to load the layout.")

# Game loop
while True:
    for event in pygame.event.get():
        # Allows the player to quit the game.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draws stuff
    
    screen.fill(black)
    
    Tile.update() # This activates the update function on every tile instance that exists. This works thanks to the objs list.
    
    # Updates the screens
    pygame.display.flip()
    clock.tick(60)