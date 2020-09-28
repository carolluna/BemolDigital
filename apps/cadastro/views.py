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
                return JsonResponse(all_address, status=201)
            except ValueError as ex:
                print(ex)
                return JsonResponse({"error": str(ex)}, status=400)
        else:
            return JsonResponse({"error": 'No CEP data'}, status=400)

class RegisterClient(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
