from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    TRANSACTIO_TYPES = [
        ('INCOME','Income'),
        ('EXPENSE', 'Expense')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTIO_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=255)

    

    def __str__(self):
        return self.title
    

class Goal(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()

    def __str__(self):
        return self.name