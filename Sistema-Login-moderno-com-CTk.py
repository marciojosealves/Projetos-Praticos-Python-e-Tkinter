# Sistema de login

import customtkinter as ctk
from tkinter import *
#import banco_dados_cadastro
from tkinter import messagebox

janela = ctk.CTk()


class Aplicacao():

    def __init__(self):
        self.janela = janela
        self.tema()
        self.janela_basica()
        self.elementos_janela_basica()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def janela_basica(self):
        janela.wm_geometry("700x400")
        janela.wm_title("Sistema de Login")
        janela.wm_iconbitmap("logo-mjamf.ico")
        janela.wm_resizable(width=False, height=False)

    def elementos_janela_basica(self):
        # Parte de trabalho relativa a imagem da tela.
        imagem_janela = PhotoImage(file="logo-mjamf.png")
        # text = None ou '' para retirar o CTkLabel
        label_imagem_janela = ctk.CTkLabel(
            master=janela, image=imagem_janela, text=None).place(x=45, y=100)
        label_titulo = ctk.CTkLabel(master=janela, text='Entre no Sistema de Login MJAMF', font=(
            'Arvo', 18), text_color='#d75413').place(x=23, y=10)

        # Frame de inclusão de dados
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # Frame Widgets e elementos de inclusão de dados
        nome_frame = ctk.CTkLabel(master=login_frame, text=('Sistema de Login'), font=('Arvo', 20)).place(
            x=25, y=5)  # Veja https://github.com/TomSchimansky/CustomTkinter/wiki/CTkLabel

        nome_usuario = ctk.CTkEntry(master=login_frame, placeholder_text=(
            'Nome do Usuário'), font=('Arvo', 14), width=300).place(x=25, y=105)
        label_nome_usuario = ctk.CTkLabel(
            master=login_frame, text='*O campo Nome do Usuário é obrigatório!', font=('Arvo', 10), text_color='#d75413').place(x=25, y=135)

        senha_usuario = ctk.CTkEntry(master=login_frame, placeholder_text=(
            'Senha do Usuário'), font=('Arvo', 14), width=300, show='*').place(x=25, y=175)
        label_senha_usuario = ctk.CTkLabel(
            master=login_frame, text='*O campo Senha do Usuário é obrigatório!', font=('Arvo', 10), text_color='#d75413').place(x=25, y=205)

        marcador_checagem = ctk.CTkCheckBox(
            master=login_frame, text='Lembrar depois.').place(x=25, y=245)

        def mensagem_login():

            mensagem_login_sucesso = messagebox.showinfo(
                title='Resultado do Login', message='Login realizado com Sucesso!')

        botao_login = ctk.CTkButton(
            master=login_frame, text='LOGIN', width=300, fg_color='#d75413', hover_color='#ff8000', command=mensagem_login).place(x=25, y=285)

        label_resgistro = ctk.CTkLabel(
            master=login_frame, text='Faça sau conta.'). place(x=25, y=325)

        def janela_cadastro():
            # Remover janela de login
            login_frame.pack_forget()

            # Criando janela de cadastro so Usuário
            registro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            registro_frame.pack(side=RIGHT)

            nome_frame_registro = ctk.CTkLabel(master=registro_frame, text=('Registro no sistema'), font=('Arvo', 20)).place(
                x=25, y=5)

            frase_obrigatoria = ctk.CTkLabel(master=registro_frame, text=(
                'Insira todos os dados corretos.'), font=('Arvo', 15), text_color='#d75413').place(x=25, y=35)

            nome_usuario_registro = ctk.CTkEntry(master=registro_frame, placeholder_text=(
                'Nome do Usuário'), font=('Arvo', 14), width=300).place(x=25, y=105)

            email_usuario_registro = ctk.CTkEntry(master=registro_frame, placeholder_text=(
                'E-mail do Usuário'), font=('Arvo', 14), width=300).place(x=25, y=145)

            senha_usuario_registro = ctk.CTkEntry(master=registro_frame, placeholder_text=(
                'Senha do Usuário'), font=('Arvo', 14), width=300, show='*').place(x=25, y=185)

            confirme_senha_registro = ctk.CTkEntry(master=registro_frame, placeholder_text=(
                'Confirme Senha'), font=('Arvo', 14), width=300, show='*').place(x=25, y=225)

            marcador_checagem = ctk.CTkCheckBox(
                master=registro_frame, text='Aceito termos e condições de registro.').place(x=25, y=265)

            # Função para retorna na tela um vista anterior
            def voltar_login():
                # Para remover frame de cadastro
                registro_frame.pack_forget()

                # Traz o fremede login novamente
                login_frame.pack(side=RIGHT)

            voltar_janela = ctk.CTkButton(master=registro_frame, text='Voltar', width=145,
                                          fg_color='gray', hover_color='#989a91', command=voltar_login).place(x=25, y=325)

            def savar_dados_usuario():

                mensagem_cadastro = messagebox.showinfo(
                    title='Resultado do Cadastro', message='Cadastro realizado com Sucesso!')

            salvar_registro = ctk.CTkButton(master=registro_frame, text='Cadastro', width=145,
                                            fg_color='#d75413', hover_color='#ff8000', command=savar_dados_usuario).place(x=180, y=325)

        botao_registro = ctk.CTkButton(master=login_frame, text='Cadastro', width=190,
                                       fg_color='#d75413', hover_color='#ff8000', command=janela_cadastro).place(x=135, y=325)


Aplicacao()
