from django.shortcuts import render

def power(request):
    if request.method=='POST':
        intesity_value=int(request.POST.get('intensity-input'))
        resistance_value=int(request.POST.get('resistance-input'))
        power = (intesity_value ** 2) * resistance_value
        return render(request, 'index.html',{'output':power})
    return render (request, 'index.html')