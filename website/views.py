from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.
def index (request):
    records = Record.objects.all()
    if request.method == 'POST':
       username = request.POST ['username']
       password = request.POST ['password']

       user = authenticate(request, username = username, password = password)
       if user is not None:
           login(request, user)
           messages.success(request, "You Have Beeen IN !")
           return redirect('index')
       else:
           messages.success(request, "Invalid Credentials")
           return redirect('index')
    else :
        return render(request, 'index.html', {'records' :records})


    


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out !')
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Been Registered!')
            return redirect('index')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})  # Corrigé et repositionné



def constumer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You Must Be Login To View This Page !')
        return redirect('index')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Has Been Deleted !')
        return redirect ('index')
    else:
        messages.success(request, 'You must be login before to delete record !')
        return redirect('index')



def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save ()
                messages.success(request, 'Record Has Been Added !')
                return redirect ('index')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, 'You Must Be Login To Add Record !')
        return redirect('index')
    


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Has Been Updated !')
            return redirect ('index')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'You Must Be Login To Update Record !')
        return redirect('index')