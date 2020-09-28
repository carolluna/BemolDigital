from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .tasks import Address
from .serializers import UserSerializer

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

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
