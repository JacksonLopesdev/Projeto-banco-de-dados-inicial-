import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from main import Produtos, Vendas, Clientes, Fornecedor
import sqlite3
from customtkinter import CTkEntry, CTkLabel
from PIL import Image
from datetime import datetime

    # icones
imagem_de_salvar = ctk.CTkImage(dark_image=Image.open('icones\\icone_salvar.png'), light_image=Image.open('icones\\icone_salvar.png'), size=(30, 30))
imagem_de_cadastrar = ctk.CTkImage(dark_image=Image.open('icones\\icone_cadastrar.png'), light_image=Image.open('icones\\icone_cadastrar.png'), size=(30, 30))
imagem_de_editar = ctk.CTkImage(dark_image=Image.open('icones\\icone_editar.png'), light_image=Image.open('icones\\icone_editar.png'), size=(30, 30))
imagem_de_listar = ctk.CTkImage(dark_image=Image.open('icones\\icone_listar.png'), light_image=Image.open('icones\\icone_listar.png'), size=(30, 30))
imagem_de_iniciar = ctk.CTkImage(dark_image=Image.open('icones\\icone_iniciar.png'), light_image=Image.open('icones\\icone_iniciar.png'), size=(30, 30))

#logica de autocompletar, apenas aparece abaixo da label, e nao da pra clicar
class AutocompleteEntry_produtos(CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.autocomplete)
        self.bind("<FocusOut>", self.fechar_autocomplete)
        self.autocomplete_label = None  # Para mostrar as sugestões

    def autocomplete(self, event):
        texto = self.get().strip()
        if texto:
            produtos = self.buscar_produtos(texto)
            if produtos:
                self.mostrar_autocomplete(produtos)
        else:
            self.fechar_autocomplete()

    def buscar_produtos(self, entrada):
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome_produto FROM Produtos WHERE nome_produto LIKE ?", ('%' + entrada + '%',))
        produtos = [produto[0] for produto in cursor.fetchall()]
        conn.close()
        return produtos

    def mostrar_autocomplete(self, produtos):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()

        self.autocomplete_label = CTkLabel(self.master, text='\n'.join(produtos), text_color= 'black', justify='left', anchor='w')
        self.autocomplete_label.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())

    def fechar_autocomplete(self, event=None):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()


class AutocompleteEntry_clientes(CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.autocomplete)
        self.bind("<FocusOut>", self.fechar_autocomplete)
        self.autocomplete_label = None 

    def autocomplete(self, event):
        texto = self.get().strip()
        if texto:
            produtos = self.buscar_cliente(texto)
            if produtos:
                self.mostrar_autocomplete(produtos)
        else:
            self.fechar_autocomplete()

    def buscar_cliente(self, entrada):
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome_cliente FROM Clientes WHERE nome_cliente LIKE ?", ('%' + entrada + '%',))
        clientes = [cliente[0] for cliente in cursor.fetchall()]
        conn.close()
        return clientes

    def mostrar_autocomplete(self, clientes):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()

        self.autocomplete_label = CTkLabel(self.master, text='\n'.join(clientes), text_color= 'black', justify='left', anchor='w')
        self.autocomplete_label.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())

    def fechar_autocomplete(self, event=None):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()


class AutocompleteEntry_fornecedores(CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.autocomplete)
        self.bind("<FocusOut>", self.fechar_autocomplete)
        self.autocomplete_label = None 

    def autocomplete(self, event):
        texto = self.get().strip()
        if texto:
            fornecedores = self.buscar_fornecedor(texto)
            if fornecedores:
                self.mostrar_autocomplete(fornecedores)
        else:
            self.fechar_autocomplete()

    def buscar_fornecedor(self, entrada):
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome_fornecedor FROM Fornecedores WHERE nome_fornecedor LIKE ?", ('%' + entrada + '%',))
        fornecedores = [fornecedor[0] for fornecedor in cursor.fetchall()]
        conn.close()
        return fornecedores

    def mostrar_autocomplete(self, fornecedores):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()

        self.autocomplete_label = CTkLabel(self.master, text='\n'.join(fornecedores), text_color= 'black', justify='left', anchor='w')
        self.autocomplete_label.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())

    def fechar_autocomplete(self, event=None):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()


class AutocompleteEntry_vendas(CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.autocomplete)
        self.bind("<FocusOut>", self.fechar_autocomplete)
        self.autocomplete_label = None  # Para mostrar as sugestões

    def autocomplete(self, event):
        texto = self.get().strip()
        if texto:
            vendas = self.buscar_venda(texto)
            if vendas:
                self.mostrar_autocomplete(vendas)
        else:
            self.fechar_autocomplete()

    def buscar_venda(self, entrada):
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome_produto FROM Vendas WHERE nome_produto LIKE ?", ('%' + entrada + '%',))
        vendas = [venda[0] for venda in cursor.fetchall()]  # Ajustado para acessar o índice 0 (nome_produto)
        conn.close()
        return vendas


    def mostrar_autocomplete(self, vendas):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()

        self.autocomplete_label = CTkLabel(self.master, text='\n'.join(vendas), text_color= 'black', justify='left', anchor='w')
        self.autocomplete_label.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())

    def fechar_autocomplete(self, event=None):
        if self.autocomplete_label:
            self.autocomplete_label.destroy()

# mensagem de sucesso
def mostrar_mensagem(titulo, mensagem):
    Messagebox = CTkMessagebox(title=titulo, icon="check", message=mensagem)

# mensagem de erro
def mostrar_erro(titulo, mensagem):
    Messagebox = CTkMessagebox(title=titulo, icon="cancel", message=mensagem,)

