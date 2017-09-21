from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
        request.session['grandtotal'] = 0
    return render(request, 'shoppingcart/index.html')

def purchase(request):
    products = {
        '1001' : {
            'name'  : 'Dojo T-Shirt',
            'price' : '1999'
        }, 
        '1002' : {
            'name'  : 'Dojo Sweater',
            'price' : '2999'
        }, 
        '1003' : {
            'name'  : 'Dojo cup',
            'price' : '499'
        }, 
        '1004' : {
            'name'  : 'Algorithm Book',
            'price' : '4999'
        }, 
    }
    
    product_id = request.POST['product_id']
    quantity = int(request.POST['quantity'])
    product_price = int(products[product_id]['price'])


    request.session['total'] = float(product_price * quantity)/100
    request.session['count'] += quantity
    request.session['grandtotal'] += request.session['total']
    return redirect('/checkout')

def checkout(request):

    return render(request, 'shoppingcart/checkout.html')

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    print request.session
    return redirect('/')