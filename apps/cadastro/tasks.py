import requests
import json
import re

class Register:
    pass

class Address:
    def __init__(self, cep):
        self.cep = cep
        self.street = None
        self.neighborhood = None
        self.city = None
        self.uf = None
        self.check_cep()
    
    def check_cep(self):
        if not self.check_cep_len():
            raise ValueError("CEP Inválido! O CEP deve possuir 8 números.")
        elif not self.check_cep_values():
            raise ValueError("CEP Inválido! O CEP deve possuir somente números.")
    
    def check_cep_values(self):
        if re.match(r'^[0-9]*$', self.cep):
            return True
        else:
            return False

    def check_cep_len(self):
        if len(self.cep) == 8:
            return True
        else:
            return False
    
    def check_existed_cep(self, dict_info):
        if 'erro' in dict_info.keys():
            if dict_info['erro'] == True:
                return False
            else:
                return True
        else:
            return True

    def get_adress_info(self):
        dict_info = self.get_api_info()
        if self.check_existed_cep(dict_info):
            self.street = dict_info['logradouro']
            self.neighborhood = dict_info['bairro']
            self.city = dict_info['localidade']
            self.uf = dict_info['uf']
        else:
            raise ValueError("Este CEP não existe! Por favor adicione um CEP válido.") 

    def acess_viacep(self):
        response = requests.get(f'https://viacep.com.br/ws/{self.cep}/json')
        return response
    
    def get_api_info(self):
        response = self.acess_viacep()
        result = json.loads(response.content)

        return result
    
        
