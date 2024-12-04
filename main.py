from tkinter import *
from PIL import Image
import os


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
FONT_NAME = "Courier"


# ---------------------------- FUNCTIONS ------------------------------- #
def watermark(position):

    # Image setup
    image_directory = os.fsencode("./Images")
    for file in os.listdir(image_directory):
        filename = os.fsdecode(file)
        img = Image.open(f"./Images/{filename}")
        img_w, img_h = img.size

        # Logo setup
        logo_directory = os.fsencode("./Logo")
        logo = Image.open(f"./Logo/{os.fsdecode(os.listdir(logo_directory)[0])}")
        if img_w < img_h:
            logo = logo.resize((img_w // 6, img_w // 6))
        else:
            logo = logo.resize((img_h // 6, img_h // 6))
        logo_w, logo_h = logo.size
        logo.putalpha(128)

        # Offset setup
        w_preset = (img_w - logo_w)
        h_preset = (img_h - logo_h)
        offset_dict = {"middle_centre": (w_preset // 2, h_preset // 2),
                       "bottom_centre": (w_preset // 2, h_preset),
                       "middle_right": (w_preset, h_preset // 2),
                       "bottom_right": (w_preset, h_preset),
                       "bottom_left": (w_preset // w_preset, h_preset),
                       "middle_left": (w_preset // w_preset, h_preset // 2),
                       "top_left": (w_preset // w_preset, h_preset // h_preset),
                       "top_centre": (w_preset // 2, h_preset // h_preset),
                       "top_right": (w_preset, h_preset // h_preset)
                       }
        offset = offset_dict[position]

        img.paste(logo, offset, logo)
        img.save(f"./WatermarkedImages/{filename.split(".")[0]}_watermarked.png")


# ---------------------------- UI SETUP -------------------------------- #
# Window setup
window = Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=30, bg=PINK)

# Buttons
top_left = Button(text=" Top Left  ", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("top_left"))
top_left.grid(column=0, row=0, padx=2, pady=2)
top_centre = Button(text=" top centre  ", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("top_centre"))
top_centre.grid(column=1, row=0, padx=2, pady=2)
top_right = Button(text=" Top right  ", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("top_right"))
top_right.grid(column=2, row=0, padx=2, pady=2)

middle_left = Button(text="middle Left", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("middle_left"))
middle_left.grid(column=0, row=1, padx=2, pady=2)
middle_centre = Button(text="middle centre", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("middle_centre"))
middle_centre.grid(column=1, row=1, padx=2, pady=2)
middle_right = Button(text="middle right", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("middle_right"))
middle_right.grid(column=2, row=1, padx=2, pady=2)

bottom_left = Button(text="bottom Left", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("bottom_left"))
bottom_left.grid(column=0, row=2, padx=2, pady=2)
bottom_centre = Button(text="bottom centre", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("bottom_centre"))
bottom_centre.grid(column=1, row=2, padx=2, pady=2)
bottom_right = Button(text="bottom right", font=(FONT_NAME, 15, "bold"), command=lambda: watermark("bottom_right"))
bottom_right.grid(column=2, row=2, padx=2, pady=2)


window.mainloop()
