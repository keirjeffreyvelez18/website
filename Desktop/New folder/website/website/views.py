from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.forms import ModelForm, Textarea
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
import time
import calendar, datetime
from operator import attrgetter
from itertools import chain

from .models import Program, NewsPost, FacultyMember, OutreachPost, UpcomingEvent, Alumni, ResearchTitle


class ProgramForm(ModelForm):
	class Meta:
		model = Program
		fields = ['program_name', 'program_description', 'program_department']

def lists(request):
	program_list = Program.objects.all()

	page = request.GET.get('page', 1)
	paginator = Paginator(program_list, 8)
	try:
		programs = paginator.page(page)
	except PageNotAnInteger:
		programs = paginator.page(1)
	except EmptyPage:
		programs = paginator.page(paginator.num_pages)
	return render(request, 'website/list.html', {'programs': programs, 'list': "active"})


def news(request, template_name='website/news.html'):
	news_list = NewsPost.objects.all().order_by('date', 'time')
	page = request.GET.get('page', 1)
	paginator = Paginator(news_list, 3)
	months = mkmonth_lst()

	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
	return render(request, template_name, {'news': news, "months": months, 'new': "active"})


def upcomingevents(request, template_name='website/upcomingevents.html'):
	events_list = UpcomingEvent.objects.all().order_by('date')
	page = request.GET.get('page', 1)
	paginator = Paginator(events_list, 3)

	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)
	except EmptyPage:
		events = paginator.page(paginator.num_pages)
	return render(request, template_name, {'events': events, 'new': "active"})


def outreach(request):
	# now = datetime.date.today()

	outreach_list = OutreachPost.objects.all()

	page = request.GET.get('page', 1)
	paginator = Paginator(outreach_list, 6)
	try:
		outreach = paginator.page(page)
	except PageNotAnInteger:
		outreach = paginator.page(1)
	except EmptyPage:
		outreach = paginator.page(paginator.num_pages)
	return render(request, 'website/outreach.html', {'outreach': outreach, 'out': "active"})


def alumni(request):
	alumni_list = Alumni.objects.all().order_by('alumni_name')
	page = request.GET.get('page', 1)
	paginator = Paginator(alumni_list, 8)
	try:
		alumni = paginator.page(page)
	except PageNotAnInteger:
		alumni = paginator.page(1)
	except EmptyPage:
		alumni = paginator.page(paginator.num_pages)
	return render(request, 'website/alumni.html', {'alumni': alumni, 'a': "active"})

def research_item(request, pk, template_name='website/research_item.html'):
	research = get_object_or_404(ResearchTitle, pk=pk)
	return render(request, template_name, {'object': research, 'research': "active"})

def program_item(request, pk, template_name='website/program_item.html'):
	program = get_object_or_404(Program, pk=pk)
	return render(request, template_name, {'object': program, 'list': "active"})


def news_item(request, pk, template_name='website/news_item.html'):
	news = get_object_or_404(NewsPost, pk=pk)
	return render(request, template_name, {'object': news, 'new': "active"})


def item_outreach(request, pk, template_name='website/outreach_item.html'):
	outreach = get_object_or_404(OutreachPost, pk=pk)
	return render(request, template_name, {'object': outreach, 'out': "active"})


