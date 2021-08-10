# manager_db.py
import os
import sqlite3
import io
import datetime
import csv


class Connect(object):
    
    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo nome do banco
            print("Banco:", db_name)
            # lendo a versão do SQLite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            # imprimindo a versão do SQLite
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False
    
    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


class UsuariosDb(object):
    
    tb_name = 'usuarios'

    ''' A classe UsuariosDb representa um cliente no banco de dados. '''
    
    def __init__(self):
        self.db = Connect('usuarios.db')
        self.tb_name
    
    # create_schema
    def criar_schema(self, schema_name='sql/usuarios_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)

        try:

            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)

        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)

    ''' CREATE '''

    # insert_one_register
    #       . . .

    # insert_for_file
    #       . . .

    # insert_from_csv
    #       . . .

    # insert_with_parameter
    def inserir_com_parametros(self):
        # solicitando os dados ao usuário
        self.nome = input('Nome: ')
        self.idade = input('Idade: ')
        self.cpf = input('CPF: ')
        self.email = input('Email: ')
        self.fone = input('Fone: ')
        self.cidade = input('Cidade: ')
        self.uf = input('UF: ') or 'SP'
        date = datetime.datetime.now().isoformat(" ")
        self.criado_em = input('Criado em (%s): ' % date) or date

        try:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, (self.nome, self.idade, self.cpf, self.email, self.fone,
                  self.cidade, self.uf, self.criado_em))
            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def close_connection(self):
        self.db.close_db()


class LoteriasDb(object):
    
    def __init__(self):
        self.db = Connect('loterias.db')

    # create_schema
    def criar_schema(self, schema_name='sql/loterias_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)

        try:

            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)

        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)

    ''' CREATE '''

    def inserir_loteria(self):
        # solicitando os dados ao usuário
        self.nome 
        self.numero_concurso 
        self.data_concurso
        self.data_concurso_milliseconds 
        self.local_realizacao
        self.rateio_processamento
        self.acumulou 
        self.valor_acumulado
        self.arrecadacao_total
        self.data_proximo_concurso
        self.data_proximo_concurso_milliseconds
        self.valor_estimado_proximo_concurso
        self.valor_final_concurso_acumulado
        self.numero_final_concurso_acumulado
        self.valor_acumulado_especial
        self.nome_acumulado_especial


        #tabela loterias
        try:
            self.db.cursor.execute("""
            INSERT INTO loterias (nome, numero_concurso, data_concurso, data_concurso_milliseconds, local_realizacao, rateio_processamento, acumulou, valor_acumulado, 
            arrecadacao_total, data_proximo_concurso, data_proximo_concurso_milliseconds, valor_estimado_proximo_concurso, valor_final_concurso_acumulado, numero_final_concurso_acumulado, 
            valor_acumulado_especial, nome_acumulado_especial)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (self.nome, self.numero_concurso, self.data_concurso, self.data_concurso_milliseconds, self.local_realizacao,self.rateio_processamento, self.acumulou, 
            self.valor_acumulado, self.arrecadacao_total, self.data_proximo_concurso, self.data_proximo_concurso_milliseconds, self.valor_estimado_proximo_concurso, 
            self.valor_final_concurso_acumulado, self.numero_final_concurso_acumulado, self.valor_acumulado_especial, self.nome_acumulado_especial))

            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")

        except sqlite3.IntegrityError:
            print("Aviso: O numero do concurso deve ser único.")
            return False

    #tabela dezenas
    def inserir_dezenas(self):
        self.numero_concurso
        self.dezena

        try:
            self.db.cursor.execute("""
            INSERT INTO dezenas (numero_concurso, dezena)
            VALUES (?,?)
            """, (self.numero_concurso, self.dezena))

            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
            
        except sqlite3.IntegrityError:
            print("Aviso: A dezena deve ser única.")
            return False
        

    #tabela premiacao
    def inserir_premiacao(self):
        self.nome
        self.numero_concurso
        self.quantidade_ganhadores
        self.valor_total
        self.acertos

        try:
            self.db.cursor.execute("""
            INSERT INTO premiacao (nome, numero_concurso, quantidade_ganhadores, valor_total, acertos)
            VALUES (?,?,?,?)
            """, (self.nome, self.numero_concurso ,self.quantidade_ganhadores, self.valor_total, self.acertos))

            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
            
        except sqlite3.IntegrityError:
            print("Aviso: A dezena deve ser única.")
            return False


    #tabela local_ganhadores
    def inserir_local_ganhadores(self):
        self.local
        self.numero_concurso
        self.cidade
        self.uf
        self.quantidade_ganhadores
        self.canal_eletronico

        try:
            self.db.cursor.execute("""
            INSERT INTO local_ganhadores (local, numero_concurso, cidade, uf, quantidade_ganhadores, canal_eletronico)
            VALUES (?,?,?,?,?)
            """, (self.local, self.numero_concurso, self.cidade, self.uf, self.quantidade_ganhadores, self.canal_eletronico))

            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
            
        except sqlite3.IntegrityError:
            print("Aviso: A dezena deve ser única.")
            return False

    def close_connection(self):
        self.db.close_db()

    def ler_todas_loterias(self):
        sql = 'SELECT * FROM loterias INNER JOIN dezenas ON loterias.dezena_id = dezenas.id'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_todas_pessoas(self):
        lista = self.ler_todas_pessoas()
        for c in lista:
            print(c)


if __name__ == '__main__':
    #c = UsuariosDb()
    c = LoteriasDb()
    c.criar_schema()