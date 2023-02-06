# Sistema de login

import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.wm_geometry("700x400")
janela.wm_title("Sistema de Login")
janela.wm_iconbitmap("logo-mjamf.ico")
janela.wm_resizable(width=False, height=False)

#Parte de trabalho relativa a imagem da tela.
imagem_janela = PhotoImage( file="logo-mjamf.png")
label_imagem_janela = ctk.CTkLabel(master=janela, image=imagem_janela, text = None )#text = None ou '' para retirar o CTkLabel
label_imagem_janela.place(x=45,y=100)
label_titulo=ctk.CTkLabel(master=janela, text='Entre no Sistema de Login MJAMF', font=('Arvo',18), text_color='green').place(x=23,y=10)

#Frame de inclusão de dados
login_frame = ctk.CTkFrame(master = janela, width = 350, height = 396)
login_frame.pack(side=RIGHT)

#Frame Widgets
nome_frame = ctk.CTkLabel(master=login_frame, text=('Sistema de Login'), font=('Arvo',20))#Veja https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
nome_frame.place(x=25,y=5)

nome_usuario = ctk.CTkEntry(master=login_frame, placeholder_text=('Nome do Usuário'), font=('Arvo',14), width=300).place(x=25,y=105)
label_nome_usuario = ctk.CTkLabel(master=login_frame, text='*O campo Nome do Usuário é obrigatório!', font=('Arvo',10), text_color='green').place(x=25,y=135)

senha_usuario = ctk.CTkEntry(master=login_frame, placeholder_text=('Senha do Usuário'), font=('Arvo',14), width=300, show ='*').place(x=25,y=175)
label_senha_usuario = ctk.CTkLabel(master=login_frame, text='*O campo Senha do Usuário é obrigatório!', font=('Arvo',10), text_color='green').place(x=25,y=205)

marcador_checagem = ctk.CTkCheckBox(master= login_frame, text='Lembrar depois.').place(x=25,y=235)

botao_login = ctk.CTkButton(master =login_frame, text ='LOGIN', width=300).place(x=25,y=285)


janela.mainloop()
