from activitylog.models import Activity
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    activity_list = Activity.objects.all().order_by('-date')
    context = {'activity_list': activity_list}
    return render(request, 'activitylog/index.html', context)
    
def create_activity(request):
    activity_name = request.POST['activity_name']
    activity_type = request.POST['activity_type']
    activity_description = request.POST['activity_description']
    
    activity = Activity.create(activity_name, activity_type, activity_description)
    activity.save()
    return HttpResponseRedirect(reverse('index'))
    
def view_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    context = {'activity': activity}    
    return render(request, 'activitylog/detail.html', context)