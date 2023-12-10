import tkinter as tk
import random

# Makes the chart given the gender and generation
def generate_deafnessType():
    deafness_type = "Not Deaf"
    # Simulate inheritance based on Mendelian genetics

    if random.random() < 0.55:
        if random.random() < 0.85:
            deafness_type = "DFNB"
        elif 0.85 <= random.random() < 0.99:
            deafness_type = "DFNA"
        else:
            deafness_type = "DFNX"

    return deafness_type


def draw_female_info(x, y, deafnessType):
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30)
    canvas.create_text(x, y, text=f"{deafnessType}")

def draw_male_info(x, y, deafnessType):
    canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30)
    canvas.create_text(x, y, text=f"{deafnessType}")


def create_family_tree():
    generations = int(generation_var.get())
    gender = gender_var.get()
    deafness = DeafnessType_var.get()
    canvas.delete("all")  # Clear the canvas before drawing
    # Store generated deafness types for each individual
    deafness_types = []

    #initial generation
    if gender == "Female":
        draw_female_info(canvas_width // 2, vertical_spacing * 5, deafness)
        deafness_types.append(deafness)
    else:
        draw_male_info(canvas_width // 2, vertical_spacing * 5, deafness)
        deafness_types.append(deafness)
    
    # Store coordinates of the last generation's individuals
    last_generation_coords = [(canvas_width // 2, vertical_spacing * 5)]

    for i in range(1, generations + 1):
        current_generation_coords = []
        for j in range(2**i):
            deafness_type = generate_deafnessType()
            deafness_types.append(deafness_type)

            # Calculate x and y coordinates based on generation and position
            if i == 1 or j == 0:
                x = (canvas_width // (2 + i)) * (j+1)
            elif i == 2:
                x = (canvas_width // (2 + i)) + (j * 150)
            elif i == 3:
                x = (canvas_width // (2 + i)) + (j * 75)

            y = vertical_spacing * (5 - i)

            current_generation_coords.append((x, y))

            if j % 2 == 0:
                draw_female_info(x, y, deafness_type)
            else:
                draw_male_info(x, y, deafness_type)

            
            parent_x, parent_y = last_generation_coords[j // 2]  # Connect to the middle of the parents
            offspring_x, offspring_y = x, y

            # Connect from the bottom middle of the parent to the top middle of the offspring
            canvas.create_line(parent_x, parent_y - 30, offspring_x, offspring_y + 30, fill="black", arrow=tk.FIRST)

        last_generation_coords = current_generation_coords

# main code
print("Initializing project.py...\n")
root = tk.Tk()
root.title("project.py")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

canvas_width = 1000
vertical_spacing = 100

proj_title_label = tk.Label(root, text="WELCOME TO BIO PROJECT", font=("Roboto", 20, 'bold'))
proj_title_label.pack()

# Create StringVars for dropdown menus
gender_var = tk.StringVar(root)
DeafnessType_var = tk.StringVar(root)
generation_var = tk.StringVar(root)

# Set default values for dropdown menus
gender_var.set("Select Here")
DeafnessType_var.set("Select Here")
generation_var.set("Select Here")

gender_label = tk.Label(root, text="What gender?", font=("Roboto", 12, 'bold'))
gender_label.place(x=100, y=150)

gender_options = ["Male", "Female"]
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.config(width=10)
gender_menu.place(x=100, y=175)

deafness_label = tk.Label(root, text="Deafness Type?", font=("Roboto", 12, 'bold'))
deafness_label.place(x=100, y=275)

deafness_options = ["DFNB", "DFNA", "DFNX"]
deafness_menu = tk.OptionMenu(root, DeafnessType_var, *deafness_options)
deafness_menu.config(width=10)
deafness_menu.place(x=100, y=300)

generation_label = tk.Label(root, text="What generation number?", font=("Roboto", 12, 'bold'))
generation_label.place(x=100, y=400)

generation_options = ["1", "2", "3"]
generation_menu = tk.OptionMenu(root, generation_var, *generation_options)
generation_menu.config(width=10)
generation_menu.place(x=100, y=425)

gender_result_label = tk.Label(root, text="")
gender_result_label.place(x=100, y=225)

generation_result_label = tk.Label(root, text="")
generation_result_label.place(x=100, y=475)

generation_submit_button = tk.Button(root, text="Create Chart", command = create_family_tree)
generation_submit_button.place(x=150, y=500)

canvas = tk.Canvas(root, width=canvas_width, height=screen_height, highlightthickness=1, highlightbackground="black")
canvas.place(x=350, y=150)


root.mainloop()

    