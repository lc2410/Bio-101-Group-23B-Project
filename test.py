import tkinter as tk

def draw_half_filled_circle(canvas, x, y, radius, color):
    canvas.create_arc(x - radius, y - radius, x + radius, y + radius, start=0, extent=180, fill=color, outline="")

def draw_half_filled_rectangle(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, (x1 + x2) / 2, y2, fill=color, outline="")

# Create the main Tkinter window
root = tk.Tk()
root.title("Half Filled Shape")

# Create a canvas widget
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw a half-filled circle
draw_half_filled_circle(canvas, 100, 100, 50, "blue")

# Draw a half-filled rectangle
draw_half_filled_rectangle(canvas, 10, 10, 190, 190, "green")

# Start the Tkinter event loop
root.mainloop()