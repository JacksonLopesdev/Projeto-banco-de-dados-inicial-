import sqlite3

class Produtos:
    def __init__(self, quantidade, nome_produto, preco_pago, nome_fornecedor, preco_venda, data_adicao):
        self.quantidade = quantidade
        self.nome_produto = nome_produto
        self.preco_pago = preco_pago
        self.nome_fornecedor = nome_fornecedor
        self.preco_venda = preco_venda
        self.data_adicao = data_adicao  

    @staticmethod
    def conectar_bd():
        return sqlite3.connect('produtos.db')

    @staticmethod
    def criar_tabela_produtos():
        with Produtos.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Produtos (
                    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_produto TEXT NOT NULL,
                    quantidade INTEGER,
                    preco_pago REAL,
                    nome_fornecedor TEXT,
                    preco_venda REAL,
                    data_adicao TEXT
                )
            ''')
            conn.commit()

    @staticmethod
    def cadastrar_produto(quantidade, nome_produto, preco_pago, nome_fornecedor, preco_venda, data_adicao):
        with Produtos.conectar_bd() as conn:
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Produtos (nome_produto, quantidade, preco_pago, nome_fornecedor, preco_venda, data_adicao)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nome_produto, quantidade, preco_pago, nome_fornecedor, preco_venda, data_adicao))

            conn.commit()

    @staticmethod
    def editar_produto(produto):
        with sqlite3.connect('produtos.db') as conn:
            cursor = conn.cursor()

            cursor.execute('''
                UPDATE Produtos SET
                quantidade = ?,
                preco_pago = ?,
                nome_fornecedor = ?,
                preco_venda = ?,
                data_adicao = ?
                WHERE nome_produto = ?
            ''', (produto.quantidade, produto.preco_pago, produto.nome_fornecedor,
                    produto.preco_venda, produto.data_adicao, produto.nome_produto))

            conn.commit()

    @staticmethod
    def buscar_produto_por_nome(nome_produto):
        with Produtos.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Produtos WHERE nome_produto = ?
            ''', (nome_produto,))
            produto = cursor.fetchone()
            return produto

    @staticmethod
    def listar_produtos():
        with sqlite3.connect('produtos.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Produtos
            ''')
            produtos = cursor.fetchall()
            return produtos

    @staticmethod
    def deletar_produto(nome_produto, quantidade):
        with Produtos.conectar_bd() as conn:
            cursor = conn.cursor()
            # Verifica se há a quantidade desejada do produto antes de excluir
            cursor.execute('''
                SELECT quantidade FROM Produtos WHERE nome_produto = ?
            ''', (nome_produto,))
            produto = cursor.fetchone()
            if produto:
                quantidade_atual = produto[0]
                if quantidade_atual > quantidade:
                    cursor.execute('''
                        UPDATE Produtos SET quantidade = quantidade - ? WHERE nome_produto = ?
                    ''', (quantidade, nome_produto))
                    conn.commit()
                elif quantidade_atual == quantidade:
                    # Se a quantidade atual é igual à quantidade desejada, exclui o produto completamente
                    cursor.execute('''
                        DELETE FROM Produtos WHERE nome_produto = ?
                    ''', (nome_produto,))
                    conn.commit()
                else:
                    raise ValueError(f"Produto '{nome_produto}' não possui {quantidade} unidades para exclusão.")
            else:
                raise ValueError(f"Produto '{nome_produto}' não encontrado.")


class Vendas:
    def __init__(self, id_venda, quantidade_vendida, nome_produto, nome_cliente, preco_venda, data_venda):
        self.id_venda = id_venda
        self.quantidade_vendida = quantidade_vendida
        self.nome_produto = nome_produto
        self.nome_cliente = nome_cliente
        self.preco_venda = preco_venda
        self.data_venda = data_venda

    @staticmethod
    def conectar_bd():
        return sqlite3.connect('produtos.db')

    @staticmethod
    def criar_tabela_vendas():
        with Vendas.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Vendas (
                    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                    quantidade_vendida INTEGER,
                    nome_produto TEXT,
                    nome_cliente TEXT,
                    preco_venda REAL,
                    data_venda TEXT 
                )
            ''')
            conn.commit()
    
    @staticmethod
    def criar_venda(quantidade_vendida, nome_produto, nome_cliente, preco_venda, data_venda=None):
        try:
            with Vendas.conectar_bd() as conn:
                cursor = conn.cursor()

                # Verifica se há quantidade suficiente do produto em estoque
                cursor.execute('SELECT quantidade FROM Produtos WHERE nome_produto = ?', (nome_produto,))
                produto = cursor.fetchone()

                if not produto:
                    raise ValueError(f"Produto '{nome_produto}' não encontrado.")

                quantidade_atual = produto[0]
                if quantidade_atual < quantidade_vendida:
                    raise ValueError(f"Quantidade insuficiente do produto '{nome_produto}' em estoque.")

                # Cria a venda na tabela Vendas
                if data_venda is None:
                    cursor.execute('''
                        INSERT INTO Vendas (quantidade_vendida, nome_produto, nome_cliente, preco_venda)
                        VALUES (?, ?, ?, ?)
                    ''', (quantidade_vendida, nome_produto, nome_cliente, preco_venda))
                else:
                    cursor.execute('''
                        INSERT INTO Vendas (quantidade_vendida, nome_produto, nome_cliente, preco_venda, data_venda)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (quantidade_vendida, nome_produto, nome_cliente, preco_venda, data_venda))

                # Atualiza a quantidade do produto no estoque na tabela Produtos
                cursor.execute('UPDATE Produtos SET quantidade = quantidade - ? WHERE nome_produto = ?', (quantidade_vendida, nome_produto))

                conn.commit()

        except Exception as e:
            raise ValueError(f"Erro ao criar venda: {str(e)}")

    @staticmethod
    def listar_vendas():
        with Vendas.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Vendas')
            vendas = cursor.fetchall()
            lista_vendas = []
            for venda in vendas:
                lista_vendas.append(Vendas(*venda))  # Aqui, *venda desempacota os valores da tupla
            return lista_vendas

    @staticmethod
    def buscar_venda_por_nome_produto(nome_produto):
        with Vendas.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Vendas WHERE nome_produto = ?
            ''', (nome_produto,))
            venda = cursor.fetchone()
            return venda

    @staticmethod
    def atualizar_venda(id_venda, nova_quantidade_vendida, nome_produto, nome_cliente, preco_venda, nova_data_venda=None):
        with Vendas.conectar_bd() as conn:
            cursor = conn.cursor()

            # Buscar a quantidade original vendida para a venda com id_venda
            cursor.execute('SELECT quantidade_vendida, nome_produto FROM Vendas WHERE id_venda = ?', (id_venda,))
            resultado = cursor.fetchone()

            if not resultado:
                raise ValueError(f'Venda com id {id_venda} não encontrada.')

            quantidade_original = resultado[0]
            produto_vendido = resultado[1]

            # Verificar se a nova quantidade vendida é maior que a original
            if nova_quantidade_vendida > quantidade_original:
                # Verificar se há estoque suficiente para aumentar a quantidade vendida
                cursor.execute('SELECT quantidade FROM Produtos WHERE nome_produto = ?', (produto_vendido,))
                resultado_produto = cursor.fetchone()

                if not resultado_produto or resultado_produto[0] < (nova_quantidade_vendida - quantidade_original):
                    raise ValueError(f'Não há estoque suficiente para aumentar a venda para {nova_quantidade_vendida} unidades.')

            # Atualizar a venda na tabela Vendas
            if nova_data_venda is None:
                cursor.execute('''
                    UPDATE Vendas SET quantidade_vendida = ?, nome_produto = ?, nome_cliente = ?, preco_venda = ?
                    WHERE id_venda = ?
                ''', (nova_quantidade_vendida, nome_produto, nome_cliente, preco_venda, id_venda))
            else:
                cursor.execute('''
                    UPDATE Vendas SET quantidade_vendida = ?, nome_produto = ?, nome_cliente = ?, preco_venda = ?, data_venda = ?
                    WHERE id_venda = ?
                ''', (nova_quantidade_vendida, nome_produto, nome_cliente, preco_venda, nova_data_venda, id_venda))

            # Se a nova quantidade vendida for menor que a original, adicionar a diferença ao estoque
            if nova_quantidade_vendida < quantidade_original:
                cursor.execute('UPDATE Produtos SET quantidade = quantidade + ? WHERE nome_produto = ?', 
                            (quantidade_original - nova_quantidade_vendida, produto_vendido))

            # Se a nova quantidade vendida for maior que a original, diminuir a diferença do estoque
            elif nova_quantidade_vendida > quantidade_original:
                cursor.execute('UPDATE Produtos SET quantidade = quantidade - ? WHERE nome_produto = ?', 
                            (nova_quantidade_vendida - quantidade_original, produto_vendido))

            conn.commit()

    @staticmethod
    def reverter_venda(id_venda, nome_produto, quantidade_vendida):
        with Vendas.conectar_bd() as conn:
            cursor = conn.cursor()

            # Atualiza a quantidade de produtos
            cursor.execute('UPDATE Produtos SET quantidade = quantidade + ? WHERE nome_produto = ?', (quantidade_vendida, nome_produto))

            # Exclui a venda
            cursor.execute('DELETE FROM Vendas WHERE id_venda = ?', (id_venda,))
            
            conn.commit()

    @staticmethod
    def deletar_venda(nome_produto):
        with Vendas.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM Vendas WHERE nome_produto = ?
            ''', (nome_produto,))
            conn.commit()


class Clientes:
    def __init__(self, nome_cliente, telefone, endereco_cliente, cpf):
        self.nome_cliente = nome_cliente
        self.telefone = telefone
        self.endereco_cliente = endereco_cliente
        self.cpf = cpf

    @staticmethod
    def conectar_bd():
        return sqlite3.connect('produtos.db')  # Alterado para produtos.db

    @staticmethod
    def criar_tabela_clientes():
        with Clientes.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Clientes (
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cliente TEXT NOT NULL,
                    telefone TEXT,
                    endereco TEXT,
                    cpf TEXT UNIQUE
                )
            ''')
            conn.commit()

    @staticmethod
    def cadastrar_cliente(nome_cliente, telefone, endereco_cliente, cpf):
        with Clientes.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Clientes (nome_cliente, telefone, endereco, cpf)
                VALUES (?, ?, ?, ?)
            ''', (nome_cliente, telefone, endereco_cliente, cpf))
            conn.commit()

    @staticmethod
    def buscar_cliente_por_nome(nome_cliente):
        with Clientes.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Clientes WHERE nome_cliente = ?
            ''', (nome_cliente,))
            cliente = cursor.fetchone()
            return cliente

    @staticmethod
    def atualizar_cliente_por_nome(nome_cliente, novo_nome, novo_telefone, novo_endereco, novo_cpf):
        with Clientes.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Clientes SET nome_cliente = ?, telefone = ?, endereco = ?, cpf = ?
                WHERE nome_cliente = ?
            ''', (novo_nome, novo_telefone, novo_endereco, novo_cpf, nome_cliente))
            conn.commit()

    @staticmethod
    def deletar_cliente(nome_cliente):
        with Clientes.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM Clientes WHERE nome_cliente = ?
            ''', (nome_cliente,))
            conn.commit()

    @staticmethod
    def listar_clientes():
        with Clientes.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nome_cliente, telefone, endereco, cpf FROM Clientes')
            clientes = cursor.fetchall()

            lista_clientes = []
            for cliente in clientes:
                nome_cliente, telefone, endereco, cpf = cliente
                lista_clientes.append(Clientes(nome_cliente, telefone, endereco, cpf))

            return lista_clientes


