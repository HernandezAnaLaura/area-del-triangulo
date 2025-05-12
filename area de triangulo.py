
import tkinter as tk
def calcular_promedio():
    try:
        base = float(entrada_base.get())
        altura = float(entrada_altura.get())
        area = (base*altura) / 2
        if area >= 100:
            resultado = f"el area es grande{area}"
        else:
            resultado = f"el area es pequeña{area}"
        etiqueta_resultado.config(text=resultado)
    except ValueError:
        etiqueta_resultado.config(text="ingresa tus datos")
def repetir():
    entrada_base.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    etiqueta_resultado.config(text="")
def cerrar():
    ventana.destroy()
ventana = tk.Tk()
ventana.title("Calculadora de area")
ventana.geometry("500x400")
ventana.config(bg="plum")  # Morado claro
etiqueta_titulo = tk.Label(ventana, text="Ingresa tus datos", bg="plum", font=("Arial", 14))
etiqueta_titulo.pack(pady=10)
etiqueta1 = tk.Label(ventana, text="base", bg="pink")
etiqueta1.pack()
entrada_base = tk.Entry(ventana)
entrada_base.pack()
etiqueta2 = tk.Label(ventana, text="altura", bg="pink")
etiqueta2.pack()
entrada_altura= tk.Entry(ventana)
entrada_altura.pack()
boton_calcular = tk.Button(ventana, text="calcular area", command=calcular_promedio, bg="white", width=25)
boton_calcular.pack(pady=20)
etiqueta_resultado = tk.Label(ventana, text="", bg="pink")
etiqueta_resultado.pack(pady=10)
boton_si=tk.Button(ventana, text="Repetir",command=repetir)
boton_si.pack()
boton_cerrar=tk.Button(ventana, text="fin",command=cerrar)
boton_cerrar.pack()
ventana.mainloop()
