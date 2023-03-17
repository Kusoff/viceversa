from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	count_words = len(user_text.split()) #считаем количество слов в строке



	reversed_text = user_text[::-1] #переворачивает текст наоборот
	return render(request, 'reverse.html', {'usertext': user_text, 'reversed_text': reversed_text, 'count': count_words})