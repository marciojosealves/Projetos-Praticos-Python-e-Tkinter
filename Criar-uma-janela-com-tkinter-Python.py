from tkinter import *
from tkinter import ttk

minha_aplicacao = Tk()

 # Título da janela
minha_aplicacao.wm_title("Minha Aplicação") 

 # Logo ícone.
minha_aplicacao.iconbitmap('logo-mjamf.ico')

# Pode-se usar o grid(row=1, column = 25) para caso específicos.
texto_inicial = ttk.Label(text="Olá Márcio José!!!").place(x=1, y=25)

# Responsividade
minha_aplicacao.wm_geometry('700x400')
minha_aplicacao.wm_resizable(width=False, height=False)
#minha_aplicacao.wm_maxsize(width=900,height=600)
#minha_aplicacao.wm_minsize(width=400,height=200)




minha_aplicacao.mainloop()
