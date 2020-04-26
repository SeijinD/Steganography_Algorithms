# Lirary for edit image
from PIL import Image

i=0 # Counter
data = "01010011011001010110100101101010011010010110111001000100" # Data = SeijinD
with Image.open("register.png") as img: # Open image file and give img name
    width, height = img.size # Set width and height from image size
    for x in range(0, width): # Loop for all width pixels
        for y in range(0, height): # Loop for all height pixels
            pixel = list(img.getpixel((x, y))) # Get pixel for 2 loops with x and y
            for n in range(0,3): # Loop for 3 RGB values
                if(i < len(data)): # If counter is smaller for len from data go in if code
                    pixel[n] = pixel[n] & ~1 | int(data[i]) # Put pixel[n] the data with the change
                    i+=1 # Increase i with 1
            img.putpixel((x,y), tuple(pixel)) # Change a pixel with other pixel(changed pixel)
    img.save("source_secret.png", "PNG") # Save steganography image