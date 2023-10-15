from django.shortcuts import render

def main_page(request):
	menu = {"Главная":"/", "Каталог":"/catalog", "О сайте":"/about"}
	title = "Главная"
	data = {"title": title, "menu": menu}
	return render(request, "./index.html", context=data)

def catalog_page(request):
	menu = {"Главная":"/", "Каталог":"/catalog", "О сайте":"/about"}
	title = "Каталог"
	data = {"title": title, "menu": menu}
	return render(request, "./catalog.html", context=data)

def about_page(request):
	menu = {"Главная":"/", "Каталог":"/catalog", "О сайте":"/about"}
	title = "О компании"
	data = {"title": title, "menu": menu}
	return render(request, "./about.html", context=data)