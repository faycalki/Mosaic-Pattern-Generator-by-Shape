import turtle, random
#drawing_pointer.color("green") # Color of pointer    
#drawing_pointer.pendown # starts drawing
#drawing_pointer.penup # stops drawing
#drawing_pointer.forward(x) this is the same as drawing_pointer.fd(x)
#drawing_pointer.rt(x) this is the same as drawing_pointer.right(x)
#drawing_pointer.lt(x) this is the same as drawing_pointer.left(x)
#drawing_pointer.bk() this is the same as drawing_pointer.back(x). <-- we won't use this one.
#drawing_pointer.goto(x, y) <-- this we will use a lot! This draws up to that coordinate, from the current coordinate.
#We can also draw filled in circles using drawing_pointer.dot(d), where d is the diameter. But this isn't relevant to the assignment for filled in circles.
#You can change the drawing pointer size with drawing_pointer.shapesize(stretch length, stretch width, Outline width) -- best to set it all to 0 as we don't care about the pointer.
show_screen = turtle.getscreen() # This is sufficienet as a variable, because getscreen() already makes it clear what it does.
drawing_pointer = turtle.Turtle() # This is sufficient as a variable, because of how we defined it.
num_iterations = 20
length_shape_1_side = 27
length_shape_2_side = 27
length_shape_3_side = 27
length_shape_4_side = 27
num_of_sides_shape_1 = 3 # Equilateral Triangle
num_of_sides_shape_2 = 4 # Square
num_of_sides_shape_3 = 5 # Regular Pentagon
num_of_sides_shape_4 = 8 # Regular Octagon
global num_of_sides_shape
global length_shape_side
num_of_sides_shape = 0
length_shape_side = 0
starting_x_coordinate = -length_shape_1_side * 7
#print(starting_x_coordinate)
x = starting_x_coordinate
y = 0
show_screen.colormode(255) # Necessary in order to be able to use hex code coloring
def color_change(): # Simple color change function, we will invoke it using function_name(), as there are no parameters to pass into it anyway.
    R = random.randint(0, 255) # Inclusive endpoint for randint
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    drawing_pointer.pencolor(R,G,B) # Coloring for the pointer
drawing_pointer.goto(starting_x_coordinate, y)
drawing_pointer.shapesize(0.00001, 0.00001, 0.00001) # I don't really care about the drawing pointer, so I tried to set it as small as possible.
drawing_pointer.pensize(2) # Thickness of pen
drawing_pointer.speed(0) # 10 speed is max, 0 will skip animations and instantly draw. But I assume you, in the assignment, want to see it in action as it draws.
drawing_pointer.clear() # Clears screen from leftovers
drawing_pointer.setheading(0) # Setting anglee to 0, as described in the algorithm (that is, we are facing eastwards from the origin for the drawing initially)



#### THE ISSUE SEEMS TO BE THE IF LOOPS SEEM TO TERMINATE THE CANVAS EVERY TIME THEY LOOP (?) I'm not sure.
def draw_impl(length_shape_side, num_of_sides_shape):
    #print("Length of shape sides:", length_shape_side)
    #print("number of sides of shape:", num_of_sides_shape)
    drawing_pointer.forward(length_shape_side)
    drawing_pointer.left(360 / num_of_sides_shape)
    #drawing_pointer.forward(10)
    #drawing_pointer.left(36)

for count_up_1 in range(0, 3): # For the y offset drawing, #Note, exclusive end, inclusive start.
    for count_up_2 in range(0, 6): # For the x offset drawing, # Just a question: are those variables local or global? Is it fine if I use counter for all three of those repeat loops? Will it mess with it? What if I assign a variable and also call it counter, with those having counter too?
        for count_up_3 in range(0, num_iterations):
            counter = 1
            for count_up_4 in range(0, 4):
                if counter == 1:
                    length_shape_side = length_shape_1_side
                    num_of_sides_shape = num_of_sides_shape_1
                elif counter == 2:
                    length_shape_side = length_shape_2_side
                    num_of_sides_shape = num_of_sides_shape_2
                elif counter == 3:
                    length_shape_side = length_shape_3_side
                    num_of_sides_shape = num_of_sides_shape_3
                elif counter == 4:
                    length_shape_side = length_shape_4_side
                    num_of_sides_shape = num_of_sides_shape_4
                drawing_pointer.pendown()
                #print(num_of_sides_shape)
                for count_up_4 in range(0, num_of_sides_shape):
                    draw_impl(length_shape_side, num_of_sides_shape)
                drawing_pointer.lt(360 / num_of_sides_shape)
                counter += 1
        drawing_pointer.penup()
        drawing_pointer.setheading(0)
        color_change() # Invokation for color change
        x += length_shape_1_side * 3.5
        drawing_pointer.goto(x, y)
    drawing_pointer.penup()
    color_change()
    x = starting_x_coordinate
    y += length_shape_1_side * 3.5
    drawing_pointer.goto(x, y)

turtle.done() # To prevent the program from closing when done drawing
