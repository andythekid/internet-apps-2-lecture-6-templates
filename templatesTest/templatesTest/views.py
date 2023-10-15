from django.shortcuts import render

def main_page(request):
	text = "<h1>Main page<h1>"
	return render(request, "./index.html")