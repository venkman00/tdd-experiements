from django.shortcuts import render

def home_page(request):
    print("'someone's here")
    return render(request, "home.html")

