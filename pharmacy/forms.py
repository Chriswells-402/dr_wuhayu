#enabling a form where a user creates or imputa data

from django.forms import ModelForm
# accessing our models such thst wer link them to the form
from .models import *

#we are updating the already existing stock
class Addform(ModelForm):
    class Meta:
        model= Product
        fields= ['receivedQuantity']
#we model forms basing on our model for us to  record a given product sale
class Saleform(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','ammountReceived','issuedTo']        