from tkinter import *
from tkinter import ttk

minha_aplicacao= Tk()
minha_aplicacao.title("Minha Aplicação")#Título da janela
minha_aplicacao.iconbitmap('logo-mjamf.ico')

texte_inicial = ttk.Label(text = "Olá Márcio José!!!").place(x=1, y=25) # Pode-se usar o grid(row=1, column = 25) para caso específicos.

minha_aplicacao.mainloop()