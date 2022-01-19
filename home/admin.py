from django.contrib import admin
from .models import (
  NewConnection,
  BookGas
)



# Register your models here.
@admin.register(NewConnection)
class NewConnectionModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','fname','lname','phoneno','email','gender','aadhaar','address','paymentOption']

@admin.register(BookGas)
class BookGasModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','billnum','gctype','accname','billdate','status','delivboy','expctdate','amount']

