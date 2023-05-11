from django.http import JsonResponse, HttpResponse
from events.models import Event
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from events.models import Event
import json
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        event_id = request.GET.get('id')
        event_type = request.GET.get('type')
        limit = request.GET.get('limit')
        page = request.GET.get('page')

        if event_id:
            try:
                event = Event.objects.get(id=event_id) 
                event_data = {
                    'id': event.id,
                    'name': event.name,
                    'tagline': event.tagline,
                    'schedule': str(event.schedule),
                    'description': event.description,
                    'moderator': str(event.moderator.username),
                    'category': event.category,
                    'sub_category': event.sub_category,
                    'rigor_rank': event.rigor_rank,
                    'attendees': [i.username for i in event.attendees.all()],
                }
                return JsonResponse(event_data, safe=False)
            except Event.DoesNotExist:
                return HttpResponse(status=404)

        if event_type == 'latest':
            events = Event.objects.order_by('-schedule')[:int(limit)]
            event_list = []
            for event in events:
                event_data = {
                    'id': event.id,
                    'name': event.name,
                    'tagline': event.tagline,
                    'schedule': str(event.schedule),
                    'description': event.description,
                    'moderator': str(event.moderator.username),
                    'category': event.category,
                    'sub_category': event.sub_category,
                    'rigor_rank': event.rigor_rank,
                    'attendees': [i.username for i in event.attendees.all()],
                }
                event_list.append(event_data)
            return JsonResponse(event_list, safe=False)

        # Handle pagination if required

    elif request.method == 'POST':
        event_data = json.loads(request.body)
        uid=event_data.get('uid')
        name = event_data.get('name')
        tagline = event_data.get('tagline')
        schedule = event_data.get('schedule')
        description = event_data.get('description')
        moderator = event_data.get('moderator')
        category = event_data.get('category')
        sub_category = event_data.get('sub_category')
        rigor_rank = event_data.get('rigor_rank')
        attendees = event_data.get('attendees')

        find_moderator = get_object_or_404(User, username=moderator)
        find_attendee = []
        for i in attendees:
            attendee = get_object_or_404(User, username=i)
            find_attendee.append(attendee.id)
        event = Event.objects.create(
            uid=uid,
            name=name,
            tagline=tagline,
            schedule=schedule,
            description=description,
            moderator=find_moderator,
            category=category,
            sub_category=sub_category,
            rigor_rank=rigor_rank,
        )
        event.attendees.set(find_attendee)
        return JsonResponse({'id': event.id}, status=201)

    else:
        return HttpResponse(status=405)


@csrf_exempt
def event_detail(request):
    if request.method == 'GET':
        event_id = request.GET.get('id')
        if event_id:
            try:
                event = Event.objects.get(id=event_id) 
                event_data = {
                    'id': event.id,
                    'name': event.name,
                    'tagline': event.tagline,
                    'schedule': str(event.schedule),
                    'description': event.description,
                    'moderator': str(event.moderator.username),
                    'category': event.category,
                    'sub_category': event.sub_category,
                    'rigor_rank': event.rigor_rank,
                    'attendees': [i.username for i in event.attendees.all()],
                }
                # print(json.dumps(event_data))
                return JsonResponse(event_data, safe=False)
            except Event.DoesNotExist:
                return HttpResponse(status=404)

    elif request.method == 'PUT':
        event_id = request.GET.get('id')
        if event_id:
            try:
                event = Event.objects.get(id=event_id)

                event_data = json.loads(request.body)
                moderator_username = event_data.get('moderator')
                find_moderator = get_object_or_404(User, username=moderator_username)

                attendees = event_data.get('attendees', [])
                find_attendees = []
                for attendee_username in attendees:
                    attendee = get_object_or_404(User, username=attendee_username)
                    find_attendees.append(attendee)

                event.uid = event_data.get('uid', event.uid)
                event.name = event_data.get('name', event.name)
                event.tagline = event_data.get('tagline', event.tagline)
                event.schedule = event_data.get('schedule', event.schedule)
                event.description = event_data.get('description', event.description)
                event.moderator = find_moderator
                event.category = event_data.get('category', event.category)
                event.sub_category = event_data.get('sub_category', event.sub_category)
                event.rigor_rank = event_data.get('rigor_rank', event.rigor_rank)

                event.attendees.clear()  # Clear existing attendees
                event.attendees.add(*find_attendees)  # Add new attendees

                event.save()
                return JsonResponse({'id': event.id}, safe=False)
            except Event.DoesNotExist:
                return HttpResponse(status=404)



    elif request.method == 'DELETE':
        event_id = request.GET.get('id')
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({'id': event.id}, safe=False)
        except Event.DoesNotExist:
            return HttpResponse(status=404)

    return HttpResponse(status=405)

        
