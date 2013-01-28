# Create your views here.
import simplejson as json
from random import choice
from itertools import groupby

from django.core.serializers.json import DjangoJSONEncoder
from django.core.cache import cache
from django.http import HttpResponse

from models import EnergyDataPoint
from Smartility.apps.categories.models import Category



def get_data(request, user_id):
    response_data = {'message':'failed'}
    response_data['data'] = []
    response_data['title'] = "Energy Costs for the Month of January"
    start_time = request.GET.get('start','2012-01-01 00:00:00+00:00')
    end_time = request.GET.get('end', '2012-02-01 00:00:00+00:00')
    category = request.GET.get('cat', None)
    granularity = request.GET.get('gran', None)
    
    KEY = "data_key"
    KEY_CAT = "cat_key"
    if category:
        KEY = KEY + category
        
    datapoints = cache.get(KEY)
    
    if not datapoints:
        print "Cache Miss"
        datapoints = EnergyDataPoint.objects.filter(start_time__gte=start_time,end_time__lte=end_time)
        if category:
            datapoints = datapoints.filter(category_id=category)
        datapoints = datapoints.order_by('start_time')
        cache.set(KEY,datapoints)
    else:
        print "Cache Hit"
    cat = cache.get(KEY_CAT)
    if not cat and category:
        cat = Category.objects.get(pk=category)
        cache.set(KEY_CAT,cat)
    response_data['title'] = "{} ({})".format(response_data['title'], cat.name)

    if granularity == "day":
        for start_date, group in groupby(datapoints, key=lambda x: x.start_time.date()):
            response_data['data'].append(sum(data.value for data in list(group)))
        response_data['pointInterval'] = 24 * 3600 * 1000 #one day
        
    else:
        for start_date, group in groupby(datapoints, key=lambda x: x.start_time.time()):
            response_data['data'].append(sum(data.value for data in list(group)))
        response_data['pointInterval'] = 3600 * 1000 #one hour
    response_data['message'] = 'success'
    response_data['user'] = user_id
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_tips(request, user_id):
    response_data = {}
    OPTIONS = ('Save money by looking for ENERGY STAR labels on electronics.',
               'Switch to flourescent light bulbs, which use 3/4 less energy and last up to 10 times longer!',
               'When installed properly, a progammable thermostat can reduce heating and cooling costs by 10%.',
               'Switching off unneccessary lights can reduce your electricity bill.')
    response_data['tip'] = choice(OPTIONS)
    response_data['message'] = 'success'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

        
    