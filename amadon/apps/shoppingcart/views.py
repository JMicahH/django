from django.shortcuts import render, HttpResponse, redirect

# asdfCreate your views here.
def index(request):

    return render(request,'shoppingcart/index.html')

def purchase(request):
    products = {
        '1001' : {
            'name'  : 'Dojo T-Shirt',
            'price' : '19.99',
        } 
        '1002' : {
            'name'  : 'Dojo Sweater',
            'price' : '29.99',
        } 
        '1003' : {
            'name'  : 'Dojo cup',
            'price' : '4.99',
        } 
        '1004' : {
            'name'  : 'Algorithm Book',
            'price' : '49.99',
        } 
    }
    
    product_id = request.POST['product_id']
    print products[product_id]

    return redirect('/process')

def process(request):

    return render(request, 'shoppingcart/checkout.html')