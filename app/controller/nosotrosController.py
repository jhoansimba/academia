from django.shortcuts import render, HttpResponse

class nosotrosController():

    def index (request):
        return render(request,'views/nosotros/nosotros.html')
        #return HttpResponse ('<h5>jhoan</h5>')