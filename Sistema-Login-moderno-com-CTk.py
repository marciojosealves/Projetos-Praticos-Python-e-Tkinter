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

#Parte de trabalho relativa a imagem da tela.
imagem_janela = PhotoImage( file="logo-mjamf.png")
label_imagem_janela = customtkinter.CTkLabel(master=janela, image=imagem_janela, text = None )#text = None ou '' para retirar o CTkLabel
label_imagem_janela.place(x=45,y=100)
label_titulo=customtkinter.CTkLabel(master=janela, text='Entre no Sistema de Login MJAMF', font=('Arvo',18), text_color='green').place(x=23,y=10)

#Frame de inclusão de dados
frame = customtkinter.CTkFrame(master = janela, width = 350, height = 396)
frame.pack(side=RIGHT)

#Frame Widgets
nome_frame = customtkinter.CTkLabel(master=frame, text=('Sistema de Login'), font=('Arvo',20))#Veja https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel
nome_frame.place(x=25,y=5)

nome_usuario = customtkinter.CTkEntry(master=frame, placeholder_text=('Nome do Usuário'), font=('Arvo',14), width=300).place(x=25,y=105)
label_nome_usuario = customtkinter.CTkLabel(master=frame, text='*O campo Nome do Usuário é obrigatório!', font=('Arvo',10), text_color='green').place(x=25,y=135)

senha_usuario = customtkinter.CTkEntry(master=frame, placeholder_text=('Senha do Usuário'), font=('Arvo',14), width=300).place(x=25,y=175)
label_senha_usuario = customtkinter.CTkLabel(master=frame, text='*O campo Senha do Usuário é obrigatório!', font=('Arvo',10), text_color='green').place(x=25,y=205)

marcador_checagem = customtkinter.CTkCheckBox(master= frame, text='Lembrar depois.').place(x=25,y=235)

botao_login = customtkinter.CTkButton(master =frame, text ='LOGIN', width=300).place(x=25,y=285)


janela.mainloop()
