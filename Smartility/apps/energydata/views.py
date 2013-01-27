# Create your views here.
import json
from random import choice
from random import randrange
from itertools import groupby

from django.http import HttpResponse

from models import EnergyDataPoint
    

def get_data(request, user_id):
    response_data = {'message':'failed'}
    response_data['data'] = []
    start_time = request.GET.get('start','2012-01-01 00:00:00+00:00')
    end_time = request.GET.get('end', '2012-02-01 00:00:00+00:00')
    category = request.GET.get('cat', None)
    granularity = request.GET.get('gran',None)
    
    datapoints = EnergyDataPoint.objects.filter(start_time__gte=start_time,end_time__lte=end_time)
    if category:
        datapoints = datapoints.filter(category_id=category)
    datapoints = datapoints.order_by('start_time')

    if granularity == "day":
        for start_date, group in groupby(datapoints, key=lambda x: x.start_time.date()):
            response_data['data'].append([start_date.__str__(), sum(data.value for data in list(group)).__str__()])
    else:
        for point in datapoints:
            response_data['data'].append([point.start_time.__str__(), point.end_time.__str__(), point.category_id.__str__(), point.value.__str__()])
    response_data['message'] = 'success'
    response_data['user'] = user_id
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_tips(request, user_id):
    response_data = {}
    OPTIONS = ('Save money by looking for ENERGY STAR labels on electronics.',
               'Switch to flourescent light bulbs, which use 3/4 less energy and last up to 10 times longer!',
               'When installed properly, a progammable thermostat can reduce heating and cooling costs by 10%.',
               'Switching of unneccessary lights can reduce your electricity bill.')
    response_data['tip'] = choice(OPTIONS)
    response_data['message'] = 'success'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

        
    