import tkinter as tk
ventana = tk.Tk()
ventana.title("Mi aplicación Tkinter")
ventana.geometry("800x500+200+100")
ventana.resizable(True, False)
ventana.configure(bg="gold")

ventana.state("zoomed")
ventana.attributes("-alpha", 0.85)
ventana.minsize(600, 400)
ventana.maxsize(1200, 800)
ventana.mainloop()