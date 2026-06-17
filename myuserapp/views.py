from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")

def contact(request):

    english = 70
    maths = 80
    science = 90

    total = english + maths + science
    percentage = total / 300 * 100

    if english < 33 or maths < 33 or science < 33:
        result = "Fail"
    else:
        result = "Pass"

    context = {
        'english': english,
        'maths': maths,
        'science': science,
        'total': total,
        'percentage': percentage,
        'result': result,
    }

    return render(request, 'ans.html', context)

    




    
