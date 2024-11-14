from django.db import models

# Create your models here.
from django.db import models

class ATM:
    def __init__(self, B_Name="BOM", Pin=1234, Balance=20000):
        self.__BankName = B_Name
        self.__Pin = Pin
        self.__Balance = Balance

    def verify_pin(self, input_pin):
        return self.__Pin == input_pin

    def withdraw(self, amount):
        if self.__Balance >= amount:
            self.__Balance -= amount
            return True, self.__Balance
        return False, self.__Balance

    def check_balance(self):
        return self.__Balance
