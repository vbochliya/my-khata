from django.shortcuts import render,redirect,HttpResponse
from .models import khata_transactions,given_taken
from .forms import khata_transaction_form,given_taken_form
from django.db.models import Sum
from datetime import datetime


def index(request):
    return render(request, 'khata/index.html')
    
def show_khata(request,entry_type):
    if entry_type=='transactions':
        model_class=khata_transactions
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        if start_date and end_date:
            transactions = model_class.objects.filter(datetime__range=[start_date, end_date])
        else:
            transactions = model_class.objects.all()

        expenditures = transactions.values('catagory').annotate(total=Sum('ammount'))

        # Preparing data for the pie chart
        categories = [expenditure['catagory'] for expenditure in expenditures]
        totals = [expenditure['total'] for expenditure in expenditures]

        return render(request, 'khata/show_khata.html', {
            'transactions': transactions,
            'categories': categories,
            'totals': totals,
            'start_date': start_date,
            'end_date': end_date
        })


    elif entry_type=='given_taken':
        model_class=given_taken
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        if start_date and end_date:
            transactions = model_class.objects.filter(datetime__range=[start_date, end_date])
        else:
            transactions = model_class.objects.all()
        
        #-----------------------------------
        # Aggregate expenditures by category
        expenditures = transactions.values('catagory').annotate(total=Sum('ammount'))

        # Prepare data for the pie chart
        categories = [expenditure['catagory'] for expenditure in expenditures]
        totals = [expenditure['total'] for expenditure in expenditures]

        return render(request, 'khata/show_khata.html', {
            'transactions': transactions,
            'categories': categories,
            'totals': totals,
            'start_date': start_date,
            'end_date': end_date
        })


    else:
        return redirect('index')  


    




def new_entry(request,entry_type):
    if entry_type == 'transactions':
        form_class = khata_transaction_form
        heading="transation entries"
    elif entry_type == 'given_taken':
        form_class = given_taken_form
        heading="given_taken entries"
    else:
        return redirect('index')  
    

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_khata', entry_type=entry_type)
        else:
            return HttpResponse("the form is not valid")
    else:
        form = form_class() 
        return render(request, 'khata/new_entry.html', {'form': form,'heading':heading})

