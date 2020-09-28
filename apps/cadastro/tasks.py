import requests
import json
import re

class Register:
    def __init__(self, user_info):
        self.name = user_info['name']
        self.birth = user_info['birth']
        self.cep = user_info['cep']
        self.street = user_info['street']
        self.home_number = user_info['home_number']
        self.neighborhood = user_info['neighborhood']
        self.city = user_info['city']
        self.phone = user_info['phone']
        self.uf = user_info['uf']
        self.email = user_info['email']
        self.passw = user_info['passw']

    

class Address:
    def __init__(self, cep):
        self.cep = cep
        self.street = None
        self.neighborhood = None
        self.city = None
        self.uf = None

    def get_address_info(self):
        '''
        This method get address information
        return result as dict
        '''
        self.set_adress_info()
        result = {'street': self.street,
                  'neighborhood': self.neighborhood,
                  'city': self.city,
                  'uf': self.uf                  
                 }

        return result

    def validate_cep(self):
        '''
        This method validate if the informed cep is valid.
        no return
        '''
        if not len(self.cep) == 8:
            raise ValueError("CEP Inválido! O CEP deve possuir 8 números.")
        elif not re.match(r'^[0-9]*$', self.cep):
            raise ValueError("CEP Inválido! O CEP deve possuir somente números.")

    def check_existed_cep(self, dict_info):
        '''
        This method check if the informed cep exist.
        param: dict_info as dict
        return bool
        '''
        if 'erro' in dict_info.keys():
            if dict_info['erro'] == True:
                return False
            else:
                return True
        else:
            return True

    def set_adress_info(self):
        '''
        This method set the address atributes
        no return
        '''
        dict_info = self.get_api_info()
        if self.check_existed_cep(dict_info):
            self.street = dict_info['logradouro']
            self.neighborhood = dict_info['bairro']
            self.city = dict_info['localidade']
            self.uf = dict_info['uf']
        else:
            raise ValueError("Este CEP não existe! Por favor adicione um CEP válido.")

    def acess_viacep(self):
        '''
        This method access the viacep API
        return response as json
        '''
        response = requests.get(f'https://viacep.com.br/ws/{self.cep}/json')
        return response

    def get_api_info(self):
        '''
        This method get the viacep api response.
        return result as dict
        '''
        response = self.acess_viacep()
        result = json.loads(response.content)

        return result
