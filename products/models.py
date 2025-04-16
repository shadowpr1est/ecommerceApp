from django.contrib import admin
from django.utils.timezone import now
from django.db import models

class Vacancy(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Имя и Фамилия")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    about = models.TextField(verbose_name="О себе")

    def __str__(self):
        return self.full_name


class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True, default="")
    def __str__(self):
        return f"{self.name}, {self.price}"


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150)
    user_id = models.IntegerField(null=True,blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.product.name}"



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('category',)
    search_fields = ('name',)


