from django.http import HttpResponse
from celery import  group
from.tasks import  log_loop
import json
from .models import Address
from django.shortcuts import render
# response = requests.get("http://data.fixer.io/api/latest?access_key=XXX&base=EUR")

# rates_EUR = json.loads(response.content.decode('utf-8'))
# timestamp = rates_EUR['timestamp']
# base = rates_EUR['base']
# date = rates_EUR['date']
# rates = rates_EUR['rates']

# rates_new = ratesEUR(timestamp=timestamp, base=base, date=date, rates=rates)
# rates_new.save()



def test(request):
    log_loop.delay("block_filter", 2)
    if request.method == "POST":
        body_unicode = request.body	
        body = json.loads(body_unicode.decode('utf-8')) 
        name = body['name']
        address = body['address']
        new_data = Address(name=name, address=address)
        new_data.save()
           
    return render(request, 'index.html')