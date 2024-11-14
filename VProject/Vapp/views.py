from django.shortcuts import render, redirect
from .models import ATM

# Create an instance of the ATM model (assumed to be a singleton)
atm = ATM()

def home(request):
    return render(request, 'home.html')

def verify(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if pin.isdigit():
            pin = int(pin)
            if atm.verify_pin(pin):
                return redirect('dashboard')
            else:
                return render(request, 'home.html', {'error': 'Invalid PIN!'})
        else:
            return render(request, 'home.html', {'error': 'PIN must be a number!'})
    return redirect('home')

def dashboard(request):
    balance = atm.check_balance()
    return render(request, 'dashboard.html', {'balance': balance})

def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount.isdigit():
            amount = int(amount)
            success, balance = atm.withdraw(amount)
            if success:
                return render(request, 'dashboard.html', {
                    'message': 'Withdrawal successful!',
                    'balance': balance
                })
            else:
                return render(request, 'dashboard.html', {
                    'error': 'Insufficient balance!',
                    'balance': atm.check_balance()
                })
        else:
            return render(request, 'dashboard.html', {
                'error': 'Amount must be a number!',
                'balance': atm.check_balance()
            })
    return redirect('dashboard')

def check_balance(request):
    balance = atm.check_balance()
    return render(request, 'dashboard.html', {'balance': balance})

