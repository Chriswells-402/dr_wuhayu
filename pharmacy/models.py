from django.db import models

# Create your models here.
class Stock_Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    #this model gives human a readable name for the oblect of the class which is our category
    def __str__(self) :
        return self.name

#creating a class product inherited from superclass Model
class Product(models.Model):

    #conecting products model to stock category models using foreign key
    categoryName= models.ForeignKey(Stock_Category,on_delete=models.CASCADE,null=True, blank= True)    

    itemName=models.CharField(max_length=50, null=True, blank=True)
    totalQuantity= models.IntegerField(default=0, null=True, blank=True)
    issuedQuantity=models.IntegerField(default=0, null=True, blank=True)
    receivedQuantity=models.IntegerField(default=0, null=True, blank=True)
    unitPrice= models.IntegerField(default=0, null=True, blank=True)
    manufacturer= models.CharField(max_length=50, null=True, blank=True)
    brand= models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) :
        return self.itemName
    
class Sale(models.Model):
    #the item name, the price,purchsers name, date of purchase,
    # quantity purchased, VAT
    item = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity= models.IntegerField(default=0, null=False, blank=True)
    ammountReceived= models.IntegerField(default=0, null=False, blank=True)
    issuedTo = models.CharField(max_length=50, null=True, blank=True)
    unitPrice= models.IntegerField(default=0, null=True, blank=True)
    #date = models.DateTimeField(auto_now_add=True)
    #calculating the total
    def getTotal(self):
        total= self.quantity * self.item.unitPrice
        return int(total)
    #calculating the change
    def getChange(self):
        change = self.getTotal() - self.ammountReceived
        return abs(int(change))

    def __str__(self):
        return self.item.itemName    