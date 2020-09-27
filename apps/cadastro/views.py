from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from .tasks import Address

class AllAddress(APIView):

    def get(self, request):

        if 'cep' in request.query_params.keys():
            cep = request.query_params['cep']
            try:
                address = Address(cep)
                address.validate_cep()
                all_address = address.get_address_info()
                return HttpResponse(all_address)
            except ValueError as ex:
                return HttpResponse(ex)
        else:
            return HttpResponse('No CEP data')

class RegisterClient(APIView):
    pass

