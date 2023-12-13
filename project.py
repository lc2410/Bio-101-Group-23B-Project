import tkinter as tk
import random


#generate deafness
def generate_deafnessType(offSpringdeafnessType="", parent1DeafnessType="", parent2DeafnessType=""):
    if(offSpringdeafnessType == ""):
        if(parent1DeafnessType == "Not Deaf" and parent2DeafnessType == "Not Deaf"):
            return "Not Deaf"
        elif (parent1DeafnessType == "Not Deaf" and parent2DeafnessType == "DFNB Carrier") or (parent1DeafnessType == "DFNB Carrier" and parent2DeafnessType == "Not Deaf"):
            rand = random.randint(0,1)
            if rand == 0:
                return "Not Deaf"
            else:
                return "DFNB Carrier"
        elif (parent1DeafnessType == "DFNB Carrier" and parent2DeafnessType == "DFNB Carrier"):
            rand = random.randint(0,3)
            if rand == 0:
                return "Not Deaf"
            elif rand == 1:
                return "DFNB"
            else:
                return "DFNB Carrier"
        elif (parent1DeafnessType == "DFNB" and parent2DeafnessType == "DFNB"):
            return "DFNB"
        elif (parent1DeafnessType == "DFNB" and parent2DeafnessType == "DFNB Carrier") or (parent1DeafnessType == "DFNB Carrier" and parent2DeafnessType == "DFNB"):
            print("true")
            rand = random.randint(0,1)
            if rand == 0:
                return "DFNB"
            else:
                return "DFNB Carrier"
        elif parent1DeafnessType == "DFNB" and parent2DeafnessType == "Not Deaf":
            return "DFNB Carrier"
        
        else:
            rand = random.randint(0, 100)
            if rand < populationPercentage.get(): # Population percentage
                return "DFNB"
            else:
                rand = random.randint(0, 100)
                if rand < carrierPercentage.get(): # Carrier population percentage rounded down (main)
                    return "DFNB Carrier"
                else:
                    return "Not Deaf"
    elif(offSpringdeafnessType == "Not Deaf"):
        rand = random.randint(0,2)
        if rand == 0:
            return "DFNB Carrier"
        else:
            return "Not Deaf"
    else:
        print(offSpringdeafnessType)
        return "DFNB"

    



def draw_female_info(x, y, deafnessType):
    canvas.create_oval(x - 30, y - 30, x + 30, y + 30)
    canvas.create_text(x, y, text=f"{deafnessType}")

def draw_male_info(x, y, deafnessType):
    canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30)
    canvas.create_text(x, y, text=f"{deafnessType}")


