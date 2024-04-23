from django.shortcuts import render
import razorpay
from .models import Food,Contact,Product_order,Register,Review
from math import ceil
import random
# Create your views here.
def searchMatch(query,item):
   if query in item.Food_Name.lower() or query in item.Category.lower() or query in item.sub_categoty.lower() or query in  Food_Description.lower():
      return True
   else:
      return False
def searchMatch1(query,item,a,b):
   if query in item.Food_Name.lower() or query in item.Category.lower() or query in item.Food_Description.lower() or query in item.sub_categoty.lower() and (int(a)<=int(item.price) and int(b)>=int(item.price) ):
      return True
   else:
      return False
def search(request,m):
   query=m
   aprod = []
   catprod = Food.objects.values('Category', 'id')
   cats = {item['Category'] for item in catprod}
   for cat in cats:
      prodtemp = Food.objects.filter(Category=cat)
      prod=[i for i in prodtemp if searchMatch(query,i)]
      n = len(prod)
      nos = n // 4 + ceil((n / 4) - (n // 4))
      if len(prod) != 0:
       aprod.append([prod, range(1, nos), nos])
   params = {'allprod': aprod,"msg":""}
   if len(aprod)==0 or len(query)<4:
         params={"msg":"Sorry, No item,we can add item in future"}
   return render(request, "shop/shop.html", params)
def searchu(request):
 if request.method=="POST":
   query=request.POST.get('search')
   query=query.lower()
   hj="minimal"
   print(query,hj)
   aprod = []
   catprod = Food.objects.values('Category', 'id')
   cats = {item['Category'] for item in catprod}
   for cat in cats:
      prodtemp = Food.objects.filter(Category=cat)
      prod=[i for i in prodtemp if searchMatch(query,i)]
      n = len(prod)
      nos = n // 4 + ceil((n / 4) - (n // 4))
      if len(prod) != 0:
       aprod.append([prod, range(1, nos), nos])
   params = {'allprod': aprod,"msg":""}
   if len(aprod)==0 or len(query)<4:
         params={"msg":"Sorry, No item,we can add item in future"}
   return render(request, "shop/shop.html", params)
 
def searchuu(request):
 if request.method=="POST":
   query=request.POST.get('category')
   pri=request.POST.get('price')
   pri=pri.lower()
   a=pri.split("-")
   query=query.lower()
   print(query,pri)
   aprod = []
   catprod = Products.objects.values('categoty', 'id')
   cats = {item['categoty'] for item in catprod}
   for cat in cats:
      prodtemp = Products.objects.filter(categoty=cat)
      prod=[i for i in prodtemp if searchMatch1(query,i,a[0],a[1])]
      n = len(prod)
      nos = n // 4 + ceil((n / 4) - (n // 4))
      if len(prod) != 0:
       aprod.append([prod, range(1, nos), nos])
   params = {'allprod': aprod,"msg":""}
   if len(aprod)==0 or len(query)<4:
         params={"msg":"Sorry, No item,we can add item in future"}
   return render(request, "shop/shop.html", params)
def index(request):
    return render(request,"shop/index.html")
def check(request):
    return render(request,"shop/order.html")
def contact(request):
   if request.method=="POST":
      name=request.POST.get('name')
      email = request.POST.get('email')
      mobile = request.POST.get('mob')
      a=int(len(mobile))
      if a<10 or a>10:
         print(len(mobile))
         return render(request, "shop/contact.html",{"error":"Invalid mobile Number"} )

      msg = request.POST.get('con')
      con=Contact(Name=name,Email=email,Mobile=mobile,Message=msg)
      con.save()
      return render(request, "shop/contact.html", {'error': 'Succesfully send'})
   else:
     return render(request,"shop/contact.html",{'error':'none'})
def tracking(request):
    return render(request,"shop/tracking.html")
def cart(request):
    return render(request,"shop/cart.html")
from django.conf import settings
def checkout(request):
       client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
       pay=client.order.create({"amount":100,'currency':'INR','payment_capture':1})
       print("##########")
       print(pay['id'])
       print("##########")
       par={"pay":pay}
       return render(request,"shop/checkout.html",par)
def product(request,id):
      myid=id
      products=Food.objects.filter(id=myid)
      aprod = []
      catprod = Food.objects.values('Category', 'id')
      cats = {item['Category'] for item in catprod}
      for cat in cats:
          prod = Food.objects.filter(Category=products[0].Category)
          n = len(prod)
          nos = n // 4 + ceil((n / 4) - (n // 4))
          aprod.append([prod, range(1, nos), nos])
      print(products[0].Category)
      return render(request, "shop/product.html", {'product': products[0], 'allprod': aprod})
