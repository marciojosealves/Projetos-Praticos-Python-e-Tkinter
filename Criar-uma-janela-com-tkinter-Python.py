from tkinter import *
from tkinter import ttk

minha_aplicacao = Tk()

 # Título da janela
minha_aplicacao.wm_title("Minha Aplicação") 

 # Logo ícone.
minha_aplicacao.iconbitmap('logo-mjamf.ico')

# Pode-se usar o grid(row=1, column = 25) para caso específicos.
texto_inicial = ttk.Label(text="Olá Márcio José!!!").place(x=1, y=25) #Para utilizar métrica de distâncias faça: em cm x=1c, em mm x=1m, em pol x=1i e em pontos de impressão x=1p. 

texto_inicial = ttk.Label(text="Olá Pessoas!!!", foreground='blue').place(x='1m', y='25m')# foreground para cor de texto.

# Responsividade
minha_aplicacao.wm_geometry('700x400')
minha_aplicacao.wm_resizable(width=False, height=False)
#minha_aplicacao.wm_maxsize(width=900,height=600)
#minha_aplicacao.wm_minsize(width=400,height=200)

#Cor de fundo da aplicação
minha_aplicacao.configure(background="#d75413")






minha_aplicacao.mainloop()
