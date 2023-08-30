import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Cessna 172 W&B Calculator")


# Function to actually calculate
def calculate():
    try:
        BEW = float(entry_bew.get())
        moment = float(entry_moment.get())
        FP = float(entry_fp.get())
        RP = float(entry_rp.get())
        Bag = float(entry_bag.get())
        fuel = float(entry_fuel.get())

        fuel_weight = 6 * fuel
        FP_moment = 37 * FP
        RP_moment = 73 * RP
        Bag_moment = 95 * Bag
        fuel_weight_moment = 47.8 * fuel_weight

        total_weight = BEW + FP + RP + Bag + fuel_weight
        total_moment = moment + FP_moment + RP_moment + Bag_moment + fuel_weight_moment
        cg = total_moment / total_weight
        result_text = "Total weight: {}\nTotal Moment: {} lb-in\nCG: {} inches".format(
            total_weight, total_moment, cg
        )
        result_label.config(text=result_text, font=("Times", 15))
        error_label.config(text="")
    except ValueError as e:
        error_message = "Error calculating, please review that you input valid numbers and left no blank spaces."
        error_label.config(text=error_message)


# image
image = Image.open("logo.png")
image = image.resize((600, 300))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.image = photo
image_label.grid(columnspan=3, row=0, column=0)

# rows and columnspace
canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=15)

# User input values and placement
label_bew = tk.Label(root, text="Basic empty weight:", font="Times")
entry_bew = tk.Entry(root)
label_bew.grid(row=1, column=0, sticky="e")
entry_bew.grid(row=1, column=1)

label_moment = tk.Label(root, text="Moment:", font="Times")
entry_moment = tk.Entry(root)
label_moment.grid(row=2, column=0, sticky="e")
entry_moment.grid(row=2, column=1)

label_fp = tk.Label(root, text="Sum of front passengers:", font="Times")
entry_fp = tk.Entry(root)
label_fp.grid(row=3, column=0, sticky="e")
entry_fp.grid(row=3, column=1)

label_rp = tk.Label(root, text="Sum of rear passengers:", font="Times")
entry_rp = tk.Entry(root)
label_rp.grid(row=4, column=0, sticky="e")
entry_rp.grid(row=4, column=1)

label_bag = tk.Label(root, text="Baggage area:", font="Times")
entry_bag = tk.Entry(root)
label_bag.grid(row=5, column=0, sticky="e")
entry_bag.grid(row=5, column=1)

label_fuel = tk.Label(root, text="Fuel amount (gallons):", font="Times")
entry_fuel = tk.Entry(root)
label_fuel.grid(row=6, column=0, sticky="e")
entry_fuel.grid(row=6, column=1)

calculate_button = tk.Button(
    root,
    text="Calculate",
    command=calculate,
    font=("Times", 15),
    fg="#D4AF37",
    bg="#D4AF37",
    highlightbackground="#D4AF37",
    height=2,
    width=15,
)
calculate_button.grid(columnspan=3, row=8, column=0)

result_label = tk.Label(root, text="Results will be displayed here.", font="Times")
result_label.grid(columnspan=3, row=9, column=0)

error_label = tk.Label(root, text="", fg="red", font=("Times", 12))
error_label.grid(columnspan=3, row=7, column=0)


root.mainloop()
