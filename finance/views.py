from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.views import View
from .forms import RegisterForm,TransactionForm,GoalForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Transaction,Goal
from .admin import TransactionResource
from django.db.models import Sum
import csv
# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('login')  # Make sure 'login' is a valid URL name
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'register.html', {'form': form})
    

def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('register')



class DashboardView(View, LoginRequiredMixin):
    def get(self,request, *args, **kwargs):
        transactions = Transaction.objects.filter(user = request.user)
        transactions = transactions.order_by('-date')[:10]
        goals = Goal.objects.filter(user = request.user)
        
        #Calculate total income
        total_income = Transaction.objects.filter(user = request.user, transaction_type = 'INCOME').aggregate(Sum('amount'))['amount__sum'] or 0

        #Calculate total expense
        total_expense = Transaction.objects.filter(user = request.user, transaction_type = 'EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
        
        #Calculate Net Saving
        net_saving = total_income - total_expense

        remaining_savings =net_saving

        goal_progress =[]
        for goal in goals:
            if remaining_savings >= goal.target_amount:
                goal_progress.append({'goal':goal,'progress':100})
                remaining_savings -= goal.target_amount
            elif remaining_savings > 0:
                progress = (remaining_savings / goal.target_amount)*100
                goal_progress.append({'goal':goal,'progress':progress})
                remaining_savings = 0
            else:
                goal_progress.append({'goal':goal,'progress':0})

        context = {
            'transactions':transactions,
            'total_income':total_income,
            'total_expense':total_expense,
            'net_saving':net_saving,
            'goal_progress':goal_progress
        }

        return render(request, 'dashboard.html',context)
    

class TransactionCreationView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'transactionform.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            try:
             
             # Create transaction but don't save to DB yet
             transaction = form.save(commit=False)
            # Assign the current user
             transaction.user = request.user
            # Now save to DB
             transaction.save()
             
             messages.success(request, "Transaction added successfully!")
             return redirect('dashboard')
            
            except Exception as e:
                messages.error(request, f"Error saving transaction: {str(e)}")
                return render(request, 'transactionform.html', {'form': form})
        
            # Form is invalid
        messages.error(request, "Please correct the errors below.")
        return render(request, 'transactionform.html', {'form': form})
    

class TransactionListView(LoginRequiredMixin, View):
    def get(self,request, *args, **kwargs):
        transaction = Transaction.objects.all()
        return render(request, 'transaction_list.html',{'transactions':transaction})
    

class GoalCreationView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        form = GoalForm()
        return render(request, 'goalform.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            try:
             
             # Create transaction but don't save to DB yet
             transaction = form.save(commit=False)
            # Assign the current user
             transaction.user = request.user
            # Now save to DB
             transaction.save()
             
             messages.success(request, "Goal added successfully!")
             return redirect('dashboard')
            
            except Exception as e:
                messages.error(request, f"Error adding goal: {str(e)}")
                return render(request, 'goalform.html', {'form': form})
        
            # Form is invalid
        messages.error(request, "Please correct the errors below.")
        return render(request, 'transactionform.html', {'form': form})
    

def export_transactions(request):
    user_transactions = Transaction.objects.filter(user = request.user)
    transaction_resource = TransactionResource()
    dataset = transaction_resource.export(queryset=user_transactions)

    excel_data = dataset.export('xlsx')

    # Create an Httpresponse with correct MIME type for an Excel file/CSV file
    response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Set the header for downloading the file
    response['Content-Disposition'] = 'attachment;filename=transactions_report.xlsx'
    return response

