from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
# Create your views here.
def Home(request):
    return render(request,'home.html')
def Customers(request):
    customers=customerdetail.objects.all()
    return render(request,'customers.html',{'customers':customers})
def Transfer(request):  
    customers=customerdetail.objects.all()
    if request.method == "POST":
        int_email=request.POST.get('email')
        send_email=request.POST.get('sender_email')
        amount=request.POST.get('amount')
        print(int_email)
        print(amount)
        print(send_email)
        amount=int(amount)
        
        if int_email == send_email:
            messages.info(request,"EmailId not selected or both EmailId's are same")  
        elif amount <= 0:
            messages.info(request,'Please provide valid money details!!')
        else:
            for c in customers:
                if c.email==int_email:
                    i=c.id
                    s_name=c.name
                    if amount > c.balance:
                        messages.info(request,"Insufficient Balance!!")   
                    break

        for x in customers:
            if x.email==send_email:
                rid=x.id
                r_name=x.name
                rbal=x.balance
                break
 
        for c in customers: 
            if c.email==int_email and send_email!=int_email and amount<=c.balance and amount>0:
                q1= transferdetail(name=r_name,sender_name=s_name,amount=amount)
                balance=c.balance-amount
                q2=customerdetail.objects.filter(id=i).update(balance=balance)
                q1.save()
                balance=rbal+amount
                q3=customerdetail.objects.filter(id=rid).update(balance=balance)
                messages.info(request,"Transfer complete!!")
                return redirect('/transfer')
    return render(request,'transfer.html',{'customers':customers})
def Transaction(request):
    transaction=transferdetail.objects.all()
    return render(request,'transaction.html',{'transaction':transaction})