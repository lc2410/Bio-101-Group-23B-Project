import tkinter as tk
import functions
#import os


# Reusable button function for gender
def submit_gender():
    name = gender_entry.get()
    gender_result_label.config(text="The chosen gender is: " + name + "!")
    # Have function to change model to new gender


# Reusable button function for generation
def submit_generation():
    name = generation_entry.get()
    generation_result_label.config(text="The chosen generation is: " + name + "!")
    # Have function to change model to new generation. This could be randomly generated(maybe), 
    # and updates each time it's clicked


# Makes the chart given the gender and generation
## possibly add future prediction and/or guessing previous generation
## For now, prediction first
def make_chart(gender, generation):
    pass

def get_gender():
    name = gender_entry.get()
    return name

def get_generation():
    name = generation_entry.get()
    return name



## Main function for main_test.py
## def main():

# main code
print("Initializing project.py...\n")
root = tk.Tk()
root.title("project.py")
root.geometry("1000x700")

proj_title_label = tk.Label(root, text="WELCOME TO BIO PROJECT", font=("Roboto", 20, 'bold'))
proj_title_label.pack()

gender_label = tk.Label(root, text="What gender (M/F)", font=("Roboto", 12, 'bold'))
gender_label.place(x=125, y=150)
gender_entry = tk.Entry(root)
gender_entry.place(x=125, y=175)

gender_submit_button = tk.Button(root, text="Submit", command=submit_gender)
gender_submit_button.place(x=165, y=200)

gender_result_label = tk.Label(root, text="")
gender_result_label.place(x=125, y=225)


generation_label = tk.Label(root, text="What generation (1-4)", font=("Roboto", 12, 'bold'))
generation_label.place(x=125, y=275)
generation_entry = tk.Entry(root)
generation_entry.place(x=125, y=300)

population_size = tk.Label(root, text="What is the population size?", font=("Roboto", 12, 'bold'))
population_size.place(x=400, y=275)
population_entry = tk.Entry(root)
population_entry.place(x=450,y=300)

generation_submit_button = tk.Button(root, text="Submit", command=submit_generation)
generation_submit_button.place(x=165, y=325)

generation_result_label = tk.Label(root, text="")
generation_result_label.place(x=125, y=350)


generation_submit_button = tk.Button(root, text="Create Chart", command=make_chart)
generation_submit_button.place(x=150, y=500)



root.mainloop()

    


# if __name__ == "__main__":
# 	try:
#       os.system("clear")
# 		main()
# 	except:
# 		raise