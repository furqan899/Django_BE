from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        get_latest_by = 'created_at'

class Category(TimeStampedModel):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(TimeStampedModel):
    """
    Model representing a product.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name

class Order(TimeStampedModel):
    """
    Model representing a customer order.
    """
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"
