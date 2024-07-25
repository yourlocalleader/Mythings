import tkinter as tk
from tkinter import messagebox



# capitalismo
capitalismo = "liberal? libera pra nois ai ent po nmrlzinha"
# egosocialismo

egosocialismo = "based"

# socialismo
socialismo = "discordo um pouco de vc mas tu é based"

# fascismo
fascismo = "off to the gulag you go"
# func btn
def melhor_ideologia():
    ideia = entrada.get()
    if ideia == "capitalismo": messagebox.showinfo("", f" {capitalismo}")
    if ideia == "egosocialismo": messagebox.showinfo("", f" {egosocialismo}")  
    if ideia == "socialismo": messagebox.showinfo("", f" {socialismo}")
    if ideia == "fascismo": messagebox.showinfo("", f" {fascismo}")
# janela
janela = tk.Tk()
janela.title("egosoc")
janela.geometry("300x200")

# rotulo
rotulo = tk.Label(janela, text="Socialismo, Capitalismo, Ego-Socialismo ou Fascismo?")
rotulo.pack(pady=5)

# txt entry
entrada = tk.Entry(janela)
entrada.pack(pady=5)

# btn
botao = tk.Button(janela, text="click to discover all the truth", command=melhor_ideologia)
botao.pack(pady=10)


janela.mainloop()
