import turtle
import tkinter as tk

def draw_tree(t, branch_length, shorten_by, angle, level, min_length=5):
    if level > 0 and branch_length > min_length:
        t.forward(branch_length)
        new_length = max(branch_length - shorten_by, min_length)  # Preventing negative branch length

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
        draw_tree(t, 100, 15, 45, level)

    # Closing the main Tkinter window after closing the turtle window
    root.destroy()

    # Close the turtle graphics window on click
    screen.exitonclick()

if __name__ == "__main__":
    main()
