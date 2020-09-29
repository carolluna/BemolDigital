import requests
import json

from tkinter import *

class UserRegister:

    def __init__(self, master=None):
        self.fonte = ("Verdana", "10")
        
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.titulo = Label(self.container1, text="CADASTRO BEMOL DIGITAL")
        self.titulo["font"] = ("Calibri", "15", "bold")
        self.titulo.pack ()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.lblnome = Label(self.container2, text="Nome Completo:", font=self.fonte, width=20)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container2)
        self.txtnome["width"] = 40
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.lblemail = Label(self.container3, text="Email:", font=self.fonte, width=20)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container3)
        self.txtemail["width"] = 40
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=20)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 40
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.lblnascimento = Label(self.container5, text="Data de Nascimento: YYYY-MM-DD", font=self.fonte, width=30)
        self.lblnascimento.pack(side=LEFT)
        self.txtnascimento = Entry(self.container5)
        self.txtnascimento["width"] = 40
        self.txtnascimento["font"] = self.fonte
        self.txtnascimento.pack(side=LEFT)

        self.container6 = Frame(master)
        self.container6["padx"] = 10
        self.container6["pady"] = 5
        self.container6.pack()
        self.lblcep = Label(self.container6, text="CEP:", font=self.fonte, width=10)
        self.lblcep.pack(side=LEFT)
        self.txtcep = Entry(self.container6)
        self.txtcep["width"] = 8
        self.txtcep["font"] = self.fonte
        self.txtcep.pack(side=LEFT)
        self.btnBuscar = Button(self.container6, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarcep
        self.btnBuscar.pack(side=RIGHT)

        self.container7 = Frame(master)
        self.container7["padx"] = 5
        self.container7["pady"] = 5
        self.container7.pack()
        self.lblrua = Label(self.container7, text="Rua:", font=self.fonte, width=5)
        self.lblrua.pack(side=LEFT)
        self.txtrua = Entry(self.container7)
        self.txtrua["width"] = 40
        self.txtrua["font"] = self.fonte
        self.txtrua.pack(side=LEFT)
        self.lblnumero = Label(self.container7, text="Número:", font=self.fonte, width=8)
        self.lblnumero.pack(side=LEFT)
        self.txtnumero = Entry(self.container7)
        self.txtnumero['width'] = 5
        self.txtnumero["font"] = self.fonte
        self.txtnumero.pack(side=RIGHT)

        self.container8 = Frame(master)
        self.container8["padx"] = 10
        self.container8["pady"] = 5
        self.container8.pack()
        self.lblbairro = Label(self.container8, text="Bairro:", font=self.fonte, width=8)
        self.lblbairro.pack(side=LEFT)
        self.txtbairro = Entry(self.container8)
        self.txtbairro["width"] = 20
        self.txtbairro["font"] = self.fonte
        self.txtbairro.pack(side=LEFT)
        self.lblcidade = Label(self.container8, text="Cidade:", font=self.fonte, width=8)
        self.lblcidade.pack(side=LEFT)
        self.txtcidade = Entry(self.container8)
        self.txtcidade['width'] = 20
        self.txtcidade['font'] = self.fonte
        self.txtcidade.pack(side=LEFT)
        self.lbluf = Label(self.container8, text="UF:", font=self.fonte, width=4)
        self.lbluf.pack(side=LEFT)
        self.txtuf = Entry(self.container8)
        self.txtuf["width"] = 3
        self.txtuf['font'] = self.fonte
        self.txtuf.pack(side=RIGHT)

        self.container9 = Frame(master)
        self.container9["padx"] = 10
        self.container9["pady"] = 5
        self.container9.pack()
        self.lblsenha = Label(self.container9, text="Senha:", font=self.fonte, width=7)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container9)
        self.txtsenha['width'] = 20
        self.txtsenha['font'] = self.fonte
        self.txtsenha['show'] = "*"
        self.txtsenha.pack(side=LEFT)

        self.container10 = Frame(master)
        self.container10["padx"] = 10
        self.container10["pady"] = 5
        self.container10.pack()
        self.btnCadastrar = Button(self.container10, text="Cadastrar", font=self.fonte, width=10)
        self.btnCadastrar["command"] = self.cadastrar_user
        self.btnCadastrar.pack(side=RIGHT)
        
        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()
        self.lblmsg = Label(self.container11, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def buscarcep(self):
        cep = self.txtcep.get()
        response = requests.get(f'http://127.0.0.1:8000/cadastro/address/?cep={cep}')
        result = json.loads(response.content)
        print(result)

        if response.status_code == 201:    
            self.txtrua.delete(0, END)
            self.txtrua.insert(INSERT, result['street'])
            self.txtbairro.delete(0, END)
            self.txtbairro.insert(INSERT, result['neighborhood'])
            self.txtcidade.delete(0, END)
            self.txtcidade.insert(INSERT, result['city'])
            self.txtuf.delete(0, END)
            self.txtuf.insert(INSERT, result['uf'])
        else:
            self.txtrua.delete(0, END)
            self.txtbairro.delete(0, END)
            self.txtcidade.delete(0, END)
            self.txtuf.delete(0, END)
            self.lblmsg['text'] = result['error']

    def cadastrar_user(self):
        if self.check_fields():
            payload = json.dumps(self.set_dict())
            response = requests.post('http://127.0.0.1:8000/cadastro/register/', data=payload)
            self.check_response(response)
        else:
            self.lblmsg['text'] = 'Todos os campos devem ser preenchidos'
    
    def check_response(self, response):
        if response.status_code == 201:
            self.lblmsg['text'] = 'Cadastrado com sucesso'
        else:
            self.lblmsg['text'] = json.loads(response.content)



    def set_dict(self):
        result = {'name': self.txtnome.get(),
                  'birth': self.txtnascimento.get(),
                  'cep': self.txtcep.get(),
                  'street': self.txtrua.get(),
                  'home_number': self.txtnumero.get(),
                  'neighborhood': self.txtbairro.get(),
                  'city': self.txtcidade.get(),
                  'phone': self.txttelefone.get(),
                  'uf': self.txtuf.get(),
                  'email': self.txtemail.get(),
                  'passw': self.txtsenha.get() }
        
        return result

    def check_fields(self):
        if not (self.txtnome.get() 
                and self.txtemail.get()
                and self.txtnascimento.get()
                and self.txttelefone.get()
                and self.txtcep.get()
                and self.txtcidade.get()
                and self.txtbairro.get()
                and self.txtnumero.get()
                and self.txtrua.get()
                and self.txtsenha.get()
                and self.txtuf.get()):
            
            return False

        else:
            return True
            


root = Tk()
UserRegister(root)
root.mainloop()