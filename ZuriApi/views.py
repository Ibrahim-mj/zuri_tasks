from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import datetime

# Create your views here.

def info_render(request, slack_name, track):
    date = datetime.datetime.now()
    slack_name = request.GET.get('slack_name',)
    track = request.GET.get('track', None)

    if request.method == 'GET':
        slack_name = slack_name
        current_day = date.strftime('%A')
        utc_time = date.strftime('%Y-%m-%dT%H:%M:%SZ')
        track = track
        github_file_url = 'https://github.com/Ibrahim-mj/zuri_tasks/blob/main/ZuriApi/views.py'
        github_repo_url = 'https://github.com/Ibrahim-mj/zuri_tasks'
        status_code = 200

        context = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': utc_time,
            'track': track,
            'github_file_url': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': status_code
        }
        return JsonResponse(context)
    
    else:
        return JsonResponse(status=403)