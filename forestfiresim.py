Courtney, Chris, Tara 

 

import random, sys, time  

try:  

    import bext   

except ImportError:  

    print('This program requires the bext module, which you')   

    print('can install by following the instructions at')   

    print('https://pypi.org/project/Bext/')   

    sys.exit()  

# Set up the constants:  

WIDTH = 79  

HEIGHT = 22  

TREE = 'A'  

FIRE = '@' [=  

EMPTY = ' '   

WATER = '~'   # NEW: Water feature character  

# (!) Try changing these settings to anything between 0.0 and 1.0:  

INITIAL_TREE_DENSITY = 0.20 GROW_CHANCE = 0.01   

FIRE_CHANCE = 0.01  

PAUSE_LENGTH = 0.5  

def main(): forest = createNewForest() bext.clear()  

while True:  # Main program loop.  

displayForest(forest)  

# Run a single simulation step:  

    nextForest = {'width': forest['width'],  

                  'height': forest['height']}  

  

    for x in range(forest['width']):  

        for y in range(forest['height']):  

            if (x, y) in nextForest:  

                continue  # Already updated  

  

            if forest[(x, y)] == WATER:  # NEW: Skip water cells  

                nextForest[(x, y)] = WATER  # Lake stays unchanged  

                continue  

  

            if ((forest[(x, y)] == EMPTY)  

                and (random.random() <= GROW_CHANCE)):  

                nextForest[(x, y)] = TREE  

            elif ((forest[(x, y)] == TREE)  

                  and (random.random() <= FIRE_CHANCE)):  

                nextForest[(x, y)] = FIRE  

            elif forest[(x, y)] == FIRE:  

                for ix in range(-1, 2):  

                    for iy in range(-1, 2):  

                        neighbor = (x + ix, y + iy)  

                        if forest.get(neighbor) == TREE:  

                            nextForest[neighbor] = FIRE  

                nextForest[(x, y)] = EMPTY  

            else:  

                nextForest[(x, y)] = forest[(x, y)]  

  

    forest = nextForest  

    time.sleep(PAUSE_LENGTH)  

   

def createNewForest():  

 """Returns a dictionary for a new forest with a static lake."""   

forest = {'width': WIDTH, 'height': HEIGHT}  

# NEW: Define lake region in the center  

lake_width = 10  

lake_height = 5  

lake_x_start = (WIDTH - lake_width) // 2  

lake_y_start = (HEIGHT - lake_height) // 2  

  

for x in range(WIDTH):  

    for y in range(HEIGHT):  

        if (lake_x_start <= x < lake_x_start + lake_width and  

            lake_y_start <= y < lake_y_start + lake_height):  

            forest[(x, y)] = WATER  # NEW: Place water  

        else:  

            if (random.random() <= INITIAL_TREE_DENSITY):  

                forest[(x, y)] = TREE  

            else:  

                forest[(x, y)] = EMPTY  

return forest  

   

def displayForest(forest):  

        """Display the forest data structure on the screen."""   

         bext.goto(0, 0)   

          for y in range(forest['height']):   

                 for x in range(forest['width']):  

         if forest[(x, y)] == TREE:   

                          bext.fg('green')   

                          print(TREE, end='')  

      elif forest[(x, y)] == FIRE:  

                          bext.fg('red')   

                          print(FIRE, end='')   

       elif forest [(x, y)] == WATER:  # NEW: Display water   

                          bext.fg('blue')   

                          print(WATER, end=' ')   

       else:   

                          print(EMPTY, end=' ')   

          print()   

bext.fg('reset')   

print('Grow chance: {}% '.format(GROW_CHANCE * 100), end='')   

print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')  

 print('Press Ctrl-C to quit.')  

#If this program was run (instead of imported), run the game:  

If __name__ == '__main__':   

try:   

main()   

except KeyboardInterrupt:   

sys.exit() 
