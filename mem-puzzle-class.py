"""memory puzzle - gui version using classes
    simple implementation of classic game memoty tile puzzle
    for animation and graphics i use turtle module 
"""
import turtle, random, time

#-- constants 
tile = 100
width = 500
height = 500

#-- screen setup 
screen = turtle.Screen()
screen.setup(width, height, 700)
screen.bgcolor("black")
screen.tracer(1)

#-- class Game holding  graphic attribs and game attribs 
class Game(turtle.Turtle):
    def __init__(self):
        #-- module attributes
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(4.8)
        self.setpos(-200,200)
        self.speed(4)
        #-- game attributes
        self.items = list("aabbccddeeffgghhssoo")
        random.shuffle(self.items)
        self.items = [self.items[:4], self.items[4:8],\
                          self.items[8:12], self.items[12:16],\
                          self.items[16:]]
        self.grid = [] #-- to find the position of each tile 
        self.temp_selected = []
        self.temp_coordinates = []
        self.count = 0
        self.correct = 0 
    #-- a simple 2D array using for backend board 
    def print_items(self):
        for r in range(len(self.items)):
            time.sleep(0.10)
            for c in range(len(self.items[0])):
                print(self.items[r][c], end ="")
            print()
    #-- depending on tile position in 2D array, finds the items color
    def get_color(self, r,c):
        if self.items[r][c] == "a":
            self.fillcolor("white")
        elif self.items[r][c] == "b":
            self.fillcolor("blue")
        elif self.items[r][c] == "c":
            self.fillcolor("orange")
        elif self.items[r][c] == "d":
            self.fillcolor("red")
        elif self.items[r][c] == "e":
            self.fillcolor("green")
        elif self.items[r][c] == "f":
            self.fillcolor("yellow")
        elif self.items[r][c] == "g":
            self.fillcolor("light green")
        elif self.items[r][c] == "h":
            self.fillcolor("pink")
        elif self.items[r][c] == "s":
            self.fillcolor("lightblue")
        elif self.items[r][c] == "o":
            self.fillcolor("gold")
    #-- acording to the position of items in 2D array draws the graphical board
    def draw_colors(self):
        for r in range(len(self.items)):
            for c in range(len(self.items[0])):
                self.get_color(r,c)
                self.stamp()
                int(self.xcor())
                int(self.ycor())
                self.grid.append((self.xcor(), self.ycor()))#-- keep a track of position of each tile
                self.forward(tile)
            self.back(tile * 4)
            self.right(90)
            self.forward(tile)
            self.left(90)
    #-- covers the tiles by stamping the gray color on them 
    def draw_cover(self):
        self.fillcolor("gray")
        self.setpos(-200, 200)
        for r in range(len(self.items)):
            for c in range(len(self.items[0])):
                self.stamp()
                self.forward(tile)
            self.back(tile*4)
            self.right(90)
            self.forward(tile)
            self.left(90)
        self.reset_first_click()
    #-- acording to grid list we can locate the exact position of each tile
    def get_coordinate(self, r,c):
        if (r,c) == (0,0):
            return self.grid[0]
        elif (r,c) == (0,1):
            return self.grid[1]
        elif (r,c) == (0,2):
            return self.grid[2]
        elif (r,c) == (0,3):
            return self.grid[3]
        elif (r,c) == (1,0):
            return self.grid[4]
        elif (r,c) == (1,1):
            return self.grid[5]
        elif (r,c) == (1,2):
            return self.grid[6]
        elif (r,c) == (1,3):
            return self.grid[7]
        elif (r,c) == (2,0):
            return self.grid[8]
        elif (r,c) == (2,1):
            return self.grid[9]
        elif (r,c) == (2,2):
            return self.grid[10]
        elif (r,c) == (2,3):
            return self.grid[11]
        elif (r,c) == (3,0):
            return self.grid[12]
        elif (r,c) == (3,1):
            return self.grid[13]
        elif (r,c) == (3,2):
            return self.grid[14]
        elif (r,c) == (3,3):
            return self.grid[15]
        elif (r,c) == (4,0):
            return self.grid[16]
        elif (r,c) == (4,1):
            return self.grid[17]
        elif (r,c) == (4,2):
            return self.grid[18]
        elif (r,c) == (4,3):
            return self.grid[19]
    #-- metod to select the first tile
    #-- keeps  a track of temporary coordinates, and selected item
    def first(self, x,y):
        self.temp_coordinates.clear()
        self.temp_selected.clear()
        #-- converting cartesian board to screen (row, column)
        c = int(x+(width/2)) // tile
        r = int(-y +(height/2)) //tile
        self.get_color(r,c)
        self.goto(self.get_coordinate(r,c))
        self.stamp()
        self.temp_selected.append(self.items[r][c])
        self.temp_coordinates.append(self.pos())
        self.reset_second_click()
    #-- metod to select the second tile
    #-- keeps  a track of temporary coordinates, and selected item
    def second(self, x,y):
        c = int(x+(width/2)) // tile
        r = int(-y +(height/2)) //tile
        self.get_color(r,c)
        self.goto(self.get_coordinate(r,c))
        if self.pos() == self.temp_coordinates[0]:
            print("this is the first color, choose second color!")
        else:
            self.stamp()
            self.temp_selected.append(self.items[r][c])
            self.temp_coordinates.append(self.pos())
            self.check()
    #-- checks if two selected tiles are match and reset the temporary trackers    
    def check(self):
        if self.temp_selected[0] == self.temp_selected[1]:
            print("correct")
            self.correct += 1
            if self.correct == 10:               
                print("You solve the puzzle with: ", self.correct + self.count, "moves.")
            self.reset_first_click()
        else:
            self.count +=1
            self.fillcolor("gray")
            for coordinate in self.temp_coordinates:
                self.goto(coordinate)
                self.stamp()
                self.reset_first_click()
        
    #-- reseting the mouse event for first and second selection 
    def reset_first_click(self):
        turtle.onscreenclick(self.first)    
    def reset_second_click(self):
        turtle.onscreenclick(self.second)

#-- main function 
def main():
    #-- creating class object and calling some methods 
    game = Game()
    game.print_items()
    game.draw_colors()
    game.draw_cover()
    turtle.mainloop() #-- creates the main loop for turtle screen 
if __name__ == "__main__":
    main()
