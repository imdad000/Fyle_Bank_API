from django.shortcuts import render
from fyleApp.models import Branches
import requests
from django.shortcuts import render,redirect
import csv
from django.http import HttpResponseRedirect, HttpResponse
from  django.db.utils import IntegrityError
# Create your views here.
def bank_detail(request):
	all_bank=Branches.objects.all()
	print(len(all_bank))
	context={
		'total':all_bank
	}
	return render(request,"home_page.html",context)


