from django.shortcuts import render

posts = [
    {
        'Student': 'Sreerag O B',
        'Department': 'CSE',
        'CGPA': '8.19',
        'date_posted': 'August 17, 2021'
    },
    {
        'Student': 'SIVA',
        'Department': 'CSE',
        'CGPA': '6.97',
        'date_posted': 'August 18, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'student/home.html', context)


def about(request):
    return render(request, 'student/about.html', {'title': 'About'})