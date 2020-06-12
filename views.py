from .models import Meeting, MeetingMinutes, Resource, Event

from django.shortcuts import get_object_or_404

from django.shortcuts import render

from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'pythonclubapp/index.html')


def getresources(request):
    resource_list = Resource.objects.all()
    return render (request, 'pythonclubapp/resources.html', {'resource_list' : resource_list})


def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render (request, 'pythonclubapp/meetings.html',{'meetings_list': meetings_list,})

def meetingdetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    context={
        'meeting': meeting,
    }
    return render(request, 'pythonclubapp/meetingdetails.html', context=context)

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'pythonclubapp/newmeeting.html', {'form':form})

@login_required
def newMinutes(request):
    form=MeetingMinutesForm
    if request.method=='POST':
        form=MeetingMinutesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingMinutesForm()
    else:
        form=MeetingMinutesForm()
    return render(request, 'pythonclubapp/newminutes.html', {'form':form})

@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'pythonclubapp/newresource.html', {'form':form})

@login_required
def newEvent(request):
    form=EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'pythonclubapp/newevent.html', {'form':form})



def loginmessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')

