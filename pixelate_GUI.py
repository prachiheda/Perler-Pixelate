import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import * 
from PIL import ImageTk, Image
from pixelate_image import pixelate

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = 450
root.geometry(f"{screen_width}x{screen_height}")
root.title("pixelate")
upload_button = Button(root, text = "Upload Image", width = 48, command = lambda: upload_file())
upload_button.grid(row = 0, column = 8)
download_button = Button(root, text = "Download Image", width = 47, command = lambda:download_img())
download_button.grid(row = 0, column = 9)
palette_label = Label(root, text = "Select Color Palette", width = 55, bg="white")
palette_label.grid(row = 0, column = 0, columnspan = 7)
f = open("color_palette.txt", "w")
    

#create color buttons 

color_data = [
    ("Apricot", "#ffa967"), ("Black", "#000000"), ("Blueberry Cream", "#8297d9"),
    ("Blush", "#ff8285"), ("Brown", "#513931"), ("Bubblegum", "#dd669b"),
    ("Butterscotch", "#d48437"), ("Charcoal", "#3c4949"), ("Cheddar", "#f1aa0c"),
    ("Cherry", "#910a14"), ("Cobalt", "#194691"), ("Cocoa", "#403129"),
    ("Cotton Candy", "#f08bb3"), ("Cranapple", "#803245"), ("Creme", "#e0dea9"),
    ("Dark Blue", "#2b3f87"), ("Dark Green", "#1c753e"), ("Dark Grey", "#4d5156"),
    ("Dark Spruce", "#063841"), ("Denim", "#43658b"), ("Eggplant", "#522f42"),
    ("Evergreen", "#355343"), ("Fawn", "#f0cdaa"), ("Fern", "#7b9730"),
    ("Flamingo", "#ffb9b9"), ("Forest", "#214039"), ("Fruit Punch", "#dd075a"),
    ("Fuchsia", "#dc44b7"), ("Gingerbread", "#805d49"), ("Grape", "#503b82"),
    ("Green", "#4fad42"), ("Grey", "#8a8d91"), ("Honey", "#b98a33"),
    ("Hot Coral", "#ff3851"), ("Iris", "#484780"), ("Kiwi Lime", "#6cbe13"),
    ("Lagoon", "#00abb2"), ("Lavender", "#ad98d4"), ("Light Blue", "#3370c0"),
    ("Light Brown", "#815d34"), ("Light Green", "#56ba9f"), ("Light Grey", "#b1b5b2"),
    ("Light Pink", "#f6b3dd"), ("Magenta", "#f22a7b"), ("Midnight", "#323755"),
    ("Mint", "#b4debd"), ("Mist", "#9cb9c7"), ("Mulberry", "#7a3b74"),
    ("Olive", "#84873b"), ("Orange", "#ed6120"), ("Orange Cream", "#f0aa93"),
    ("Orchid", "#ef83e8"), ("Parrot Green", "#067c81"), ("Pastel Blue", "#5390d1"),
    ("Pastel Green", "#76c882"), ("Pastel Lavender", "#8a72c1"), ("Pastel Yellow", "#fef875"),
    ("Peach", "#eebab2"), ("Pearl Green", "#84b791"), ("Periwinkle Blue", "#647cbe"),
    ("Pewter", "#a0a5a5"), ("Pink", "#e44892"), ("Plum", "#a24b9c"),
    ("Prickly Pear", "#b6ff51"), ("Purple", "#604089"), ("Raspberry", "#a53061"),
    ("Red", "#bf2e40"), ("Robin's Egg", "#afe1e6"), ("Rose", "#a85869"),
    ("Rust", "#8c372c"), ("Sage", "#98b196"), ("Salmon", "#ff7d64"),
    ("Sand", "#e4b690"), ("Shamrock", "#007341"), ("Sherbert", "#e1ee7d"),
    ("Sky", "#54cde3"), ("Slate Blue", "#5a7180"), ("Slime", "#bfb629"),
    ("Sour Apple", "#b0d169"), ("Spice", "#e35c44"), ("Stone", "#9c8d8e"),
    ("Tan", "#bc9371"), ("Tangerine", "#d6642d"), ("Teal", "#20c5f7"),
    ("Thistle", "#8e8da5"), ("Toasted Marshmallow", "#ebe1cd"), ("Tomato", "#ea4242"),
    ("Toothpaste", "#93c8d4"), ("Turquoise", "#2b89c6"), ("White", "#f8f8f8"),
    ("Yellow", "#ecd800")
]

All = Button(root, text = "All Colors", width = 28)
All.config(command = lambda:color_clicked(All, "all"))
All.grid(row = 14, column = 0, columnspan = 7)
color_buttons = []
for index, (color_name, bg_color) in enumerate(color_data):
    button = tk.Button(root, text=color_name, bg=bg_color, width=4)
    button.config(command=lambda b=button, c=color_name: color_clicked(b, c))
    button.grid(row=index // 7 + 1, column=index % 7)
    color_buttons.append(button)


def color_clicked(button, color_name):
    if button == All:
        with open("color_palette.txt", "w") as file_object:
            file_object.write("all")
        for color_button in color_buttons:
            if color_button != All:
                color_button.config(state="disabled")

    with open("color_palette.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data)>0:
            file_object.write("\n")
        file_object.write(color_name)
    button.config(relief=SUNKEN)
    button.config(state = "disabled")



def pixelate_img():
    global pixelated_label
    pixelated_img = pixelate(filename, int(Height_entry.get()), int(Width_entry.get()), "color_palette.txt", dithering = True)
    pixelated_img = ImageTk.PhotoImage(image = pixelated_img)
    pixelated_label = Label(root)
    pixelated_label.grid(row=1, column=9, rowspan = 19)
    pixelated_label.image = pixelated_img
    pixelated_label['image']= pixelated_img


def upload_file():
    f_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    global filename
    filename = tk.filedialog.askopenfilename(filetypes = f_types)
    img = Image.open(filename)
    # Set the maximum width and height for the scaled image.
    max_width = 400
    max_height = 400

    # Get the original dimensions of the image.
    original_width, original_height = img.size

    # Calculate the scaling factor based on the maximum width and height.
    width_scale = max_width / original_width
    height_scale = max_height / original_height

    # Use the smaller scaling factor to preserve the aspect ratio.
    scale = min(width_scale, height_scale)

    # Calculate the new width and height after scaling.
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    # Resize the image using the calculated new dimensions.
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image = img)
    image_label = Label(root)
    image_label.grid(row = 1, column = 8, rowspan = 19)
    image_label.image = img 
    image_label['image']= img 

    Height_label = Label(root, text = "Pixel Height")
    Height_label.grid(row = 20, column = 8)
    global Height_entry
    Height_entry = Entry(root)
    Height_entry.grid(row=21, column = 8)

    Width_label = Label(root, text = "Pixel Width")
    Width_label.grid(row = 22, column = 8)
    global Width_entry
    Width_entry = Entry(root)
    Width_entry.grid(row = 23, column = 8)

    pixelate_button = Button(root, text = "Pixelate!", width = 30, command = lambda:pixelate_img())
    pixelate_button.grid(row = 24, column = 8)

def download_img():
    f_types = [("Jpg Files", "*.jpg"), ("PNG Files", "*.png")]
    filename = asksaveasfilename(defaultextension=".png", filetypes=f_types)
    pixelated_img = pixelated_label.image
    pixelated_img.write(filename)


root.mainloop()