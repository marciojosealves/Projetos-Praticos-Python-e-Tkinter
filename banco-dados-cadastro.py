
import sqlite3

conexao_banco_dados = sqlite3.connect("cadastro-dados-sistema-login.db")

cursor = conexao_banco_dados.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS usuarios (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome-usuario TEXT NOT NULL,
    Email-usuario TEXT NOT NULL,
    Senha-usuario TEXT NOT NULL,
    Confirme-senha TEXT NOT NULL

) """)
#É um boa prática fazer os comandos SQL em texto de CAIXA-ALTA...

print("Conexão feita com SUCESSO!!!")
