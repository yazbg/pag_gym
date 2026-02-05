from django.shortcuts import render

# Create your views here.
def my_view(request):
    machines = [
        {'title': 'Treadmill'},
        {'title': 'Exercise Bike'},
        {'title': 'Rowing Machine'},
    ]
    contex = {
        'machines': machines       
    }
    return render(request, 'machine_list.html', contex) #las vistas siempre retornan un render