class Fornecedor:
    def __init__(self, nome_fornecedor, telefone, endereco_fornecedor, cnpj):
        self.nome_fornecedor = nome_fornecedor
        self.telefone = telefone
        self.endereco_fornecedor = endereco_fornecedor
        self.cnpj = cnpj

    @staticmethod
    def conectar_bd():
        return sqlite3.connect('produtos.db')  # Alterado para produtos.db

    @staticmethod
    def criar_tabela_fornecedores():
        with Fornecedor.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Fornecedores (
                    id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_fornecedor TEXT NOT NULL,
                    telefone TEXT,
                    endereco TEXT,
                    cnpj TEXT UNIQUE
                )
            ''')
            conn.commit()

    @staticmethod
    def cadastrar_fornecedor(nome_fornecedor, telefone, endereco_fornecedor, cnpj):
        with Fornecedor.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Fornecedores (nome_fornecedor, telefone, endereco, cnpj)
                VALUES (?, ?, ?, ?)
            ''', (nome_fornecedor, telefone, endereco_fornecedor, cnpj))
            conn.commit()

    @staticmethod
    def buscar_fornecedor_por_nome(nome_fornecedor):
        with Fornecedor.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM Fornecedores WHERE nome_fornecedor = ?
            ''', (nome_fornecedor,))
            fornecedor = cursor.fetchone()
            return fornecedor

    @staticmethod
    def atualizar_fornecedor_por_nome(nome_fornecedor, novo_nome, novo_telefone, novo_endereco, novo_cnpj):
        with Fornecedor.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Fornecedores SET nome_fornecedor = ?, telefone = ?, endereco = ?, cnpj = ?
                WHERE nome_fornecedor = ?
            ''', (novo_nome, novo_telefone, novo_endereco, novo_cnpj, nome_fornecedor))
            conn.commit()

    @staticmethod
    def listar_fornecedores():
        with Fornecedor.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id_fornecedor, nome_fornecedor, telefone, endereco, cnpj FROM Fornecedores
            ''')
            fornecedores = cursor.fetchall()

            lista_fornecedores = []
            for fornecedor in fornecedores:
                id_fornecedor, nome_fornecedor, telefone, endereco, cnpj = fornecedor
                lista_fornecedores.append(Fornecedor(nome_fornecedor, telefone, endereco, cnpj))  # Criando objetos Fornecedor com os dados retornados

            return lista_fornecedores

    @staticmethod
    def deletar_fornecedor(nome_fornecedor):
        with Fornecedor.conectar_bd() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM Fornecedores WHERE nome_fornecedor = ?
            ''', (nome_fornecedor,))
            conn.commit()