import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("My First GUI")

# Create a label widget
label = tk.Label(app, text="Hello, Tkinter!")
label.pack()  # Pack the label into the window

# Create a button widget
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(app, text="Click me!", command=on_button_click)
button.pack()  # Pack the button into the window

# Start the main event loop
app.mainloop()