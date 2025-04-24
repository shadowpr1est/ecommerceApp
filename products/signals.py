from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product


@receiver(pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Product.objects.get(pk=instance.pk).image
    except Product.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if old_file:
            old_file.delete(save=False)
