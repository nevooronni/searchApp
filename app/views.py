from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,Http404
import datetime as dt
from .models import Article

# Create your views here.
def index(request):
	return render(request, 'index.html')

def index(request):
	date = dt.date.today()
	news = Article.todays_news()
	return render(request,'index.html',{"date":date,"news":news})

def article(request,article_id):#pass in artitcle id from url 
	try:
		article = Article.objects.get(id = article_id)#query db for article
	except DoesNotExist:#catch the does not exist expection when we fail to find object with the id and throw a 404 error 
		raise Http404()
	return render(request,"all-news/article.html",{"article":article})	

def search_results(request):

	if 'article' in request.GET and request.GET["article"]:#we first check if the article query exists in our request.GET object
		search_term = request.GET.get("article")#get the search term using the request.GET object
		searched_articles = Article.search_by_category(search_term)#search the user input
		message = f"{search_term}"

		return render(request,'search.html',{"message":message,"articles":searched_articles})

	else:
		message = "You haven't searched for any term"
		return render(request,'search.html',{"message":message})
