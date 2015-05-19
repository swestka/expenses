__author__ = 'doe'
import django

from django.db import models

class Transaction(models.Model):
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=19, decimal_places=2)

class Currency(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Debt(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=2)
    maturity = models.DateTimeField()

class Loan(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=2)
    maturity = models.DateTimeField()

class Installment(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=2)
    date = models.DateTimeField()



