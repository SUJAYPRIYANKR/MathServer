
from django.shortcuts import render

def churnrate(request):
    c = float(request.POST.get('custlost', '0'))
    i = float(request.POST.get('inicust', '0'))

    churnrate = c * i if request.method == 'POST' else 0

    print("customer lost =", c)
    print("initial customer =", i)
    print("churn rate =", churnrate)

    return render(
        request,
        'myapp/fungus.html',
        {'c': c, 'i': i, 'churnrate': churnrate}
    )