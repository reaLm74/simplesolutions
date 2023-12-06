from django.db import models

currency = [
        ("USD", "usd"),
        ("EUR", "eur"),
    ]


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, choices=currency)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


class Order(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='order',
        verbose_name='Order'
    )


class Discount(models.Model):
    discount = models.CharField(max_length=10)
