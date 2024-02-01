import turtle
import tkinter as tk
from tkinter import simpledialog

# Global flag to control drawing
drawing = True

def pythagorean_tree(t, branch_length, angle, level):
    """Draws a Pythagorean tree fractal using recursive function calls."""
    global drawing  # Use the global flag
    if level > 0 and drawing:
        try:
            t.forward(branch_length)
            t.left(angle)
            pythagorean_tree(t, branch_length / 1.2, angle, level - 1)
            t.right(angle * 2)
            pythagorean_tree(t, branch_length / 1.2, angle, level - 1)
            t.left(angle)
            t.backward(branch_length)
        except turtle.Terminator:
            pass

def main():
    """Sets up the turtle environment, captures user input for recursion level,
    and initiates the drawing of the Pythagorean tree fractal."""
    # Set up the turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.speed(0)
    t.color("black")

    # Position of the turtle
    t.penup()
    t.goto(0, -screen.window_height() // 3)
    t.setheading(90)
    t.pendown()

    # Capture user input for recursion level using tkinter's simpledialog
    level = simpledialog.askinteger("Input", "Enter recursion level (1-10):", minvalue=1, maxvalue=10)

    if level is not None:
        # Draw the Pythagorean tree
        pythagorean_tree(t, 100, 45, level)

    try:
        turtle.mainloop()  # Keeps the window open
    except turtle.Terminator:
        pass

if __name__ == "__main__":
    try:
        main()
    except tk.TclError:
        # Handle the Tkinter error when the window is forcibly closed
        drawing = False  # Stop the drawing
