import json
import tkinter as tk
from tkinter import filedialog, messagebox, Frame, Button, Label
import bancoPalabras

class CompresorPalabras:
    def __init__(self, master):
        self.master = master
        self.nombre_archivo_cargado = tk.StringVar()
        self.compresor_ui()
        self.mapa_palabras = self.cargar_mapa_palabras()
        self.archivo_actual = None

    def compresor_ui(self):
        self.master.title("Compresor de Textos")
        self.master.geometry("400x300")
        self.master.configure(bg="#757575")  # Color de fondo de la ventana

        frame = Frame(self.master, bg="#757575")
        frame.pack(padx=20, pady=20)

        # Botón para cargar archivo
        btn_cargar = Button(frame, text="Seleccionar Archivo (.txt)", command=self.cargar_archivo, bg="#1976d2", fg="white", bd=0, padx=10, pady=5)
        btn_cargar.config(font=("Arial", 12, "bold"))
        btn_cargar.pack(fill=tk.X, pady=(0, 10))
        
        # Etiqueta para mostrar la ruta del archivo cargado
        self.archivo_label = Label(frame, textvariable=self.nombre_archivo_cargado, fg="#303434", bg="#757575", font=("Arial", 10))
        self.archivo_label.pack(fill=tk.X, pady=(10, 0))

        self.archivo_label = Label(frame, text="", fg="#333333", bg="#757575", font=("Arial", 10))
        self.archivo_label.pack(fill=tk.X, pady=(10, 0))
        
        # Etiqueta para "Elija una opción"
        label_opcion = Label(frame, text="Elija una opción:", fg="#000000", bg="#757575", font=("Arial", 14, "bold"))
        label_opcion.pack(fill=tk.X, pady=(0, 10))

        # Botón para comprimir
        btn_comprimir = Button(frame, text="Comprimir archivo", command=lambda: self.procesar_archivo(comprimir=True), bg="#ff9800", fg="white", bd=0, padx=10, pady=5)
        btn_comprimir.config(font=("Arial", 12, "bold"))
        btn_comprimir.pack(fill=tk.X, pady=(0, 5))

        # Botón para descomprimir
        btn_descomprimir = Button(frame, text="Descomprimir archivo", command=lambda: self.procesar_archivo(comprimir=False), bg="#ff9800", fg="white", bd=0, padx=10, pady=5)
        btn_descomprimir.config(font=("Arial", 12, "bold"))
        btn_descomprimir.pack(fill=tk.X, pady=(0, 5))


    def cargar_mapa_palabras(self):
        with open('mapa_palabras.json') as archivo:
            datos = json.load(archivo)

        caracteres_especiales = [chr(i) for i in range(32, 1000) if chr(i) not in 'aeiouyAEIOUY.0123456789']
        compresion_mapa = {}
        descompresion_mapa = {}

        for palabra, char in zip(datos.keys(), caracteres_especiales):
            compresion_mapa[palabra] = ' ' + char + ' '
            descompresion_mapa[' ' + char + ' '] = ' ' + palabra + ' '

        return compresion_mapa, descompresion_mapa

    def cargar_archivo(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            self.archivo_actual = filepath
            self.nombre_archivo_cargado.set("Archivo cargado: " + filepath)
            messagebox.showinfo("Archivo cargado", "Archivo cargado correctamente.")

    def procesar_archivo(self, comprimir=True):
        if not self.archivo_actual:
            messagebox.showwarning("Advertencia", "Primero debe cargar un archivo.")
            return

        with open(self.archivo_actual, 'r', encoding='utf-8') as file:
            contenido = file.read()

        resultado = self.comprimir_texto(contenido) if comprimir else self.descomprimir_texto(contenido)

        save_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(resultado)
            messagebox.showinfo("Éxito", "El archivo ha sido guardado correctamente.")

    def comprimir_texto(self, texto):
        texto = ' ' + texto.lower() + ' '
        for palabra, char in self.mapa_palabras[0].items():
            texto = texto.replace(' ' + palabra + ' ', char)
        return texto.strip()

    def descomprimir_texto(self, texto):
        texto = ' ' + texto + ' '
        for char, palabra in self.mapa_palabras[1].items():
            texto = texto.replace(char, palabra)
        return texto.strip()

def main():
    root = tk.Tk()
    root.configure(bg="#424242")  # Color de fondo de la ventana principal
    app = CompresorPalabras(root)
    root.mainloop()

if __name__ == "__main__":
    main()


