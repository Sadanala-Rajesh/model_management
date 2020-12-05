from django.shortcuts import render
from app1.models import *

def display_data(request):
	data=Document.objects.smaller_than(10)
	data1 = Document.objects.get(name='xyz',file_type='abc')
	data2=data1.full_name
	print(data,data2)
