from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {
            'name': 'Ashutosh',
            'age': 35,
        })