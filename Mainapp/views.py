from django.shortcuts import render


from models import Topic

# Create your views here.

def index(request):
    return render(request, 'Mainapp/index.html')

def topics(request):
    topics = Topic.objects.all().order_by('date_added')
    context= {'topics': topics}

    return render(request, 'Mainapp/topics.html', context)

def topics(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')

    context= {'topics': topics, 'entries':entries}
    return render(request, 'Mainapp/topics.html', context)


