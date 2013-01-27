# Create your views here.
import json

from django.http import HttpResponse

from models import EnergyDataPoint

def get_data(request, user_id):
    response_data = {'message':'failed'}
    start_time = request.GET.get('start','2012-01-01 00:00:00+00:00')
    end_time = request.GET.get('end', '2012-02-01 00:00:00+00:00')
    category = request.GET.get('cat', None)
    
    datapoints = EnergyDataPoint.objects.filter(start_time__gte=start_time,end_time__lte=end_time)
    print datapoints
    if category:
        datapoints.filter(category_id=category)

    if datapoints:
        response_data['data'] = []
    for point in datapoints:
        response_data['data'].append([point.start_time.__str__(), point.end_time.__str__(), point.category_id.__str__(), point.value.__str__()])
    response_data['message'] = 'success'
    response_data['user'] = user_id
    return HttpResponse(json.dumps(response_data), content_type="application/json")