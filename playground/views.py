from locale import currency
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.


# Define "views" here.. Views are functions that take http requests and return response

def say_hello(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM user''')
    roq = cursor.fetchone()
    return HttpResponse(roq)