#funcao para cadastro de produtos
def cadastrar_produto():
    cadastro_produto = ctk.CTk(fg_color= 'darkgray')
    cadastro_produto.title("Cadastro de Produtos")
    cadastro_produto.geometry("400x400")

 
    label_nome_produto = ctk.CTkLabel(cadastro_produto, text="Nome do Produto:", text_color= 'black')
    label_nome_produto.pack()

    entry_nome_produto = ctk.CTkEntry(cadastro_produto, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_produto.pack()

    label_quantidade = ctk.CTkLabel(cadastro_produto, text="Quantidade:", text_color= 'black')
    label_quantidade.pack()

    entry_quantidade = ctk.CTkEntry(cadastro_produto, width= 300, placeholder_text= "Exemplo: 5")
    entry_quantidade.pack()

    label_preco_pago = ctk.CTkLabel(cadastro_produto, text="Preço Pago:", text_color= 'black')
    label_preco_pago.pack()

    entry_preco_pago = ctk.CTkEntry(cadastro_produto, width= 300, placeholder_text= "EXEMPLO: XX.XX")
    entry_preco_pago.pack()

    label_nome_fornecedor = ctk.CTkLabel(cadastro_produto, text="Nome do Fornecedor:", text_color= 'black')
    label_nome_fornecedor.pack()

    entry_nome_fornecedor = ctk.CTkEntry(cadastro_produto, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_fornecedor.pack()

    label_preco_venda = ctk.CTkLabel(cadastro_produto, text="Preço de Venda:", text_color= 'black')
    label_preco_venda.pack()

    entry_preco_venda = ctk.CTkEntry(cadastro_produto, width= 300, placeholder_text= "EXEMPLO: XX.XX")
    entry_preco_venda.pack()

    def salvar_produto():
        try:
            nome_produto = entry_nome_produto.get().strip().lower()
            quantidade = int(entry_quantidade.get().strip())
            preco_pago = float(entry_preco_pago.get().strip())
            nome_fornecedor = entry_nome_fornecedor.get().strip().lower()
            preco_venda = float(entry_preco_venda.get().strip())
            data_adicao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if not nome_produto or quantidade <= 0 or preco_pago <= 0 or preco_venda <= 0:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            Produtos.criar_tabela_produtos() 
            Produtos.cadastrar_produto(quantidade, nome_produto, preco_pago, nome_fornecedor, preco_venda, data_adicao)

            mostrar_mensagem("Cadastro de Produto", f"Produto '{nome_produto}' cadastrado com sucesso!")
            cadastro_produto.destroy()  # Fechar a janela de cadastro após sucesso

        except ValueError:
            mostrar_erro("Erro de Valor", "Verifique se os campos numéricos estão preenchidos corretamente.")
        except Exception as e:
            mostrar_erro("Erro ao cadastrar produto", f"Erro: {str(e)}")

    button_cadastrar = ctk.CTkButton(cadastro_produto, text="Cadastrar Produto", text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=salvar_produto)
    button_cadastrar.pack(pady=10)

    cadastro_produto.mainloop()

#funcao para a edicao de produtos
def editar_produto():
    editar_produto_janela = ctk.CTk(fg_color= 'darkgray')
    editar_produto_janela.title("Editar Produto")
    editar_produto_janela.geometry("400x450")

    label_nome_produto = ctk.CTkLabel(editar_produto_janela, text="Nome do Produto:", text_color= 'black')
    label_nome_produto.pack()

    entry_nome_produto = AutocompleteEntry_produtos(editar_produto_janela, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_produto.pack()

    label_quantidade = ctk.CTkLabel(editar_produto_janela, text="Quantidade:", text_color= 'black')
    label_quantidade.pack()

    entry_quantidade = ctk.CTkEntry(editar_produto_janela, width= 300, placeholder_text= "Exemplo: 5")
    entry_quantidade.pack()

    label_preco_pago = ctk.CTkLabel(editar_produto_janela, text="Preço Pago:", text_color= 'black')
    label_preco_pago.pack()

    entry_preco_pago = ctk.CTkEntry(editar_produto_janela, width= 300, placeholder_text= "EXEMPLO: XX.XX")
    entry_preco_pago.pack()

    label_nome_fornecedor = ctk.CTkLabel(editar_produto_janela, text="Nome do Fornecedor:", text_color= 'black')
    label_nome_fornecedor.pack()

    entry_nome_fornecedor = ctk.CTkEntry(editar_produto_janela, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_fornecedor.pack()

    label_preco_venda = ctk.CTkLabel(editar_produto_janela, text="Preço de Venda:", text_color= 'black')
    label_preco_venda.pack()

    entry_preco_venda = ctk.CTkEntry(editar_produto_janela, width= 300, placeholder_text= "EXEMPLO: XX.XX")
    entry_preco_venda.pack()

    def buscar_e_preencher_dados():
        nome_produto = entry_nome_produto.get().strip().lower()

        produto = Produtos.buscar_produto_por_nome(nome_produto)

        if produto:
            entry_quantidade.delete(0, "end")
            entry_quantidade.insert(0, produto[2])  

            entry_preco_pago.delete(0, "end")
            entry_preco_pago.insert(0, produto[3])  

            entry_nome_fornecedor.delete(0, "end")
            entry_nome_fornecedor.insert(0, produto[4])  

            entry_preco_venda.delete(0, "end")
            entry_preco_venda.insert(0, produto[5])  
        else:
            mostrar_erro("Produto não encontrado", f"Produto '{nome_produto}' não encontrado.")

    def salvar_edicao():
        try:
            nome_produto = entry_nome_produto.get().strip().lower()
            quantidade = int(entry_quantidade.get().strip())
            preco_pago = float(entry_preco_pago.get().strip())
            nome_fornecedor = entry_nome_fornecedor.get().strip().lower()
            preco_venda = float(entry_preco_venda.get().strip())
            data_adicao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if quantidade <= 0 or preco_pago <= 0 or preco_venda <= 0:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            produto = Produtos(quantidade, nome_produto, preco_pago, nome_fornecedor, preco_venda, data_adicao)
            Produtos.editar_produto(produto)

            mostrar_mensagem("Produto Editado", f"Produto '{nome_produto}' editado com sucesso!")
            editar_produto_janela.destroy()  # Fechar a janela de edição após sucesso

        except ValueError:
            mostrar_erro("Erro de Valor", "Verifique se os campos numéricos estão preenchidos corretamente.")
        except Exception as e:
            mostrar_erro("Erro ao editar produto", f"Erro: {str(e)}")

    def abrir_janela_exclusao():
        nome_produto = entry_nome_produto.get().strip().lower()
        quantidade_produto = entry_quantidade.get().strip()

        if not nome_produto:
            mostrar_erro("Erro de Validação", "Preencha o campo Nome do Produto.")
            return
        
        if not quantidade_produto:
            mostrar_erro("Erro de Validação", "Digite a quantidade a ser excluída.")
            return
        
        try:
            quantidade_produto = int(quantidade_produto)
            if quantidade_produto <= 0:
                mostrar_erro("Erro de Validação", "A quantidade a ser excluída deve ser um número maior que zero.")
                return
            
            janela_exclusao = ctk.CTk(fg_color= 'darkgray')
            janela_exclusao.title("Confirmação de Exclusão")
            janela_exclusao.geometry("400x200")

            label_confirmar = ctk.CTkLabel(janela_exclusao, text=f"Tem certeza que deseja excluir {quantidade_produto} unidade(s) do produto '{nome_produto}'?", text_color= 'black')
            label_confirmar.pack(pady=10)

            label_quantidade_excluir = ctk.CTkLabel(janela_exclusao, text="Quantidade a Excluir:", text_color= 'black')
            label_quantidade_excluir.pack()

            entry_quantidade_excluir = ctk.CTkEntry(janela_exclusao)
            entry_quantidade_excluir.pack()

            def confirmar_exclusao():
                try:
                    quantidade_excluir = int(entry_quantidade_excluir.get())
                    Produtos.deletar_produto(nome_produto, quantidade_excluir)
                    mostrar_mensagem("Produto Excluído", f"{quantidade_excluir} unidades do produto '{nome_produto}' foram excluídas com sucesso!")
                    janela_exclusao.destroy()  
                    editar_produto_janela.destroy()  
                except ValueError as e:
                    mostrar_erro("Erro ao excluir produto", str(e))
                except Exception as e:
                    mostrar_erro("Erro ao excluir produto", f"Erro: {str(e)}")

            button_confirmar = ctk.CTkButton(janela_exclusao, text="Confirmar",
                                             text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=confirmar_exclusao)
            button_confirmar.pack(pady=10)

            janela_exclusao.mainloop()

        except ValueError:
            mostrar_erro("Erro de Validação", "Digite um número válido para a quantidade a ser excluída.")
        except Exception as e:
            mostrar_erro("Erro ao abrir janela de exclusão", f"Erro: {str(e)}")

    button_buscar = ctk.CTkButton(editar_produto_janela, text="Buscar Produto",
                                  text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=buscar_e_preencher_dados)
    button_buscar.pack(pady=10)

    button_salvar = ctk.CTkButton(editar_produto_janela, text="Salvar Edição",
                                  text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=salvar_edicao)
    button_salvar.pack(pady=10)

    button_excluir = ctk.CTkButton(editar_produto_janela, text="Excluir Produto",
                                   text_color= 'black',
                                    fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                    hover_color= 'white', command=abrir_janela_exclusao)
    button_excluir.pack(pady=10)

    editar_produto_janela.mainloop()

#funcao para listar produtos, irei adicionar uma logica para separar por data !, e colocar um top 10 talvez, fica mais pra frente
def listar_produtos():
    listar_produtos_janela = ctk.CTk(fg_color= 'darkgray')
    listar_produtos_janela.title("Listagem de Produtos")
    listar_produtos_janela.geometry("900x600")

    textbox_produtos = ctk.CTkTextbox(listar_produtos_janela, font=("Arial", 14),
                                       text_color= 'black', fg_color= 'white', width=900, height=500)
    textbox_produtos.pack(pady="5", padx="20")

    def preencher_lista():
        textbox_produtos.delete("1.0", "end")
        produtos = Produtos.listar_produtos()

        lista_texto = ""
        for produto in produtos:
            nome_produto = produto[1]
            quantidade = produto[2]
            preco_pago = produto[3]
            fornecedor = produto[4]
            preco_venda = produto[5]
            data_adicao = produto[6]

            lista_texto += f"Nome do produto: {nome_produto}\n"
            lista_texto += f"Quantidade: {quantidade}\n"
            lista_texto += f"Preço pago: R${preco_pago:.2f}\n"  
            lista_texto += f"Fornecedor: {fornecedor}\n"
            lista_texto += f"Preço de venda: R${preco_venda:.2f}\n" 
            lista_texto += f"Data de Adição: {data_adicao}\n\n"

        textbox_produtos.insert("1.0", lista_texto)

    preencher_lista()
    button_atualizar = ctk.CTkButton(listar_produtos_janela, text="Atualizar Lista",
                                     text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=preencher_lista)
    button_atualizar.pack()

    listar_produtos_janela.mainloop()

#funcao cadastro de cliente
def cadastrar_cliente():
    cadastro_cliente = ctk.CTk(fg_color= 'darkgray')
    cadastro_cliente.title("Cadastro de Clientes")
    cadastro_cliente.geometry("400x300")

    label_nome_cliente = ctk.CTkLabel(cadastro_cliente, text="Nome do Cliente:", text_color= 'black')
    label_nome_cliente.pack()

    entry_nome_cliente = ctk.CTkEntry(cadastro_cliente, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_cliente.pack()

    label_telefone_cliente = ctk.CTkLabel(cadastro_cliente, text="Telefone do Cliente:", text_color= 'black')
    label_telefone_cliente.pack()

    entry_telefone_cliente = ctk.CTkEntry(cadastro_cliente, width= 300, placeholder_text= "Exemplo: (XX) XXXX-XXXX")
    entry_telefone_cliente.pack()

    label_endereco_cliente = ctk.CTkLabel(cadastro_cliente, text="Endereço do Cliente:", text_color= 'black')
    label_endereco_cliente.pack()

    entry_endereco_cliente = ctk.CTkEntry(cadastro_cliente, width= 300, placeholder_text= "Rua, numero, bairro e cidade")
    entry_endereco_cliente.pack()

    label_cpf_cliente = ctk.CTkLabel(cadastro_cliente, text="CPF do Cliente:", text_color= 'black')
    label_cpf_cliente.pack()

    entry_cpf_cliente = ctk.CTkEntry(cadastro_cliente, width= 300, placeholder_text= "Exemplo: XXX.XXX.XXX-XX")
    entry_cpf_cliente.pack()

    def salvar_cliente():
        try:
            nome_cliente = entry_nome_cliente.get()
            telefone = entry_telefone_cliente.get()
            endereco = entry_endereco_cliente.get()
            cpf = entry_cpf_cliente.get()

            if not nome_cliente or not telefone or not endereco or not cpf:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            Clientes.criar_tabela_clientes()

            Clientes.cadastrar_cliente(nome_cliente, telefone, endereco, cpf)

            mostrar_mensagem("Cadastro de Cliente", f"Cliente '{nome_cliente}' cadastrado com sucesso!")
            cadastro_cliente.destroy()  # Fechar a janela de cadastro após sucesso

        except ValueError:
            mostrar_erro("Erro de Valor", "Verifique se os campos numéricos estão preenchidos corretamente.")
        except Exception as e:
            mostrar_erro("Erro ao cadastrar cliente", f"Erro: {str(e)}")

    button_cadastrar = ctk.CTkButton(cadastro_cliente, text="Cadastrar Cliente", text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=salvar_cliente)
    button_cadastrar.pack(pady=10)

    cadastro_cliente.mainloop()

#funcao de edicao de clientes
def editar_cliente():
    editar_cliente_janela = ctk.CTk(fg_color='darkgray')
    editar_cliente_janela.title("Editar Cliente")
    editar_cliente_janela.geometry("400x450")

    label_nome_cliente = ctk.CTkLabel(editar_cliente_janela, text="Nome do Cliente:", text_color='black')
    label_nome_cliente.pack()

    entry_nome_cliente = AutocompleteEntry_clientes(editar_cliente_janela, width=300, placeholder_text="Sem acentos ou pontuação")
    entry_nome_cliente.pack()

    label_telefone = ctk.CTkLabel(editar_cliente_janela, text="Telefone:", text_color='black')
    label_telefone.pack()

    entry_telefone = ctk.CTkEntry(editar_cliente_janela, width=300, placeholder_text="Exemplo: (XX) XXXX-XXXX")
    entry_telefone.pack()

    label_endereco_cliente = ctk.CTkLabel(editar_cliente_janela, text="Endereço:", text_color='black')
    label_endereco_cliente.pack()

    entry_endereco_cliente = ctk.CTkEntry(editar_cliente_janela, width=300, placeholder_text="Rua, numero, bairro e cidade")
    entry_endereco_cliente.pack()

    label_cpf = ctk.CTkLabel(editar_cliente_janela, text="CPF:", text_color='black')
    label_cpf.pack()

    entry_cpf = ctk.CTkEntry(editar_cliente_janela, width=300, placeholder_text="Exemplo: XXX.XXX.XXX-XX")
    entry_cpf.pack()

    def buscar_e_preencher_dados():
        nome_cliente = entry_nome_cliente.get().strip().lower()

        cliente = Clientes.buscar_cliente_por_nome(nome_cliente)

        if cliente:
            entry_telefone.delete(0, "end")
            entry_telefone.insert(0, cliente[2])  # telefone

            entry_endereco_cliente.delete(0, "end")
            entry_endereco_cliente.insert(0, cliente[3])  # endereco

            entry_cpf.delete(0, "end")
            entry_cpf.insert(0, cliente[4])  # cpf
        else:
            mostrar_erro("Cliente não encontrado", f"Cliente '{nome_cliente}' não encontrado.")

    def salvar_edicao():
        try:
            nome_cliente = entry_nome_cliente.get().strip().lower()
            telefone = entry_telefone.get().strip()
            endereco = entry_endereco_cliente.get().strip()
            cpf = entry_cpf.get().strip()

            if not nome_cliente or not telefone or not endereco or not cpf:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            Clientes.atualizar_cliente_por_nome(nome_cliente, nome_cliente, telefone, endereco, cpf)

            mostrar_mensagem("Cliente Editado", f"Cliente '{nome_cliente}' editado com sucesso!")
            editar_cliente_janela.destroy()  # Fechar a janela de edição após sucesso

        except Exception as e:
            mostrar_erro("Erro ao editar cliente", f"Erro: {str(e)}")

    def confirmar_exclusao():
        nome_cliente = entry_nome_cliente.get().strip().lower()
        
        janela_exclusao = ctk.CTk(fg_color='darkgray')
        janela_exclusao.title("Confirmação de Exclusão")
        janela_exclusao.geometry("400x150")

        label_confirmar = ctk.CTkLabel(janela_exclusao, text=f"Tem certeza que deseja excluir o cliente '{nome_cliente}'?", text_color='black')
        label_confirmar.pack(pady=10)

        def excluir_cliente():
            try:
                Clientes.deletar_cliente(nome_cliente)
                mostrar_mensagem("Cliente Excluído", f"Cliente '{nome_cliente}' foi excluído com sucesso!")
                janela_exclusao.destroy()
                editar_cliente_janela.destroy() 
            except Exception as e:
                mostrar_erro("Erro ao excluir cliente", f"Erro: {str(e)}")

        button_confirmar = ctk.CTkButton(janela_exclusao, text="Confirmar", text_color='black',
                                         fg_color="#5D3EBC", border_color='#ECF0F1',
                                         hover_color='white', command=excluir_cliente)
        button_confirmar.pack(pady=10)

        janela_exclusao.mainloop()

    button_buscar = ctk.CTkButton(editar_cliente_janela, text="Buscar Cliente",
                                  text_color='black',
                                  fg_color="#5D3EBC", border_color='#ECF0F1',
                                  hover_color='white', command=buscar_e_preencher_dados)
    button_buscar.pack(pady=10)

    button_salvar = ctk.CTkButton(editar_cliente_janela, text="Salvar Edição",
                                  text_color='black',
                                  fg_color="#5D3EBC", border_color='#ECF0F1',
                                  hover_color='white', command=salvar_edicao)
    button_salvar.pack(pady=10)

    button_excluir = ctk.CTkButton(editar_cliente_janela, text="Excluir Cliente",
                                   text_color='black',
                                   fg_color="#5D3EBC", border_color='#ECF0F1',
                                   hover_color='white', command=confirmar_exclusao)
    button_excluir.pack(pady=10)

    editar_cliente_janela.mainloop()

#funcao onde listo todos os clientes
def listar_clientes():
    listar_clientes_janela = ctk.CTk(fg_color='darkgray')
    listar_clientes_janela.title("Listagem de Clientes")
    listar_clientes_janela.geometry("900x600")

    textbox_clientes = ctk.CTkTextbox(listar_clientes_janela, font=("Arial", 14),
                                       text_color='black', fg_color='white', width=900, height=500)
    textbox_clientes.pack(pady="5", padx="20")

    def preencher_lista():
        textbox_clientes.delete("1.0", "end")

        clientes = Clientes.listar_clientes()

        lista_texto = ""
        for cliente in clientes:
            lista_texto += f"Nome do cliente: {cliente.nome_cliente}\n"
            lista_texto += f"Telefone: {cliente.telefone}\n"
            lista_texto += f"Endereço: {cliente.endereco_cliente}\n"
            lista_texto += f"CPF: {cliente.cpf}\n\n"

        textbox_clientes.insert("1.0", lista_texto)

    preencher_lista()

    button_atualizar = ctk.CTkButton(listar_clientes_janela, text="Atualizar Lista",
                                     text_color='black',
                                     fg_color="#5D3EBC", border_color='#ECF0F1',
                                     hover_color='white', command=preencher_lista)
    button_atualizar.pack()

    listar_clientes_janela.mainloop()

#funcao de cadastro de fornecedores
def cadastrar_fornecedor():
    cadastro_fornecedor = ctk.CTk(fg_color= 'darkgray')
    cadastro_fornecedor.title("Cadastro de Fornecedores")
    cadastro_fornecedor.geometry("400x300")

    label_nome_fornecedor = ctk.CTkLabel(cadastro_fornecedor, text="Nome do Fornecedor:", text_color= 'black')
    label_nome_fornecedor.pack()

    entry_nome_fornecedor = ctk.CTkEntry(cadastro_fornecedor, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_fornecedor.pack()

    label_telefone_fornecedor = ctk.CTkLabel(cadastro_fornecedor, text="Telefone do Fornecedor:", text_color= 'black')
    label_telefone_fornecedor.pack()

    entry_telefone_fornecedor = ctk.CTkEntry(cadastro_fornecedor, width= 300, placeholder_text= "Exemplo: (XX) XXXX-XXXX")
    entry_telefone_fornecedor.pack()

    label_endereco_fornecedor = ctk.CTkLabel(cadastro_fornecedor, text="Endereço do Fornecedor:", text_color= 'black')
    label_endereco_fornecedor.pack()

    entry_endereco_fornecedor = ctk.CTkEntry(cadastro_fornecedor, width= 300, placeholder_text= "Rua, numero, bairro e cidade")
    entry_endereco_fornecedor.pack()

    label_cnpj_fornecedor = ctk.CTkLabel(cadastro_fornecedor, text="CNPJ do Fornecedor:", text_color= 'black')
    label_cnpj_fornecedor.pack()

    entry_cnpj_fornecedor = ctk.CTkEntry(cadastro_fornecedor, width= 300, placeholder_text= "Exemplo: XXX.XXX.XXX-XX")
    entry_cnpj_fornecedor.pack()

    def salvar_fornecedor():
        try:
            nome_fornecedor = entry_nome_fornecedor.get()
            telefone = entry_telefone_fornecedor.get()
            endereco = entry_endereco_fornecedor.get()
            cnpj = entry_cnpj_fornecedor.get()

            if not nome_fornecedor or not telefone or not endereco or not cnpj:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            Fornecedor.criar_tabela_fornecedores()

            Fornecedor.cadastrar_fornecedor(nome_fornecedor, telefone, endereco, cnpj)

            mostrar_mensagem("Cadastro de Fornecedor", f"Fornecedor '{nome_fornecedor}' cadastrado com sucesso!")
            cadastro_fornecedor.destroy()
        
        except Exception as e:
            mostrar_erro("Erro ao cadastrar fornecedor", f"Erro: {str(e)}")
        
    button_cadastrar = ctk.CTkButton(cadastro_fornecedor, text="Cadastrar Fornecedor", text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=salvar_fornecedor)
    button_cadastrar.pack(pady= 10)

    cadastro_fornecedor.mainloop()

#funcao de edicao de fornecedores
def editar_fornecedor():
    editar_fornecedor_janela = ctk.CTk(fg_color='darkgray')
    editar_fornecedor_janela.title("Editar Fornecedor")
    editar_fornecedor_janela.geometry("400x450")

    label_nome_fornecedor = CTkLabel(editar_fornecedor_janela, text="Nome do Fornecedor:", text_color='black')
    label_nome_fornecedor.pack()

    entry_nome_fornecedor = AutocompleteEntry_fornecedores(editar_fornecedor_janela, width=300, placeholder_text="Sem acentos ou pontuação")
    entry_nome_fornecedor.pack()

    label_telefone = CTkLabel(editar_fornecedor_janela, text="Telefone:", text_color='black')
    label_telefone.pack()

    entry_telefone = CTkEntry(editar_fornecedor_janela, width=300, placeholder_text="Exemplo: (XX) XXXX-XXXX")
    entry_telefone.pack()

    label_endereco_fornecedor = CTkLabel(editar_fornecedor_janela, text="Endereço:", text_color='black')
    label_endereco_fornecedor.pack()

    entry_endereco_fornecedor = CTkEntry(editar_fornecedor_janela, width=300, placeholder_text="Rua, numero, bairro e cidade")
    entry_endereco_fornecedor.pack()

    label_cnpj = CTkLabel(editar_fornecedor_janela, text="CNPJ:", text_color='black')
    label_cnpj.pack()

    entry_cnpj = CTkEntry(editar_fornecedor_janela, width=300, placeholder_text="Exemplo: XX.XXX.XXX/XXXX-XX")
    entry_cnpj.pack()

    def buscar_e_preencher_dados():
        nome_fornecedor = entry_nome_fornecedor.get().strip().lower()

        try:
            fornecedor = Fornecedor.buscar_fornecedor_por_nome(nome_fornecedor)

            if fornecedor:
                id_fornecedor, nome_fornecedor, telefone, endereco, cnpj = fornecedor

                entry_telefone.delete(0, "end")
                entry_telefone.insert(0, telefone)

                entry_endereco_fornecedor.delete(0, "end")
                entry_endereco_fornecedor.insert(0, endereco)

                entry_cnpj.delete(0, "end")
                entry_cnpj.insert(0, cnpj)
            else:
                mostrar_erro("Fornecedor não encontrado", f"Fornecedor '{nome_fornecedor}' não encontrado.")

        except Exception as e:
            mostrar_erro("Erro ao buscar fornecedor", f"Erro: {str(e)}")

    def salvar_edicao():
        try:
            nome_fornecedor = entry_nome_fornecedor.get().strip().lower()
            telefone = entry_telefone.get().strip()
            endereco = entry_endereco_fornecedor.get().strip()
            cnpj = entry_cnpj.get().strip()

            if not nome_fornecedor or not telefone or not endereco or not cnpj:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            Fornecedor.atualizar_fornecedor_por_nome(nome_fornecedor, nome_fornecedor, telefone, endereco, cnpj)

            mostrar_mensagem("Fornecedor Editado", f"Fornecedor '{nome_fornecedor}' editado com sucesso!")
            editar_fornecedor_janela.destroy()  # Fechar a janela de edição após sucesso

        except Exception as e:
            mostrar_erro("Erro ao editar fornecedor", f"Erro: {str(e)}")

    def confirmar_exclusao():
        nome_fornecedor = entry_nome_fornecedor.get().strip().lower()

        janela_exclusao = ctk.CTk(fg_color='darkgray')
        janela_exclusao.title("Confirmação de Exclusão")
        janela_exclusao.geometry("400x150")

        label_confirmar = CTkLabel(janela_exclusao, text=f"Tem certeza que deseja excluir o fornecedor '{nome_fornecedor}'?", text_color='black')
        label_confirmar.pack(pady=10)

        def excluir_fornecedor():
            try:
                Fornecedor.deletar_fornecedor(nome_fornecedor)
                mostrar_mensagem("Fornecedor Excluído", f"Fornecedor '{nome_fornecedor}' foi excluído com sucesso!")
                janela_exclusao.destroy()
                editar_fornecedor_janela.destroy()  
            except Exception as e:
                mostrar_erro("Erro ao excluir fornecedor", f"Erro: {str(e)}")

        button_confirmar = ctk.CTkButton(janela_exclusao, text="Confirmar", text_color='black',
                                     fg_color="#5D3EBC", border_color='#ECF0F1',
                                     hover_color='white', command=excluir_fornecedor)
        button_confirmar.pack(pady=10)

        janela_exclusao.mainloop()

    button_buscar = ctk.CTkButton(editar_fornecedor_janela, text="Buscar Fornecedor",
                              text_color='black',
                              fg_color="#5D3EBC", border_color='#ECF0F1',
                              hover_color='white', command=buscar_e_preencher_dados)
    button_buscar.pack(pady=10)

    button_salvar = ctk.CTkButton(editar_fornecedor_janela, text="Salvar Edição",
                              text_color='black',
                              fg_color="#5D3EBC", border_color='#ECF0F1',
                              hover_color='white', command=salvar_edicao)
    button_salvar.pack(pady=10)

    button_excluir = ctk.CTkButton(editar_fornecedor_janela, text="Excluir Fornecedor",
                               text_color='black',
                               fg_color="#5D3EBC", border_color='#ECF0F1',
                               hover_color='white', command=confirmar_exclusao)
    button_excluir.pack(pady=10)

    editar_fornecedor_janela.mainloop()

# funcao onde listo todos os fornecedores
def listar_fornecedores():
    listar_fornecedores_janela = ctk.CTk(fg_color='darkgray')
    listar_fornecedores_janela.title("Listagem de Fornecedores")
    listar_fornecedores_janela.geometry("900x600")

    textbox_fornecedores = ctk.CTkTextbox(listar_fornecedores_janela, font=("Arial", 14),
                                           text_color='black', fg_color='white', width=900, height=500)
    textbox_fornecedores.pack(pady="5", padx="20")

    def preencher_lista():
        textbox_fornecedores.delete("1.0", "end")

        fornecedores = Fornecedor.listar_fornecedores()

        lista_texto = ""
        for fornecedor in fornecedores:
            lista_texto += f"Nome do fornecedor: {fornecedor.nome_fornecedor}\n"
            lista_texto += f"Telefone: {fornecedor.telefone}\n"
            lista_texto += f"Endereço: {fornecedor.endereco_fornecedor}\n"
            lista_texto += f"CNPJ: {fornecedor.cnpj}\n\n"

        textbox_fornecedores.insert("1.0", lista_texto)

    preencher_lista()

    button_atualizar = ctk.CTkButton(listar_fornecedores_janela, text="Atualizar Lista",
                                     text_color='black',
                                     fg_color="#5D3EBC", border_color='#ECF0F1',
                                     hover_color='white', command=preencher_lista)
    button_atualizar.pack()

    listar_fornecedores_janela.mainloop()

#funcao onde cadastro minhas vendas
def cadastrar_venda():
    cadastro_venda = ctk.CTk(fg_color= 'darkgray')
    cadastro_venda.title("Cadastro de Vendas")
    cadastro_venda.geometry("400x300")
    
    label_nome_produto = ctk.CTkLabel(cadastro_venda, text="Nome do Produto:", text_color= 'black')
    label_nome_produto.pack()

    entry_nome_produto = AutocompleteEntry_produtos(cadastro_venda, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_produto.pack()

    label_quantidade_vendida = ctk.CTkLabel(cadastro_venda, text="Quantidade Vendida:", text_color= 'black')
    label_quantidade_vendida.pack()

    entry_quantidade_vendida = ctk.CTkEntry(cadastro_venda, width= 300, placeholder_text= "EXEMPLO: 03")
    entry_quantidade_vendida.pack()

    label_nome_cliente = ctk.CTkLabel(cadastro_venda, text="Nome do Cliente:", text_color= 'black')
    label_nome_cliente.pack()

    entry_nome_cliente = ctk.CTkEntry(cadastro_venda, width= 300, placeholder_text= "Sem acentos ou pontuação")
    entry_nome_cliente.pack()

    label_preco_venda = ctk.CTkLabel(cadastro_venda, text="Preço de Venda:", text_color= 'black')
    label_preco_venda.pack()

    entry_preco_venda = ctk.CTkEntry(cadastro_venda, width= 300, placeholder_text= "EXEMPLO: 75.25")
    entry_preco_venda.pack()

    def salvar_venda():
        try:
            quantidade_vendida = int(entry_quantidade_vendida.get())
            nome_produto = entry_nome_produto.get()
            nome_cliente = entry_nome_cliente.get()
            preco_venda = float(entry_preco_venda.get())
            data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if not quantidade_vendida or not nome_produto or not nome_cliente or not preco_venda:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            Vendas.criar_tabela_vendas()

            Vendas.criar_venda(quantidade_vendida, nome_produto, nome_cliente, preco_venda, data_venda)

            mostrar_mensagem("Cadastro de Venda", f"Venda do produto '{nome_produto}' cadastrada com sucesso!")
            cadastro_venda.destroy()

        except Exception as e:
            mostrar_erro("Erro ao cadastrar venda", f"Erro: {str(e)}")

    button_cadastrar = ctk.CTkButton(cadastro_venda, text="Cadastrar Venda", text_color= 'black',
                                      fg_color= "#5D3EBC", border_color= '#ECF0F1',
                                      hover_color= 'white', command=salvar_venda)
    button_cadastrar.pack(pady= 10)

    cadastro_venda.mainloop()

# funcao onde edito minhas vendas
def editar_venda():
    editar_venda_janela = ctk.CTk(fg_color='darkgray')
    editar_venda_janela.title("Editar Venda")
    editar_venda_janela.geometry("400x500")  # Aumentei a altura para acomodar o novo botão

    label_nome_produto = ctk.CTkLabel(editar_venda_janela, text="Nome do Produto:", text_color='black')
    label_nome_produto.pack()

    entry_nome_produto = AutocompleteEntry_vendas(editar_venda_janela, width=300, placeholder_text="Nome do Produto")
    entry_nome_produto.pack()

    label_quantidade = ctk.CTkLabel(editar_venda_janela, text="Quantidade Vendida:", text_color='black')
    label_quantidade.pack()

    entry_quantidade = ctk.CTkEntry(editar_venda_janela, width=300, placeholder_text="Quantidade")
    entry_quantidade.pack()

    label_cliente = ctk.CTkLabel(editar_venda_janela, text="Nome do Cliente:", text_color='black')
    label_cliente.pack()

    entry_cliente = ctk.CTkEntry(editar_venda_janela, width=300, placeholder_text="Nome do Cliente")
    entry_cliente.pack()

    label_preco = ctk.CTkLabel(editar_venda_janela, text="Preço de Venda:", text_color='black')
    label_preco.pack()

    entry_preco = ctk.CTkEntry(editar_venda_janela, width=300, placeholder_text="Preço")
    entry_preco.pack()

    def buscar_e_preencher_dados():
        try:
            nome_produto = entry_nome_produto.get().strip().lower()

            venda = Vendas.buscar_venda_por_nome_produto(nome_produto)

            if venda:
                entry_quantidade.delete(0, "end")
                entry_quantidade.insert(0, venda[1])  

                entry_cliente.delete(0, "end")
                entry_cliente.insert(0, venda[3]) 

                entry_preco.delete(0, "end")
                entry_preco.insert(0, venda[4]) 
            else:
                mostrar_erro("Venda não encontrada", f"Venda com produto '{nome_produto}' não encontrada.")

        except Exception as e:
            mostrar_erro("Erro ao buscar venda", f"Erro: {str(e)}")

    def salvar_edicao():
        try:
            nome_produto = entry_nome_produto.get().strip().lower()
            quantidade_vendida = int(entry_quantidade.get().strip())
            nome_cliente = entry_cliente.get().strip()
            preco_venda = float(entry_preco.get().strip())
            data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if not nome_produto or not quantidade_vendida or not nome_cliente or not preco_venda:
                mostrar_erro("Erro de Validação", "Por favor, preencha todos os campos corretamente.")
                return

            venda = Vendas.buscar_venda_por_nome_produto(nome_produto)
            if not venda:
                mostrar_erro("Venda não encontrada", f"Venda com produto '{nome_produto}' não encontrada.")
                return

            Vendas.atualizar_venda(venda[0], quantidade_vendida, nome_produto, nome_cliente, preco_venda, data_venda)
            mostrar_mensagem("Venda Editada", f"Venda do produto '{nome_produto}' editada com sucesso!")
            editar_venda_janela.destroy()

        except ValueError as ve:
            mostrar_erro("Erro ao editar venda", str(ve))
        except Exception as e:
            mostrar_erro("Erro ao editar venda", f"Erro: {str(e)}")

    def confirmar_exclusao():
        nome_produto = entry_nome_produto.get().strip().lower()

        janela_exclusao = ctk.CTk(fg_color='darkgray')
        janela_exclusao.title("Confirmação de Exclusão")
        janela_exclusao.geometry("400x150")

        label_confirmar = ctk.CTkLabel(janela_exclusao, text=f"Tem certeza que deseja excluir a venda do produto '{nome_produto}'?", text_color='black')
        label_confirmar.pack(pady=10)

        def excluir_venda():
            try:
                Vendas.deletar_venda(nome_produto)
                mostrar_mensagem("Venda Excluída", f"Venda do produto '{nome_produto}' foi excluída com sucesso!")
                janela_exclusao.destroy()
                editar_venda_janela.destroy() 
            except Exception as e:
                mostrar_erro("Erro ao excluir venda", f"Erro: {str(e)}")

        button_confirmar = ctk.CTkButton(janela_exclusao, text="Confirmar", text_color='black',
                                         fg_color="#5D3EBC", border_color='#ECF0F1',
                                         hover_color='white', command=excluir_venda)
        button_confirmar.pack(pady=10)

        janela_exclusao.mainloop()

    def reverter_venda():
        try:
            nome_produto = entry_nome_produto.get().strip().lower()

            venda = Vendas.buscar_venda_por_nome_produto(nome_produto)
            if not venda:
                mostrar_erro("Venda não encontrada", f"Venda com produto '{nome_produto}' não encontrada.")
                return

            quantidade_vendida = venda[1]  # A quantidade vendida está no índice 1

            # Reverte a venda (atualiza quantidade do produto e exclui a venda)
            Vendas.reverter_venda(venda[0], nome_produto, quantidade_vendida)
            mostrar_mensagem("Venda Revertida", f"Venda do produto '{nome_produto}' foi revertida com sucesso!")
            editar_venda_janela.destroy()

        except Exception as e:
            mostrar_erro("Erro ao reverter venda", f"Erro: {str(e)}")

    button_buscar = ctk.CTkButton(editar_venda_janela, text="Buscar Venda",
                                  text_color='black',
                                  fg_color="#5D3EBC", border_color='#ECF0F1',
                                  hover_color='white', command=buscar_e_preencher_dados)
    button_buscar.pack(pady=10)

    button_salvar = ctk.CTkButton(editar_venda_janela, text="Salvar Edição",
                                  text_color='black',
                                  fg_color="#5D3EBC", border_color='#ECF0F1',
                                  hover_color='white', command=salvar_edicao)
    button_salvar.pack(pady=10)

    button_excluir = ctk.CTkButton(editar_venda_janela, text="Excluir Venda",
                                   text_color='black',
                                   fg_color="#5D3EBC", border_color='#ECF0F1',
                                   hover_color='white', command=confirmar_exclusao)
    button_excluir.pack(pady=10)

    button_reverter = ctk.CTkButton(editar_venda_janela, text="Reverter Venda",
                                    text_color='black',
                                    fg_color="#5D3EBC", border_color='#ECF0F1',
                                    hover_color='white', command=reverter_venda)
    button_reverter.pack(pady=10)  # Adicionando o botão de reverter venda

    editar_venda_janela.mainloop()

#funcao para lista as vendas feitas
def listar_vendas():
    listar_vendas_janela = ctk.CTk(fg_color='darkgray')
    listar_vendas_janela.title("Listagem de Vendas")
    listar_vendas_janela.geometry("900x600")
    textbox_vendas = ctk.CTkTextbox(listar_vendas_janela, font=("Arial", 14),
                                     text_color='black', fg_color='white', width=900, height=500)
    textbox_vendas.pack(pady="5", padx="20")

    def preencher_lista():
        textbox_vendas.delete("1.0", "end")

        vendas = Vendas.listar_vendas()

        lista_texto = ""
        for venda in vendas:
            lista_texto += f"ID da Venda: {venda.id_venda}\n"
            lista_texto += f"Quantidade Vendida: {venda.quantidade_vendida}\n"
            lista_texto += f"Nome do Produto: {venda.nome_produto}\n"
            lista_texto += f"Nome do Cliente: {venda.nome_cliente}\n"
            lista_texto += f"Preço de Venda: {venda.preco_venda}\n"
            lista_texto += f"Data da Venda: {venda.data_venda}\n\n"

        textbox_vendas.insert("1.0", lista_texto)

    preencher_lista()

    button_atualizar = ctk.CTkButton(listar_vendas_janela, text="Atualizar Lista",
                                     text_color='black',
                                     fg_color="#5D3EBC", border_color='#ECF0F1',
                                     hover_color='white', command=preencher_lista)
    button_atualizar.pack()

    listar_vendas_janela.mainloop()

# interface e botoes das tabs, parte principal da interface
def main():
    janela = ctk.CTk()
    janela.title("Sistema de Gerenciamento de Vendas e Cadastro de Clientes")
    janela.geometry("800x600")  # Tamanho maior para a janela principal
    pagina_inicial = ctk.CTkFrame(janela, fg_color= 'darkgray')

    def exibir_pagina_inicial():
        pagina_inicial.pack(fill="both", expand=True)

    def esconder_pagina_inicial():
        pagina_inicial.pack_forget()

        tabview = ctk.CTkTabview(janela, corner_radius= 20, border_width=5, width= 4,
                                 fg_color= "darkgray", border_color= '#5D3EBC', text_color= 'black',
                                 segmented_button_selected_color='#5D3EBC', segmented_button_unselected_color= 'darkgray',
                                 segmented_button_unselected_hover_color='white')
        
        tabview.pack(side= 'left', expand=True, fill= 'both' , padx=20, pady=20)  
        aba_produtos = tabview.add("Produtos")

        botao1_produtos = ctk.CTkButton(aba_produtos, text="Cadastrar Produto", text_color= "black", fg_color= "#5D3EBC", 
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_cadastrar, font=("Arial", 17, "bold"), width=60, height=60,
                                command=cadastrar_produto)
        botao1_produtos.place(relx=0.2, rely=0.2, anchor="center")

        botao2_produtos = ctk.CTkButton(aba_produtos, text="Editar Produto", text_color= "black", fg_color= "#5D3EBC",
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_editar, font=("Arial", 17, "bold"), width=60, height=60,
                                        command=editar_produto)
        botao2_produtos.place(relx=0.5, rely=0.2, anchor="center")

        botao3_produtos = ctk.CTkButton(aba_produtos, text="Listar Produtos", text_color= "black", fg_color= "#5D3EBC",
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_listar, font=("Arial", 17, "bold"), width=60, height=60,
                                        command=listar_produtos)
        botao3_produtos.place(relx=0.8, rely=0.2, anchor="center")

        aba_clientes = tabview.add("Clientes")

        botao1_clientes = ctk.CTkButton(aba_clientes, text="Cadastrar Cliente", text_color= "black", fg_color= "#5D3EBC", 
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_cadastrar, font=("Arial", 17, "bold"), width=60, height=60,
                                command=cadastrar_cliente)
        botao1_clientes.place(relx=0.2, rely=0.2, anchor="center")

        botao2_clientes = ctk.CTkButton(aba_clientes, text="Editar Clientes", text_color= "black", fg_color= "#5D3EBC",
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_editar, font=("Arial", 17, "bold"), width=60, height=60,
                                        command=editar_cliente)
        botao2_clientes.place(relx=0.5, rely=0.2, anchor="center")

        botao3_clientes = ctk.CTkButton(aba_clientes, text="Listar Clientes", text_color= "black", fg_color= "#5D3EBC",
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_listar, font=("Arial", 17, "bold"), width=60, height=60,
                                        command=listar_clientes)
        botao3_clientes.place(relx=0.8, rely=0.2, anchor="center")

        aba_fornecedores = tabview.add("Fornecedores")

        botao1_fornecedores = ctk.CTkButton(aba_fornecedores, text="Cadastrar Fornecedor", text_color= "black", fg_color= "#5D3EBC", 
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_cadastrar, font=("Arial", 17, "bold"), width=60, height=60,
                                command=cadastrar_fornecedor)
        botao1_fornecedores.place(relx=0.2, rely=0.2, anchor="center")

        botao2_fornecedores = ctk.CTkButton(aba_fornecedores, text="Editar Fornecedor", text_color= "black", fg_color= "#5D3EBC", 
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_editar, font=("Arial", 17, "bold"), width=60, height=60,
                                command=editar_fornecedor)
        botao2_fornecedores.place(relx=0.5, rely=0.2, anchor="center")

        botao3_fornecedores = ctk.CTkButton(aba_fornecedores, text="Listar Fornecedores", text_color= "black", fg_color= "#5D3EBC",
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_listar, font=("Arial", 17, "bold"), width=60, height=60,
                                        command=listar_fornecedores)
        botao3_fornecedores.place(relx=0.8, rely=0.2, anchor="center")

        aba_vendas = tabview.add("Vendas")

        botao1_vendas = ctk.CTkButton(aba_vendas, text="Cadastrar Venda", text_color= "black", fg_color= "#5D3EBC", 
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_cadastrar, font=("Arial", 17, "bold"), width=60, height=60,
                                command=cadastrar_venda)
        botao1_vendas.place(relx=0.2, rely=0.2, anchor="center")

        botao2_vendas = ctk.CTkButton(aba_vendas, text="Editar Venda", text_color= "black", fg_color= "#5D3EBC", 
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_editar, font=("Arial", 17, "bold"), width=60, height=60,
                                command=editar_venda)
        botao2_vendas.place(relx=0.5, rely=0.2, anchor="center")

        botao3_vendas = ctk.CTkButton(aba_vendas, text="Listar Vendas", text_color= "black", fg_color= "#5D3EBC",
                                        border_color= '#ECF0F1', hover_color= 'white',
                                         image= imagem_de_listar, font=("Arial", 17, "bold"), width=60, height=60,
                                        command=listar_vendas)
        botao3_vendas.place(relx=0.8, rely=0.2, anchor="center")

    
    label_boas_vindas = ctk.CTkLabel(pagina_inicial, text=f"Boas vindas:\nPrograma de gerenciamento e cadastro de produtos, clientes, fornecedores e vendas\ncriado por Jackson Lopes",
                                     text_color= 'black', font=("Arial", 18, "bold"), justify="center")
    label_boas_vindas.pack(pady=100)

    botao_iniciar = ctk.CTkButton(pagina_inicial, text="Iniciar Programa",
                                  text_color= "black", fg_color= "#5D3EBC",
                                  border_color= '#ECF0F1', hover_color= 'white',
                                  image= imagem_de_iniciar, font=("Arial", 16, "bold"),
                                  width=40, height=40, command=esconder_pagina_inicial)
    botao_iniciar.pack()

    # Mostra a página inicial ao iniciar o programa
    exibir_pagina_inicial()

    # Inicia o loop de eventos
    janela.mainloop()


if __name__ == "__main__":
    main()

