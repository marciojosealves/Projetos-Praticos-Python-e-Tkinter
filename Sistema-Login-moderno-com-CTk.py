# Sistema de login

import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.wm_geometry("700x400")
janela.wm_title("Sistema de Login")
janela.wm_iconbitmap("logo-mjamf.ico")
janela.wm_resizable(width=False, height=False)

imagem_janela = PhotoImage( file="logo-mjamf2.png")
label_imagem_janela = customtkinter.CTkLabel(master=janela, image=imagem_janela)
label_imagem_janela.place(x=5,y=70)


janela.mainloop()
