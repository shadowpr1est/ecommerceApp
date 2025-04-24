from django.contrib import admin
from django.utils.timezone import now
from django.db import models

from django.db import models
from django.utils.timezone import now
from decimal import Decimal
# models.py

from django.db import models
from django.utils.timezone import now
from decimal import Decimal

class Vacancy(models.Model):
    full_name = models.CharField("ФИО", max_length=150)
    phone_number = models.CharField("Телефон", max_length=20)
    about = models.TextField("О себе")

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название", max_length=150)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True,related_name="products")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField("Скидка %", default=0)
    image = models.ImageField("Изображение", upload_to="products/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} — {self.total_price} тг"

    @property
    def total_price(self):
        return self.price - self.price * self.discount/100


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField("Имя пользователя", max_length=150)
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} → {self.product.name}"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('cat',)
    search_fields = ('name',)
