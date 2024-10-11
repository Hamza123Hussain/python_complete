import sys
from PIL import Image

# Initialize an empty list to hold images
images = []

# Loop over the command-line arguments (starting from index 1 to skip the script name)
for arg in sys.argv[1:]:
    try:
        # Open the image file and append it to the list of images
        image = Image.open(arg)
        images.append(image)
    except Exception as e:
        print(f"Error opening {arg}: {e}")

# Ensure that we have at least two images to create a GIF
if len(images) > 1:
    # Save the first image as a GIF and append the rest as frames
    images[0].save(
        'Giff.gif',  # Output GIF file name
        save_all=True,  # Save all frames
        append_images=images[1:],  # Append the rest of the images as frames
        duration=200,  # Frame duration in milliseconds
        loop=0  # Loop indefinitely
    )
    print("GIF created successfully!")
else:
    print("Error: Need at least two images to create a GIF.")
