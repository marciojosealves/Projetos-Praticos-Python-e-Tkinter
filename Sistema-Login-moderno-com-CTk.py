import customtkinter as ctk
from tkinter import PhotoImage


class aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Configuracao_janela_principal()
        self.elementos_janela_basica()

    # Configuração da janela principal
    def Configuracao_janela_principal(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(width=False, height=False)

    def elementos_janela_basica(self):
        # Parte de trabalho relativa a imagem da tela.
        self.imagem_janela = PhotoImage(file="logo-mjamf.png")

        # text = None ou '' para retirar o CTkLabel
        self.label_imagem_janela = ctk.CTkLabel(
            self, image=self.imagem_janela, text=None).place(x=45, y=100)

        # Título da janela
        self.label_titulo = ctk.CTkLabel(self, text='Entre no Sistema no MJAMF\n para Login ou cadstro.', font=(
            'Arvo bold', 18), text_color='#d75413').place(x=45, y=10)

        # frame do formulário de login
        self.login_frame = ctk.CTkFrame(self, width=350, height=396)
        self.login_frame.place(x=347, y=2)

        # Frame Widgets e elementos de inclusão de dados
        self.nome_frame = ctk.CTkLabel(self.login_frame, text=(
            'Sistema de Login'), font=('Arvo bold', 20)).place(x=90, y=45)

        self.nome_usuario_login = ctk.CTkEntry(self.login_frame, placeholder_text=(
            'Nome do Usuário'), font=('Arvo', 14), width=300, corner_radius=15, border_color="#d75413").place(x=25, y=105)
        label_nome_usuario = ctk.CTkLabel(
            self.login_frame, text='*O campo Nome do Usuário é obrigatório!', font=('Arvo', 10), text_color='#d75413').place(x=25, y=135)

        self.senha_usuario_login = ctk.CTkEntry(self.login_frame, placeholder_text=(
            'Senha do Usuário'), font=('Arvo', 14), width=300, show='*', corner_radius=15, border_color="#d75413").place(x=25, y=175)
        label_senha_usuario = ctk.CTkLabel(
            self.login_frame, text='*O campo Senha do Usuário é obrigatório!', font=('Arvo', 10), text_color='#d75413').place(x=25, y=205)

        self.marcador_checagem_senha_login = ctk.CTkCheckBox(
            self.login_frame, text='Mostrar senha.', font=('Arvo', 14), corner_radius=20).place(x=25, y=245)

        self.botao_login = ctk.CTkButton(
            self.login_frame, text='LOGIN', width=300, font=('Arvo', 16), fg_color='#d75413', hover_color='#ff8000', corner_radius=15).place(x=25, y=285)

        self.label_resgistro = ctk.CTkLabel(
            self.login_frame, text='Faça sua conta.'.upper(), font=('Arvo', 12)). place(x=25, y=325)

        self.botao_registro = ctk.CTkButton(self.login_frame, text='Cadastro', width=180,
                                            fg_color='#d75413', hover_color='#ff8000', font=('Arvo bold', 14), corner_radius=20).place(x=145, y=325)


if __name__ == "__main__":
    meu_aplicativo = aplicativo()
    meu_aplicativo.mainloop()
