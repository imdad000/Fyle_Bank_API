from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Branches,Banks
from .serializers import BranchesSerializer
from .serializers import BanksSerializer
# Create your views here.

@api_view(['GET'])
def get_bank_by_bankname(request,ifsc):
	try:
		ifsc =ifsc
		all_data=Branches.objects.all()
		print(all_data)
		print(ifsc)
		banks = Branches.objects.filter(ifsc = ifsc)
		print(banks)
		result=BranchesSerializer(banks,many=True)
	except Branches.DoesNotExist:
		result = {"status" : status.HTTP_404_NOT_FOUND,"msg" : "Bank Not Found"}
	return Response(result.data)


@api_view(['GET'])
def bank_detail(request,city,bank):
	try:
		city = city
		print(city)
		bank      =bank
		print(bank)
		query_set =Branches.objects.filter(city__contains=city, bank__name__contains=bank)
		print(query_set)
		result = BranchesSerializer(query_set, many=True)
	except Branches.DoesNotExist:
		result = {"status" : status.HTTP_404_NOT_FOUND,"msg" : "Bank Not Found"}
	return Response(result.data)


