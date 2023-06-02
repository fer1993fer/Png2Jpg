
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.font import Font
from PIL import Image

class Converter(tk.Tk) :
    def __init__(self) :
        super().__init__()

        self.f = Font(family='Cantarell-Bold', name='q', size=12, weight='bold', slant="italic")


        self.s = ttk.Style()
        self.s.configure("TLabel", font=self.f)
        self.s.configure("F.TButton", font=self.f)

        self.resizable(False,False)
        self.geometry("426x240")
        self.title("JPG2PNG")
       
        self.fr = tk.Frame(master=self)
        self.fr.configure(height=230, width=416, borderwidth=5)
        self.fr.place(x=5, y=5)

        self.et = ttk.Label(master=self.fr)
        self.et.configure(text="Selecciona la carpeta con tus imagenes")
        self.et.place(x=20, y=25)

        self.ent = tk.Entry(master=self.fr, width=20)
        self.ent.place(x=115, y=60)

        self.btn = tk.Button(master=self.fr)
        self.btn.configure(command=self.imgf, text="...", border=0)
        self.btn.place(x=280, y=73, height=10, width=20)

        self.et2 = ttk.Label(master=self.fr)
        self.et2.configure(text="Selecciona la carpeta de destino", border=0)
        self.et2.place(x=50, y=100)
        
        self.ent2 = tk.Entry(master=self.fr, width=20)
        self.ent2.place(x=115, y=130)

        self.btn2 = tk.Button(master=self.fr)
        self.btn2.configure(command=self.destf, text="...", border=0)
        self.btn2.place(x=280, y=143, height=10, width=20)

        self.btn3 = ttk.Button(master=self.fr)
        self.btn3.configure(text="Iniciar", command=self.inicio, style="F.TButton")
        self.btn3.place(x=150, y= 180)


    def imgf(self) :
        im = askdirectory(title="Seleccion de carpeta contenedora")
        self.ent.insert(tk.END, im)

    def destf(self) :
        imm = askdirectory(mustexist=True, title="Seleccion de carpeta destino")
        self.ent2.insert(tk.END, imm)

    def inicio(self) :
        image_folder = self.ent.get()
        output_folder = self.ent2.get()
        for files in os.listdir(image_folder) :     
            nombre, extencion = os.path.splitext(files)
            if extencion in [".png", "PNG"] :
                with Image.open(image_folder + "/" + files) as img :
                    ctimg = img.convert("RGB")
                    ctimg.save(output_folder + "/" + nombre + ".jpg")

if __name__ == "__main__" :
    app = Converter()
    app.mainloop()
