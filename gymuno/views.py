from django.shortcuts import render

# Create your views here.
def my_view(request):

    
    return render(request, 'machine_list.html') #las vistas siempre retornan un render
