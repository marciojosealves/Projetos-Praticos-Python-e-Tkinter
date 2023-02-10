import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
# letras ASCII (todas as letras de "a" a "z", maiúsculas e minúsculas)
from string import ascii_letters


class lado_servidor():

    def conexao_banco_dados(self):
        self.faca_conexao = sqlite3.connect("Sistema_Login_Cadastro.db")
        self.cursor = self.faca_conexao.cursor()
        print("Banco de dados conectado!")

    def desconexao_banco_dados(self):
        self.faca_conexao.close()
        print("Banco de dados desconectado!")

    def iniciar_tabela_dados(self):
        self.conexao_banco_dados()

        self.cursor.execute("""
            
            CREATE TABLE IF NOT EXISTS Usuarios(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome_usuario TEXT NOT NULL,
            Email_usuario TEXT NOT NULL,
            Senha_usuario TEXT NOT NULL,
            Confirme_senha_usuario TEXT NOT NULL

            );
         
         """)  # Nome_usuario,Email_usuario e outros elementos são as colunas na tabela.
        self.faca_conexao.commit()
        print("Tabela criada no banco de dados com sucesso!")
        self.desconexao_banco_dados()

    def cadastrar_usuario_banco_dados(self):

        self.nome_usuario_entrada = self.nome_usuario_registro.get()
        self.email_usuario_entrada = self.email_usuario_registro.get()
        self.senha_usuario_entrada = self.senha_usuario_registro.get()
        self.confirme_senha_entrada = self.confirme_senha_registro.get()

        self.conexao_banco_dados()

        self.cursor.execute("""

            INSERT INTO Usuarios (Nome_usuario, Email_usuario, Senha_usuario, Confirme_senha_usuario)
            VALUES (?,?,?,?)""", (self.nome_usuario_entrada, self.email_usuario_entrada, self.senha_usuario_entrada, self.confirme_senha_entrada))

        try:
            if (self.nome_usuario_entrada == "" or self.email_usuario_entrada == "" or self.senha_usuario_entrada == "" or self.confirme_senha_entrada == ""):
                messagebox.showerror(
                    title="Sistema de Login", message="Todos os campos devem ser preenchidos!")
            elif all(caracter in (ascii_letters + 'áéíóú') for caracter in self.nome_usuario_entrada):
                # (ascii_letters + 'áéíóú') acrescenta o espaço e algumas letras acentuadas, adicione tudo que precisar aqui
                messagebox.showwarning(
                    title="Sistema de Login", message="Por favor digite um nome válido com pelo menos,\nnome e último nome.\n(somente letras e espaços)")
            elif (len(self.senha_usuario_entrada) < 4):
                messagebox.showwarning(
                    title="Sistema de Login", message=" O senha deve ter pelo menos quatro caracteres.")
            elif (self.senha_usuario_entrada != self.confirme_senha_entrada):
                messagebox.showerror(
                    title="Sistema de Login", message="Senhas não são iguais!")
            else:
                self.faca_conexao.commit()
                messagebox.showinfo(
                    title="sistema de Login", message=f"Dados cadastrados com sucesso!\n{self.nome_usuario_entrada} seja BEM-VINDO!")
                print("Dados cadastrados com sucesso!")
                self.desconexao_banco_dados()
                self.limpa_cadastro()

        except:
            messagebox.showerror(
                title="Sistema de Login", message="Erro no processamento do seu pedido!\n Tente novamente mais tarde.")
            self.desconexao_banco_dados()

    def verificar_login(self):

        self.nome_usuario_login_verifica = self.nome_usuario_login.get()
        self.senha_usuario_login_verifica = self.senha_usuario_login.get()

        self.conexao_banco_dados()

        self.cursor.execute("""

            SELECT * FROM Usuarios WHERE (Nome_usuario = ? AND Senha_usuario = ?)""", (self.nome_usuario_login_verifica, self.senha_usuario_login_verifica))

        # Percorre a tabela Usuarios é indicado .fetchone(),mas pode usar .fetchall()
        self.verifica_dados = self.cursor.fetchone()

        try:
            if (self.nome_usuario_login_verifica == "" or self.senha_usuario_login_verifica == ""):
                messagebox.showwarning(
                    title="Sistema de Login", message="Os campos devem ser todos preenchidos.")
            elif (self.nome_usuario_login_verifica in self.verifica_dados and self.senha_usuario_login_verifica in self.verifica_dados):
                messagebox.showinfo(
                    title="Sistema de Login", message=f"BEM-VINDO {self.nome_usuario_login_verifica}\n Login realizado com sucesso.")
                self.desconexao_banco_dados()
                # Se hovesse um painel, seria encaminhado para ele.
                self.limpa_login()

        except:
            messagebox.showerror(
                title="Sistema de Login", message="Usuário não encontrado no sistema.\nVerifique seus dados ou faça seu cadastro.")
            self.desconexao_banco_dados()
            # Aqui não limpamos os dados para usuário verificar se digitou corretamente.


