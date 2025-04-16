from django.urls import path
from .views import RegisterView,DashboardView,TransactionCreationView,TransactionListView,GoalCreationView,export_transactions,home_view
urlpatterns = [
    path('', home_view, name='home'),  # New home view for root URL
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('tansaction/add/', TransactionCreationView.as_view(), name='transaction_add'),
    path('tansactions/', TransactionListView.as_view(), name='transaction_list'),
    path('goal/add/', GoalCreationView.as_view(), name='goal_add'),
    path('generate-report/', export_transactions, name='export_transactions'),

]
