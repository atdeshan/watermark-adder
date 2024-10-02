import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageDraw,ImageFont


def saveImage(image):
    save_file = asksaveasfilename(title="Save image",filetypes=[("image", ".png")])
    image.save(save_file)
def preview(image):
    previewWindow = tk.Toplevel(root)
    previewWindow.title("Preview")
    previewWindow.geometry("800x800")
    preview = image.resize((600, 600))
    preview = ImageTk.PhotoImage(preview)
    preview_lable = tk.Label(previewWindow, imag=preview)
    preview_lable.image = preview
    preview_lable.pack(padx=20, pady=20)
    download = tk.Button(previewWindow, text="Download", command=lambda:saveImage(image))
    download.pack(padx=20, pady=20)
    previewWindow.mainloop()
def process_image(water_mark):
    file_path = askopenfilename(title="Choose an image",filetypes=[("image", ".png")])
    image = Image.open(file_path)
    try:
        font = ImageFont.truetype("Helvetica.ttc", 50)
    except:
        font = ImageFont.load_default()
    drow = ImageDraw.Draw(image)
    drow.text((20, 20), water_mark, fill=(255, 255, 255),font=font)

    preview(image)
    
    
root = tk.Tk()
root.title("WaterMark Genarator")
root.geometry("300x250")

lable = tk.Label(root,text="Enter Your Watermark")
lable.place(relx=0.5,rely=0.1,anchor="center")
water_mark = tk.Entry(root,width=20,borderwidth=1, relief="solid")
water_mark.place(relx=0.5,rely=0.6,anchor="center")
add_image = tk.Button(root,text="process",command=lambda:process_image(f"{water_mark.get()}"))
add_image.place(relx=0.5,rely=0.8,anchor="center")
root.mainloop()