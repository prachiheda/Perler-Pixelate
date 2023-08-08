# Perler-Pixelate
Pixelate any image using a Perler color palette 

The pixelate_image script allows you to pixelate an image using a specified pixel size and a custom color palette. It offers the option to apply dithering using the Floyd-Steinberg algorithm for smoother color transitions. The script also supports adding gridlines to the pixelated image.

python pixelate_image.py image_path pixel_height pixel_width specific_color_text [--dithering]

image_path: Path to the input image.

pixel_height: Height of each pixel in the pixelated output.

pixel_width: Width of each pixel in the pixelated output.

specific_color_text: Path to the text file containing specific colors (one color per line) or "all" for using the entire color palette. The script includes a predefined color palette with a variety of color names and their corresponding RGB values. You can specify a subset of these colors or use the entire palette.

--dithering: (Optional) Enable dithering (Floyd-Steinberg algorithm) for smoother color transitions. Floyd-Steinberg dithering works by distributing the quantization error (the difference between the original color and the closest available color in the palette) to neighboring pixels. This redistribution of errors across adjacent pixels helps create smoother transitions between colors and preserves more detail in the image.

The pixelate_GUI script is a simple graphical user interface application built using the tkinter library in Python, designed to pixelate images and provide color palette options. The app enables you to upload an image, select a color palette, specify pixel dimensions, and then pixelate and save the modified image.

Features

Upload an image: Choose an image (JPG or PNG format) from your local file system to pixelate.

Select a color palette: Pick from a predefined list of colors to use for pixelation.

Specify pixel dimensions: Enter the desired pixel height and width for the pixelation effect.

Pixelate the image: Click the "Pixelate!" button to apply the pixelation effect to the uploaded image using the selected color palette and pixel dimensions.

Download the pixelated image: Save the pixelated image in JPG or PNG format to your preferred location.