def create_family_tree():    
    canvas.delete("all")  # Clear the canvas before drawing
    generations = int(generation_var.get())
    parent1PhenoType = parent_1_choice.get()
    parent2PhenoType = parent_2_choice.get()

    # Store generated deafness types for each individual
    deafness_types = []
    genders = []

    #gen 0
    parent1GenoType = generate_deafnessType(offSpringdeafnessType=parent1PhenoType)
    parent2GenoType = generate_deafnessType(offSpringdeafnessType=parent2PhenoType)


    #initial generation
    draw_female_info(canvas_width // 5, 200, parent1GenoType)
    draw_male_info(canvas_width // 5 + 300, 200, parent2GenoType)

    deafness_types.append(parent1GenoType)
    deafness_types.append(parent2GenoType)
    genders.append("Female")
    genders.append("Male")
    
    
    # Store coordinates of the last generation's individuals
    last_generation_coords = [(canvas_width // 5, 200), (canvas_width // 5 + 300, 200)]

    for i in range(1, generations+1):
        rand = random.randint(0,1)
        x1 = canvas_width // (5-i)
        y1 = 200 + (i * vertical_spacing)

        x2 = canvas_width // (5-i) + 300
        y2 = 200 + (i * vertical_spacing)
        if rand == 0:
            offspringGenes = generate_deafnessType(parent1DeafnessType=deafness_types[len(deafness_types) - 2], parent2DeafnessType=deafness_types[len(deafness_types) - 1])
            print(deafness_types)
            draw_male_info(x1, y1, offspringGenes)
            genders.append("Male")
            deafness_types.append(offspringGenes)
        
            if(i != generations):
                partnerGenes = generate_deafnessType()
                draw_female_info(x2, y2, partnerGenes)
                genders.append("Female")
                deafness_types.append(partnerGenes)
            
        else:
            offspringGenes = generate_deafnessType(parent1DeafnessType=deafness_types[len(deafness_types) - 2], parent2DeafnessType=deafness_types[len(deafness_types) - 1])
            draw_female_info(x1, y1, offspringGenes)
            genders.append("Female")
            deafness_types.append(offspringGenes)

            if(i != generations):
                partnerGenes = generate_deafnessType()
                draw_male_info(x2, y2, partnerGenes)
                genders.append("Male")
                deafness_types.append(partnerGenes)

        parent1x, parent1y = last_generation_coords[0]
        parent2x, parent2y = last_generation_coords[1]

        canvas.create_line(parent1x, parent1y+30, x1, y1-30, fill="black", arrow=tk.LAST)
        canvas.create_line(parent2x, parent2y+30, x1, y1-30, fill="black", arrow=tk.LAST)

        last_generation_coords = [(x1, y1), (x2, y2)]


# main code
print("Initializing project.py...\n")
root = tk.Tk()
root.title("project.py")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#global variables as tk updates
populationPercentage = tk.IntVar()
populationPercentage.set(13)
carrierPercentage = tk.IntVar()
carrierPercentage.set(3 * int(populationPercentage.get() / 5)) # Rounds down


#Window Size 
root.geometry(f"{screen_width}x{screen_height}")

canvas_width = 1000
vertical_spacing = 100

proj_title_label = tk.Label(root, text="WELCOME TO BIO PROJECT", font=("Roboto", 20, 'bold'))
proj_title_label.pack()

# Create StringVars for dropdown menus
parent_1_choice = tk.StringVar(root)
parent_2_choice = tk.StringVar(root)
generation_var = tk.StringVar(root)

# Set default values for dropdown menus
parent_1_choice.set("Select Here")
parent_2_choice.set("Select Here")
generation_var.set("Select Here")

gender_label = tk.Label(root, text="Parent 1 (female) phenotype?", font=("Roboto", 12, 'bold'))
gender_label.place(x=100, y=150)

deafness_options = ["Not Deaf", "Deaf"]
gender_menu = tk.OptionMenu(root, parent_1_choice, *deafness_options)
gender_menu.config(width=10)
gender_menu.place(x=100, y=175)

deafness_label = tk.Label(root, text="Parent 2 (male) phenotype?", font=("Roboto", 12, 'bold'))
deafness_label.place(x=100, y=275)

deafness_menu = tk.OptionMenu(root, parent_2_choice, *deafness_options)
deafness_menu.config(width=10)
deafness_menu.place(x=100, y=300)

generation_label = tk.Label(root, text="# of Generations?", font=("Roboto", 12, 'bold'))
generation_label.place(x=100, y=400)

generation_options = ["1", "2", "3"]
generation_menu = tk.OptionMenu(root, generation_var, *generation_options)
generation_menu.config(width=10)
generation_menu.place(x=100, y=425)

deafPercentage_label = tk.Label(root, text="Deaf Population Percentage?", font=("Roboto", 12, 'bold'))
deafPercentage_label.place(x=100, y=525)


#update carrier label
#arg is the populationPercentage variable that was sent in deafPercentage_scale
def updateCarrier(arg):
    carrierPercentage.set(int(3 * (populationPercentage.get() / 5))) # Rounds down
    deafCarrier_label2 = tk.Label(root, textvariable=carrierPercentage, font=("Roboto", 8))
    deafCarrier_label2.place(x=275, y=625)


deafPercentage_scale = tk.Scale(root, from_=5, to=20, orient="horizontal", variable=populationPercentage, command=updateCarrier)
deafPercentage_scale.place(x=100, y=550)

deafPercentage_label2 = tk.Label(root, text=f"Deaf Population Percentage:\t        %", font=("Roboto", 8))
deafPercentage_label2.place(x=100, y=600)
deafPercentage_label3 = tk.Label(root, textvariable=populationPercentage, font=("Roboto", 8))
deafPercentage_label3.place(x=275, y=600)

deafCarrier_label = tk.Label(root, text=f"Deaf Carrier Percentage:\t        %", font=("Roboto", 8))
deafCarrier_label.place(x=100, y=625)

deafCarrier_label2 = tk.Label(root, textvariable=carrierPercentage, font=("Roboto", 8))
deafCarrier_label2.place(x=275, y=625)

generation_submit_button = tk.Button(root, text="Create Chart", command = create_family_tree)
generation_submit_button.place(x=150, y=675)

#Chart sizes
canvas = tk.Canvas(root, width=canvas_width, height=screen_height, highlightthickness=1, highlightbackground="black")  
canvas.place(x=375, y=150)


root.mainloop()

    