from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
	"""home page"""
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	"""page to show all topics"""
	# make sure user can only view his/her own topics
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""page to show a specific topic"""
	topic = Topic.objects.get(id=topic_id)
	# make sure this specific topic belongs to this user
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added') # latest entry is shown on top
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""add a new topic"""
	if request.method != 'POST':
		# user not make a post request
		form = TopicForm() # new form for user to enter the topic
	else: # user is adding a new topic
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect((reverse('learning_logs:topics')))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""add a new entry"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""edit a specific entry"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)
