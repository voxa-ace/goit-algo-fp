import turtle
import tkinter as tk

def draw_tree(t, branch_length, shorten_by, angle, level):
    """
    Recursive function to draw a fractal tree with adjustable parameters.

    Args:
    t (turtle.Turtle): The turtle object used for drawing.
    branch_length (float): The length of the current branch.
    shorten_by (float): The factor by which the branch length is shortened.
    angle (float): The angle between branches.
    level (int): The current level of recursion.
    """
    if level > 0:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        draw_tree(t, new_length, shorten_by, angle, level-1)
        
        t.right(angle * 2)
        draw_tree(t, new_length, shorten_by, angle, level-1)
        
        t.left(angle)
        t.backward(branch_length)

def main():
    """
    Main function to set up the turtle environment and capture user input for recursion level.
    """
    # Set up the turtle
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.bgcolor("white")
    t.speed(0)
    t.color("black")
    t.penup()
    t.goto(0, -screen.window_height() // 4)
    t.setheading(90)  # Point the turtle upwards
    t.pendown()

    # Set up user input for recursion level
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    level = tk.simpledialog.askinteger("Input", "Enter recursion level:",
                                       minvalue=0, maxvalue=10)

    if level is not None and level > 0:
        # Draw the tree
        draw_tree(t, 100, 20, 30, level)

    # Closing the main Tkinter window after closing the turtle window
    root.destroy()

    # Close the turtle graphics window on click
    screen.exitonclick()

if __name__ == "__main__":
    main()