class aplicativo(ctk.CTk, lado_servidor):
    def __init__(self):
        super().__init__()
        self.tema()
        self.Configuracao_janela_principal()
        self.elementos_janela_basica()
        # self.elementos_de_janela_cadastro()
        # self.voltar_login()
        self.iniciar_tabela_dados()

    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    # Configuração da janela principal
    def Configuracao_janela_principal(self):
        self.wm_geometry("700x400")
        self.wm_title("Sistema de Login")
        self.wm_iconbitmap("logo-mjamf.ico")
        # com wm_resizable é itulizado o sistema atual
        self.wm_resizable(width=False, height=False)

    def elementos_janela_basica(self):
        # Parte de trabalho relativa a imagem da tela.
        self.imagem_janela = PhotoImage(file="logo-mjamf.png")

        # text = None ou '' para retirar o CTkLabel
        self.label_imagem_janela = ctk.CTkLabel(
            self, image=self.imagem_janela, text=None)
        self.label_imagem_janela.grid(row=1, column=0, padx=40, pady=40)

        # Título da janela
        self.label_titulo = ctk.CTkLabel(self, text='Entre no Sistema no MJAMF\n para Login ou cadstro.', font=(
            'Arvo bold', 18), text_color='#d75413')
        self.label_titulo.grid(row=0, column=0, padx=1, pady=20)

        # frame do formulário de login
        self.login_frame = ctk.CTkFrame(self, width=350, height=396)
        self.login_frame.place(x=347, y=2)

        # Frame Widgets e elementos de inclusão de dados
        self.nome_frame = ctk.CTkLabel(self.login_frame, text=(
            'Sistema de Login'), font=('Arvo bold', 20))
        self.nome_frame.grid(row=0, column=0, padx=10, pady=10)

        self.nome_usuario_login = ctk.CTkEntry(self.login_frame, placeholder_text=(
            'Nome do Usuário'), font=('Arvo', 14), width=300, corner_radius=15, border_color="#d75413")
        self.nome_usuario_login.grid(row=1, column=0, padx=15, pady=10)

        label_nome_usuario = ctk.CTkLabel(
            self.login_frame, text='*O campo Nome do Usuário é obrigatório!', font=('Arvo', 10), text_color='#d75413')
        label_nome_usuario.grid(row=2, column=0, padx=15, pady=1)

        self.senha_usuario_login = ctk.CTkEntry(self.login_frame, placeholder_text=(
            'Senha do Usuário'), font=('Arvo', 14), width=300, show='*', corner_radius=15, border_color="#d75413")
        self.senha_usuario_login.grid(row=3, column=0, padx=15, pady=10)

        label_senha_usuario = ctk.CTkLabel(
            self.login_frame, text='*O campo Senha do Usuário é obrigatório!', font=('Arvo', 10), text_color='#d75413')
        label_senha_usuario.grid(row=4, column=0, padx=15, pady=1)

        self.marcador_checagem_senha_login = ctk.CTkCheckBox(
            self.login_frame, text='Mostrar senha.', font=('Arvo', 14), corner_radius=20)
        self.marcador_checagem_senha_login.grid(
            row=5, column=0, padx=10, pady=1)

        self.botao_login = ctk.CTkButton(
            self.login_frame, text='LOGIN', width=300, font=('Arvo', 16), fg_color='#d75413', hover_color='#ff8000', corner_radius=15, command=self.verificar_login)
        self.botao_login.grid(row=6, column=0, padx=15, pady=15)

        self.label_resgistro = ctk.CTkLabel(
            self.login_frame, text='Faça sua conta.'.upper(), font=('Arvo', 12))
        self.label_resgistro.grid(row=7, column=0, padx=15, pady=5)

        self.botao_cadastro = ctk.CTkButton(self.login_frame, text='Cadastro', width=180,
                                            fg_color='#d75413', hover_color='#ff8000', font=('Arvo bold', 14), corner_radius=20, command=self.elementos_de_janela_cadastro)
        self.botao_cadastro.grid(row=8, column=0, padx=10, pady=5)

    def elementos_de_janela_cadastro(self):
        # Remover janela de login
        self.login_frame.place_forget()
        # Criando janela de cadastro so Usuário

        self.cadastro_frame = ctk.CTkFrame(self, width=350, height=396)
        self.cadastro_frame.place(x=347, y=2)

        # frame do formulário de cadastro

        self.nome_frame_registro = ctk.CTkLabel(self.cadastro_frame, text=(
            'Registro no sistema'), font=('Arvo', 20))
        self.nome_frame_registro.grid(row=0, column=0, padx=10, pady=5)

        self.frase_obrigatoria = ctk.CTkLabel(self.cadastro_frame, text=(
            'Insira todos os dados corretos.'), font=('Arvo', 15), text_color='#d75413')
        self.frase_obrigatoria.grid(row=1, column=0, padx=10, pady=5)

        self.nome_usuario_registro = ctk.CTkEntry(self.cadastro_frame, placeholder_text=(
            'Nome do Usuário'), font=('Arvo', 14), width=300, corner_radius=15, border_color="#d75413")
        self.nome_usuario_registro.grid(row=2, column=0, padx=10, pady=2)

        self.email_usuario_registro = ctk.CTkEntry(self.cadastro_frame, placeholder_text=(
            'E-mail do Usuário'), font=('Arvo', 14), width=300, corner_radius=15, border_color="#d75413")
        self.email_usuario_registro.grid(row=3, column=0, padx=10, pady=2)

        self.senha_usuario_registro = ctk.CTkEntry(self.cadastro_frame, placeholder_text=(
            'Senha do Usuário'), font=('Arvo', 14), width=300, show='*', corner_radius=15, border_color="#d75413")
        self.senha_usuario_registro.grid(row=4, column=0, padx=10, pady=2)

        self.confirme_senha_registro = ctk.CTkEntry(self.cadastro_frame, placeholder_text=(
            'Confirme Senha'), font=('Arvo', 14), width=300, show='*', corner_radius=15, border_color="#d75413")
        self.confirme_senha_registro.grid(row=5, column=0, padx=10, pady=2)

        self.marcador_checagem = ctk.CTkCheckBox(
            self.cadastro_frame, text='Mostrar senha.', corner_radius=20)
        self.marcador_checagem.grid(row=6, column=0, padx=10, pady=5)

        self.voltar_janela = ctk.CTkButton(self.cadastro_frame, text='Voltar', width=145,
                                           fg_color='gray', hover_color='#989a91', command=self.elementos_janela_basica, font=('Arvo bold', 14), corner_radius=15)
        self.voltar_janela.grid(row=8, column=0, padx=10, pady=15)

        self.salvar_registro = ctk.CTkButton(self.cadastro_frame, text='Cadastro', width=300,
                                             fg_color='#d75413', hover_color='#ff8000', font=('Arvo bold', 14), corner_radius=15, command=self.cadastrar_usuario_banco_dados)
        self.salvar_registro.grid(row=7, column=0, padx=10, pady=25)

    def limpa_cadastro(self):
        self.nome_usuario_registro.delete(0, END)
        self.email_usuario_registro.delete(0, END)
        self.senha_usuario_registro.delete(0, END)
        self.confirme_senha_registro.delete(0, END)

    def limpa_login(self):
        self.nome_usuario_login.delete(0, END)
        self.senha_usuario_login.delete(0, END)


if __name__ == "__main__":
    meu_aplicativo = aplicativo()
    meu_aplicativo.mainloop()
