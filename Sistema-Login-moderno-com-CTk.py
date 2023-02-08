import customtkinter as ctk



class aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Configuracao_janela_principal()

    #Configuração da janela principal
    def Configuracao_janela_principal(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(width=False, height=False)  


if __name__== "__main__":
    meu_aplicativo = aplicativo()
    meu_aplicativo.mainloop()
 