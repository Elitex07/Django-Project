from django.db import models
from django.contrib.auth.models import User
'''from django.core.validators import MaxValueValidator, MinValueValidator ''' 

# Create your models here.
GENDER_OPTS= (
  ('M','male'),
  ('F','female'),
  ('N','none')
)
PAY_OPTS=(
  ('cod','CashOnDelivery'),
  ('upi','UPI')
)
GCTYPE=(
  ('7.8kg','7.8kg'),
  ('10.3kg','10.3kg'),
  ('14.2kg','14.2kg'),
)
BOOK_STATUS=(
  ('pending','pending'),
  ('confirmed','confirmed'),
  ('failed','failed'),
  ('on delivery','on delivery'),
  ('delivered','delivered')
)
PAYMENT_STATUS=(
  ('pending','pending'),
  ('payed','payed'),
  ('failed','failed'),
)
class NewConnection(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  fname = models.CharField(max_length = 20)
  lname = models.CharField(max_length = 20)
  phoneno = models.IntegerField()
  email = models.CharField(max_length = 20)
  gender = models.CharField(choices=GENDER_OPTS,max_length=1,default='N')
  aadhaar = models.IntegerField()
  address = models.TextField(max_length = 100)
  zipcode = models.CharField(max_length = 6)
  paymentOption = models.CharField(choices=PAY_OPTS,max_length=3,default='cod')
  def __str__(self):
    return str(self.id)

class BookGas(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  billnum = models.CharField(max_length = 20)
  gctype = models.CharField(choices=GCTYPE,max_length=7,default='a')
  accname = models.CharField(max_length = 40)
  billdate = models.CharField(max_length = 30)
  status = models.CharField(choices=BOOK_STATUS,max_length=30,default='pending')
  delivboy = models.CharField(max_length = 30)
  expctdate = models.CharField(max_length = 30)
  amount = models.IntegerField()
  payment = models.CharField(choices=PAYMENT_STATUS,max_length=30,default='pending')
  def __str__(self):
    return str(self.id)

