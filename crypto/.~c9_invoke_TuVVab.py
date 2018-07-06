from django.shortcuts import render
from . import blockchain
# from blockchain import newNode
from . import forms
import time
from django.http import HttpResponse
# Entry.objects.order_by('-headline')[0]

# Create your views here.
@login_required(login_url="/accounts/login/")

def sell_block(request):
    
    if request.method=='POST':
            mlist = [instance.sender.tostring(), instance.receiver.tostring(), instance.sender.tostring()]
        # getting last row data from transactions table
        
        form=forms.SellBlock(request.POST,request.FILES)
        
        if form.is_valid():
            
            instance = form.save(commit=False)
            
            # storing form data in a list
            mlist = [str(instance.data), str(instance.amount), str(instance.sender), str(instance.receiver)]
            ret = newNode(mlist)
            if (ret == true)
                # save to databse
                instance.data
                instance.save()            #save it
                return HttpResponse('DB')
            else
                # show error
                return HttpResponse('ERROR')
            # passing data through block class and returning node to node
            # node = blockchain.block(index=3, mlist[0], time.ctime(), mlist[1], mlist[2], mlist[3], previoushash='')              # index must be no of rows in the transactions list
            
            

    else:
        form = forms.SellBlock()
    
    return render(request,'crypto/sell_block.html',{'form':form})
    
    