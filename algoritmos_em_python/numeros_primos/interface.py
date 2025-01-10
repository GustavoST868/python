import tkinter as tk
import primo
def Interface():

    def Calculate():
        value = int(field_number.get())
        result = primo.Primo(value)
        label_result.config(text=f"Resultado = [{result}]")

    window = tk.Tk()
    window.title("Número Primo")
    window.geometry("220x70")
    label_number = tk.Label(window,text="Número:")
    label_number.grid(row=0,column=0,padx=5,pady=5)
    field_number = tk.Entry(window)
    field_number.configure(background="gray76")
    field_number.grid(row=0,column=1,padx=5,pady=5)
    button_calculate = tk.Button(window,text="Calcular",command=Calculate)
    button_calculate.configure(background="lime green")
    button_calculate.grid(row=1,column=0,padx=5,pady=5)
    label_result = tk.Label(window,text="Resultado = []")
    label_result.grid(row=1,column=1,padx=5,pady=5)
    window.mainloop()