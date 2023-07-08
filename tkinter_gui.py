import tkinter as tk
from constants import *
from button_controls import *
# import generate_passwords as gen



# Determine size of grid. Will always be a box
rows, cols = [], []
for i in range(Constants.BOX):
    rows.append(i)
    cols.append(i)
size = len(cols)
left = int((size / 2) - 1)
middle = int(size / 2)
right = int((size / 2) + 1)
print(f"left ={left}, right={right}, middle={middle} ")
# create GUI
window = tk.Tk()
window.rowconfigure(rows, minsize="50", weight=1)
window.columnconfigure(cols, minsize="50", weight=1)
greeting = tk.Label(text="Welcome To the Python Password Generator")
greeting.grid(row=0, column=middle)
pnum_field_label = tk.Label(text="Amount of passwords to generate: ")
pnum_field_label.grid(row=1, column=middle)


# password number display **THIS IS CHANGED WITH +, - BUTTONS**
lbl_pnum = tk.Label(master=window, text="1")
lbl_pnum.grid(row=2, column=middle)

# decrease number of passwords
btn_num_decrease = tk.Button(master=window, text="-",
                             command=decrease_num)
btn_num_decrease.grid(row=2, column=left)

# increase number of passwords
btn_increase = tk.Button(master=window, text="+",
                         command=increase_num)
btn_increase.grid(row=2, column=right)

plength_label = tk.Label(text="Enter password length (min. 6): ")
plength_label.grid(row=3, column=middle)

# decrease password length
btn_len_decrease = tk.Button(master=window, text="-",
                             command=decrease_len)
btn_len_decrease.grid(row=4, column=left)

# password number display **THE LABEL THAT IS CHANGED BY BUTTONS**
lbl_plen = tk.Label(master=window, text="6")
lbl_plen.grid(row=4, column=middle)

# increase number of passwords
btn_increase = tk.Button(master=window, text="+",
                         command=increase_len)
btn_increase.grid(row=4, column=right)

# click to generate passwords with above parameters
generate_passwords = tk.Button(
    text="Generate",
    width=25,
    height=5,
    command=generate
)
#generate_passwords.bind("<Button-1>", gen.display_pass)
generate_passwords.grid(row=5, column=middle)

display_passwords = tk.Text()
display_passwords.grid(row=6, column=middle)

window.mainloop()
