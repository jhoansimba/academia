from django.shortcuts import render, HttpResponse

class direccionController():

    def index (request):
        return render(request,'views/default/direccion.html')
        #return HttpResponse ('<h5>jhoan</h5>')
    