def education(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Education")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Education"
	data['list'] = "active"
	return render(request, template_name, data)


def business(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Business Management and Administration")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Business Management and Administration"
	data['list'] = "active"
	return render(request, template_name, data)


def administration(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Public Administration and Governance")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Public Administration and Governance"
	data['list'] = "active"
	return render(request, template_name, data)


def management(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Development Management")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Development Management"
	data['list'] = "active"
	return render(request, template_name, data)


def computer_studies(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Computer Studies")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Computer Studies"
	data['list'] = "active"
	return render(request, template_name, data)


def criminal_justice(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Criminal Justice Education")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Criminal Justice Education"
	data['list'] = "active"
	return render(request, template_name, data)


def psychology(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Psychology and Guidance and Counseling")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Psychology and Guidance and Counseling"
	data['list'] = "active"
	return render(request, template_name, data)


def nursing(request, template_name='website/list_filtered.html'):
	programs = Program.objects.filter(program_department__exact="Nursing")
	data = {}
	data['object_list'] = programs
	data['dept'] = "Nursing"
	data['list'] = "active"
	return render(request, template_name, data)


def index(request, template_name='website/index.html'):
	news = NewsPost.objects.all().order_by('date', 'time')[0]
	events = UpcomingEvent.objects.all().order_by('date', 'time')[0]
	outreach = OutreachPost.objects.all().order_by('date')[0]
	return render(request, template_name, {'news': news, 'events': events, 'outreach': outreach, 'index': "active"})


def program(request, template_name='website/program.html'):
	return render(request, template_name, {'list': "active"})


def research(request, template_name='website/research.html'):
	research_list = ResearchTitle.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(research_list, 3)

	try:
		researches = paginator.page(page)
	except PageNotAnInteger:
		researches = paginator.page(1)
	except EmptyPage:
		researches = paginator.page(paginator.num_pages)

	return render(request, template_name, {'research_list': researches ,'research': "active"})


def faculty(request, template_name='website/faculty.html'):
	firstsem = FacultyMember.objects.filter(First_Semester__exact=True)
	secondsem = FacultyMember.objects.filter(Second_Semester__exact=True)
	data = {}
	data['firstsem'] = firstsem
	data['secondsem'] = secondsem
	data['faculty'] = "active"
	return render(request, template_name, data)


def contactus(request, template_name="website/contactus.html"):
	return render(request, template_name, {'contact': "active"})


def mkmonth_lst():
	if not NewsPost.objects.count(): return []

	# set up vars
	year, month = time.localtime()[:2]
	first = NewsPost.objects.order_by("date")[0]
	fyear = first.date.year
	fmonth = first.date.month
	months = []

	# loop over years and months
	for y in range(year, fyear - 1, -1):
		start, end = 12, 0
		if y == year: start = month
		if y == fyear: end = fmonth - 1

		for m in range(start, end, -1):
			months.append((y, m, calendar.month_name[m]))
	return months


def login(request, template_name='website/login.html'):
	return render(request, template_name)


def dashboard(request, template_name='website/dashboard.html'):
	events_list = UpcomingEvent.objects.all().order_by('date')
	events_count = events_list.count()
	news_list = NewsPost.objects.all().order_by('-date', '-time')
	latest_news = news_list[0]
	news_count = news_list.count()
	outreach_list = OutreachPost.objects.all().order_by('-date')
	outreach_count = outreach_list.count()
	alumni_list = Alumni.objects.all().order_by('alumni_name')
	alumni_count = alumni_list.count()
	research_list = ResearchTitle.objects.all().order_by('research_title')
	research_count = research_list.count()
	context = {
		'events_list': events_list, 'events_count': events_count,
		'news_list': news_list, 'news_count': news_count,
		'latest_news': latest_news, 'outreach_list': outreach_list,
		'outreach_count': outreach_count, 'alumni_list': alumni_list, 'alumni_count': alumni_count,
		'research_list': research_list, 'research_count': research_count
	}
	return render(request, template_name, context)


def postlist(request, string, template_name='website/post-list.html'):
	context = {}
	if string == 'News':
		context = NewsPost.objects.all().order_by('-news_date', '-news_time')
	if string == 'Events':
		context = UpcomingEvent.objects.all().order_by('event_date')
	if string == 'Outreach':
		context = OutreachPost.objects.all().order_by('-outreach_date')
	if string == 'Research':
		context = ResearchTitle.objects.all().order_by('research_title')
	if string == 'Alumni':
		context = Alumni.objects.all().order_by('alumni_name')

	page = request.GET.get('page', 1)
	paginator = Paginator(context, 10)

	try:
		content = paginator.page(page)
	except PageNotAnInteger:
		content = paginator.page(1)
	except EmptyPage:
		content = paginator.page(paginator.num_pages)
	return render(request, template_name, {'content': content, 'post': string})


def search(request, template_name='website/search.html'):
	if request.POST.get('keyword'):
		keyword = request.POST.get('keyword')
		request.session['key'] = keyword
		news_list = NewsPost.objects.filter(title__icontains=keyword)
		events_list = UpcomingEvent.objects.filter(title__icontains=keyword)
		out_list = OutreachPost.objects.filter(title__icontains=keyword)

		result_list = list(news_list) + list(events_list) + list(out_list)

		page = request.GET.get('page', 1)
		paginator = Paginator(result_list, 3)
		months = mkmonth_lst()

		try:
			news = paginator.page(page)
		except PageNotAnInteger:
			news = paginator.page(1)
		except EmptyPage:
			news = paginator.page(paginator.num_pages)

		data = {'news': news, "months": months, 'keyword': keyword}

		return render(request, template_name, data)
	elif request.session['key']:
		news_list = NewsPost.objects.filter(title__icontains=request.session['key'])
		events_list = UpcomingEvent.objects.filter(title__icontains=request.session['key'])
		out_list = OutreachPost.objects.filter(title__icontains=request.session['key'])

		result_list = list(news_list) + list(events_list) + list(out_list)

		page = request.GET.get('page', 1)
		paginator = Paginator(result_list, 3)
		months = mkmonth_lst()

		try:
			news = paginator.page(page)
		except PageNotAnInteger:
			news = paginator.page(1)
		except EmptyPage:
			news = paginator.page(paginator.num_pages)

		data = {'news': news, "months": months, 'keyword': request.session['key']}

		return render(request, template_name, data)
	else:
		return render(request, template_name, {})
