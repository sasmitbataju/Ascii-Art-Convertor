from PIL import Image
from termcolor import colored, cprint

# Open image and convert that image to grey scale.
image = Image.open("1d9464dbff7a1630882d0e2090cb714c.jpg").convert("L")

# Get RGB data of the converted jpeg.
print(image.format, image.size, image.mode)

# List RGB database
convert = list(image.getdata())

# Resize greyscale img so that it scales it down and fits the terminal screen.
new_width = 80
new_height = 40

# Accept incoming calls.
image = image.resize((new_width, new_height), Image.ANTIALIAS)

# Save image.
image.save('windows10.png')

# Add ascii chars after every gap.
s = ''.join([chr(c) for c in convert])

# Print final output as art.
cprint(s)