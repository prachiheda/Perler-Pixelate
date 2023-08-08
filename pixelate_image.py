import argparse
from PIL import Image, ImageDraw
import os
import numpy as np
from scipy.spatial import cKDTree
from collections import Counter

def compress_image(image):

    # Get the original size
    width, height = image.size

    # Calculate the aspect ratio
    aspect_ratio = width / height

    # Set the maximum size to 200 pixels (keeping the aspect ratio)
    max_size = 400

    # Calculate the new dimensions while preserving aspect ratio
    if width > height:
        new_width = max_size
        new_height = int(max_size / aspect_ratio)
    else:
        new_height = max_size
        new_width = int(max_size * aspect_ratio)

    # Resize the image while preserving aspect ratio
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    return resized_image


def get_closest_color(color, color_palette):
    # Create a numpy array from the color palette
    color_array = np.array(color_palette)

    # Create a KD-tree from the color palette
    tree = cKDTree(color_array)

    # Find the index of the color in the palette with the smallest distance
    closest_index = tree.query(color)[1]

    # Return the closest color from the palette
    return color_palette[closest_index]


def distance(color1, color2):
    # Calculate the Euclidean distance between two RGB colors
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5

color_palette = [
    ("Apricot", (255, 169, 103)),
    ("Black", (46, 47, 50)),
    ("Blueberry Cream", (130, 151, 217)),
    ("Blush", (255, 130, 133)),
    ("Brown", (81, 57, 49)),
    ("Bubblegum", (221, 102, 155)),
    ("Butterscotch", (212, 132, 55)),
    ("Charcoal", (60, 73, 73)),
    ("Cheddar", (241, 170, 12)),
    ("Cherry", (145, 10, 20)),
    ("Cobalt", (25, 70, 145)),
    ("Cocoa", (64, 49, 41)),
    ("Cotton Candy", (240, 139, 179)),
    ("Cranapple", (128, 50, 69)),
    ("Creme", (224, 222, 169)),
    ("Dark Blue", (43, 63, 135)),
    ("Dark Green", (77, 81, 86)),
    ("Dark Grey", (67, 101, 139)),
    ("Dark Spruce", (6, 56, 65)),
    ("Denim", (67, 83, 139)),
    ("Eggplant", (82, 47, 66)),
    ("Evergreen", (53, 83, 67)),
    ("Fawn", (240, 205, 170)),
    ("Fern", (123, 151, 48)),
    ("Flamingo", (255, 185, 185)),
    ("Forest", (33, 64, 57)),
    ("Fruit Punch", (221, 7, 90)),
    ("Fuchsia", (220, 68, 183)),
    ("Gingerbread", (128, 93, 73)),
    ("Grape", (80, 59, 130)),
    ("Green", (138, 141, 146)),
    ("Grey", (185, 138, 51)),
    ("Honey", (255, 56, 81)),
    ("Hot Coral", (72, 71, 128)),
    ("Iris", (108, 190, 19)),
    ("Kiwi Lime", (173, 152, 212)),
    ("Lagoon", (129, 93, 52)),
    ("Lavender", (177, 181, 178)),
    ("Light Blue", (242, 42, 123)),
    ("Light Brown", (180, 222, 189)),
    ("Light Green", (122, 59, 116)),
    ("Light Grey", (177, 181, 11)),
    ("Light Pink", (246, 179, 221)),
    ("Magenta", (242, 42, 123)),
    ("Midnight", (50, 55, 85)),
    ("Mint", (180, 222, 189)),
    ("Mist", (156, 185, 199)),
    ("Mulberry", (122, 59, 116)),
    ("Olive", (132, 135, 59)),
    ("Orange", (237, 97, 32)),
    ("Orange Cream", (240, 170, 147)),
    ("Orchid", (239, 131, 232)),
    ("Parrot Green", (6, 124, 129)),
    ("Pastel Blue", (83, 144, 209)),
    ("Pastel Green", (118, 200, 130)),
    ("Pastel Lavender", (138, 114, 193)),
    ("Pastel Yellow", (254, 248, 117)),
    ("Peach", (238, 186, 178)),
    ("Pearl Green", (132, 183, 145)),
    ("Periwinkle Blue", (100, 124, 190)),
    ("Pewter", (160, 165, 165)),
    ("Pink", (228, 72, 146)),
    ("Plum", (162, 75, 156)),
    ("Prickly Pear", (182, 255, 81)),
    ("Purple", (96, 64, 137)),
    ("Raspberry", (165, 48, 97)),
    ("Red", (191, 46, 64)),
    ("Robin's Egg", (175, 225, 230)),
    ("Rose", (168, 88, 105)),
    ("Rust", (140, 55, 44)),
    ("Sage", (152, 177, 150)),
    ("Salmon", (255, 125, 100)),
    ("Sand", (228, 282, 144)),
    ("Shamrock", (0, 115, 65)),
    ("Sherbert", (225, 238, 125)),
    ("Sky", (84, 205, 227)),
    ("Slate Blue", (90, 113, 128)),
    ("Slime", (191, 182, 41)),
    ("Sour Apple", (176, 209, 105)),
    ("Spice", (227, 92, 68)),
    ("Stone", (156, 1141, 1042)),
    ("Tan", (188, 147, 113)),
    ("Tangerine", (214, 100, 45)),
    ("Teal", (32, 197, 247)),
    ("Thistle", (142, 141, 165)),
    ("Toasted Marshmallow", (235,225,205)),
    ("Tomato", (234, 66, 66)),
    ("Toothpaste", (147, 200, 212)),
    ("Turquoise", (43, 137, 198)),
    ("White", (248, 248, 248)),
    ("Yellow", (236, 216, 0))
]
color_map = {name: rgb for name, rgb in color_palette}


