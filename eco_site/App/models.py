from django.db import models

class AddCatagoryModel(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=20)
    Category_image=models.ImageField(upload_to='admin/product_category',null=True,blank=True)
    Category_desc=models.TextField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.category_name

class AddProductModell(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=20)
    product_image=models.ImageField(upload_to='admin/add_product',null=True,blank=True)
    product_origonal_price=models.CharField(max_length=20)
    product_discounted_price=models.CharField(max_length=20)
    product_category=models.ForeignKey(AddCatagoryModel,on_delete=models.CASCADE)
    product_description=models.TextField(max_length=200)