def products(request,id):
      myid=id
      products=Food.objects.filter(id=myid)
      aprod = []
      catprod = Food.objects.values('Category', 'id')
      cats = {item['Category'] for item in catprod}
      for cat in cats:
          prod = Food.objects.filter(Category=products[0].Category)
          n = len(prod)
          nos = n // 4 + ceil((n / 4) - (n // 4))
          aprod.append([prod, range(1, nos), nos])
      print(products[0].Category)
      return render(request, "shop/product.html", {'product': products[0], 'allprod': aprod})
def shop(request):
    login = 'true'
    aprod = []
    catprod = Food.objects.values('Category', 'id')
    cats = {item['Category'] for item in catprod}
    for cat in cats:
        prod = Food.objects.filter(Category=cat)
        n = len(prod)
        nos = n // 4 + ceil((n / 4) - (n // 4))
        aprod.append([prod, range(1, nos), nos])
    params = {'allprod': aprod}
    return render(request,"shop/shop.html",params)
thanks=1
def orderNow(request):
   if request.method == 'POST':
      t=0
      fname=request.POST.get('fname')
      email = request.POST.get('email')
      mobile = request.POST.get('mobile')
      address = request.POST.get('address')
      city = request.POST.get('city')
      state = request.POST.get('state')
      zip = request.POST.get('zip')
      country = request.POST.get('country')
      items=request.POST.get('items')
      mode=request.POST.get('mode')
      f=items.split("{<>}")
      print(fname,email,mobile,address,city,state,zip,items)
      if items!='':
       for i in f:
         if i !="":
          opp=i.split("{}")
          print(opp)
          order=Product_order(Name=fname,Email=email,Mobile=mobile,Address=address,City=city,State=state,Zip=zip,Orders_name=opp[0],Orders_quantity=opp[1],Orders_price=opp[2],Orders_img=opp[4],Country=country,Orders_mode=mode)
          order.save()
   
       return render(request, "shop/confirmation.html")
       request.method ='GET'
      if items!='' and thanks % 2 != 0:
         return render(request,"shop/index.html")
      else:
         return render(request,"shop/index.html")
   else:
      return render(request, "shop/index.html")
def order(request):
 if request.method == 'POST':
   email = request.POST.get('email')
   print(email)
   products=Product_order.objects.filter(Email=email)
   a=[]
   sk={}
   if len(products)<0:
     msg='none'
   else:
      msg='true'
      for items in products:
           a.append([items.Orders_img,items.Orders_name,items.Orders_price,items.Date,items.order_Description])
      a.reverse()
      print(a)
   return render(request, "shop/order.html",{'product':a,'msg':msg})
def delete(request,id):
   myid=id
   products=Order.objects.filter(orderid=myid)
   products[0].delete()
   return render(request, "shop/index.html")
def register(request):
   if request.method=="POST":
      name=request.POST.get('name')
      email = request.POST.get('email')
      pas = request.POST.get('pass')
      mobile = request.POST.get('mobile')
      address = request.POST.get('address')
      check=Register.objects.filter(email=email)
      print(len(check))
      if(len(check)==0):
        con=Register(Name=name,email=email,password=pas,Mobile=mobile,Address=address)
        con.save()
        return render(request, "shop/login.html", {'error': 'Successfully Added'})
      else:
         return render(request, "shop/login.html", {'error': 'none'})
def login(request):
   if request.method=="POST":
      email=request.POST.get('email')
      pas = request.POST.get('pass')
      print(email,pas)
      con=Register.objects.filter(email=email,password=pas)
      print(len(con))
      if(len(con)>0):
             return render(request,"shop/index.html")
      else:
         return render(request,"shop/login.html")
   else:
      return render(request,"shop/login.html")
def lo(request):
   return render(request,"shop/login.html")
def review(request):
   if request.method=="POST":
      name=request.POST.get('name')
      rating = request.POST.get('rating')
      review = request.POST.get('review')
      idd = request.POST.get('idd')
      print(name,rating,review,idd)
      con=Review(Name=name,product_id=idd,rating=rating,review=review)
      con.save()
      myid=idd
      aprod = []
      catprod = Review.objects.values('product_id', 'id')
      cats = {item['id'] for item in catprod}
      for cat in cats:
        prod = Review.objects.filter(product_id=myid)
      n = len(prod)
      nos = n // 4 + ceil((n / 4) - (n // 4))
      aprod.append([prod, range(1, nos), nos])
      products=Products.objects.filter(id=myid)
      return render(request,"shop/product-details.html",{'product':products[0],'allprod': aprod})