def get_specific_color_palette(specific_colors_file):
    with open(specific_colors_file, 'r') as file:
        lines = file.readlines()
    color_array=[]
    for line in lines:
            if line == "all":
                color_array = list(color_map.values())
                break
            else:
                color_name = line.strip()
                # Look up the RGB value for the color name from the color_palette dictionary
                rgb_value = color_map.get(color_name)
                # If the color name exists in the dictionary, add the RGB value to the array
                if rgb_value is not None:
                    color_array.append(rgb_value)
    return color_array




def floyd_steinberg_dithering(image, color_array):
    width, height = image.size
    pixels = np.array(image, dtype=np.float32)
    #color_array = np.array(color_palette, dtype=np.float32)

    for y in range(height - 1):
        for x in range(1, width - 1):
            old_pixel = pixels[y, x]
            new_pixel = get_closest_color(old_pixel, color_array)

            pixels[y, x] = new_pixel

            error = old_pixel - new_pixel
            pixels[y, x + 1] += error * 7 / 16
            pixels[y + 1, x - 1] += error * 3 / 16
            pixels[y + 1, x] += error * 5 / 16
            pixels[y + 1, x + 1] += error * 1 / 16

    # Convert the pixel values back to integers in the range [0, 255]
    pixels = np.clip(np.round(pixels), 0, 255).astype(np.uint8)

    return Image.fromarray(pixels)

def add_gridlines(image, grid_size, line_thickness):
    width, height = image.size
    draw = ImageDraw.Draw(image)

    # Draw vertical gridlines
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height - 1)], fill=(255, 255, 255), width=line_thickness)

    # Draw horizontal gridlines
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width - 1, y)], fill=(255, 255, 255), width=line_thickness)

    return image



def pixelate(image_path, pixel_height, pixel_width, specific_color_text, dithering = False):
    specific_colors_file_path = os.path.join(os.path.dirname(__file__), specific_color_text)
    color_array = get_specific_color_palette(specific_colors_file_path)

    # Load the input image
    image = Image.open(image_path)

    image = compress_image(image)


    # Compute the size of the output image in pixels
    width, height = image.size

    pixel_size = max(width//pixel_width, height//pixel_height)
    new_width = pixel_width * pixel_size
    new_height = pixel_height * pixel_size

    # Resize the image to the nearest multiple of the pixel size
    image = image.resize((new_width, new_height))

    #create color counter
    color_counter = Counter()

    if dithering:
        image = image.convert("RGB")
        image = floyd_steinberg_dithering(image, color_array)

    # Pixelate the image by replacing each region with the average color
    pixels = image.load()
    for i in range(0, new_width, pixel_size):
        for j in range(0, new_height, pixel_size):
            box = (i, j, i+pixel_size, j+pixel_size)
            region = image.crop(box)
            average_color = region.resize((1, 1)).getpixel((0, 0))
            closest_color = get_closest_color(average_color, color_array)
            # Increment the pixel count for the closest_color in the color_counter
            color_name = [name for name, rgb in color_map.items() if rgb == closest_color][0]
            color_counter[color_name] += 1
            for x in range(box[0], box[2]):
                for y in range(box[1], box[3]):
                    pixels[x, y] = closest_color

    # Calculate grid size based on the specified pixel height and width
    grid_size_x = width // pixel_width
    grid_size_y = height // pixel_height

    # Use the larger grid size between grid_size_x and grid_size_y
    grid_size = max(grid_size_x, grid_size_y)

    # Resize the image to match the grid size
    new_width = pixel_width * grid_size
    new_height = pixel_height * grid_size
    image = image.resize((new_width, new_height))

    # Add gridlines to the image with a thin line thickness
    image = add_gridlines(image, grid_size, 1)

    
    output_dir = os.path.dirname(image_path)
    output_filename = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.join(output_dir, f"{output_filename}_pixelated3.png")
    image.save(output_path)
    return image

def main():
    parser = argparse.ArgumentParser(description="Pixelate an image with custom colors.")
    parser.add_argument("image_path", type=str, help="Path to the input image.")
    parser.add_argument("pixel_height", type=int, help="Height of each pixel.")
    parser.add_argument("pixel_width", type=int, help="Width of each pixel.")
    parser.add_argument("specific_color_text", type=str, help="Path to the text file containing specific colors.")
    parser.add_argument("--dithering", action="store_true", help="Enable dithering (Floyd-Steinberg).")

    args = parser.parse_args()

    color_count = pixelate(args.image_path, args.pixel_height, args.pixel_width, args.specific_color_text, dithering=args.dithering)
    print("Color Counts in the Output Image:")
    for color_name, count in color_count.items():
        print(f"{color_name}: {count} pixels")

if __name__ == "__main__":
    main()


#pixelate("/Users/prachiheda/Desktop/NatalieDye_RaccoonMapache.jpeg", 100,70, "allcolors.txt", dithering=True) 