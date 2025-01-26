from django.db import models


class Product(models.Model):
    slug = models.SlugField(verbose_name='Уникальное название', unique=True)
    title = models.CharField(verbose_name='Название товара',max_length=200)
    image = models.CharField(verbose_name='Изображение товара', max_length=200)
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(verbose_name='Цена' ,max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
    

class Order(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Телефон', max_length=20)
    basket = models.TextField(verbose_name='Корзина')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ No{self.id} {self.name} {self.surname} {self.phone}'
