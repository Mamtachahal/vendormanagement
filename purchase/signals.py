
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from vendor.models import PurchaseOrder, Vendor,StatusChoice
from django.db.models import Avg, Count, F, Sum


@receiver(pre_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance: PurchaseOrder, **kwargs):
    if instance.status != StatusChoice.COMPLETED:
        return
    vendor = instance.vendor
    if not instance.pk:
        return
    old_instance = PurchaseOrder.objects.get(pk=instance.pk)
    if old_instance.status !=instance.status:
        old_average_on_time_delivery_rate = vendor.on_time_delivery_rate # 1
        old_total_completed_order = PurchaseOrder.objects.filter(status = StatusChoice.COMPLETED,vendor_id=vendor.pk).count() # 3
        old_total_on_time_completed_order = old_average_on_time_delivery_rate*old_total_completed_order # 3
        is_current_order_on_time = True if old_instance.delivery_date >= instance.delivery_date else False
        new_total_completed_order = old_total_completed_order + 1 
        new_total_on_time_completed_order = old_total_on_time_completed_order + 1 if is_current_order_on_time else old_total_on_time_completed_order 
        new_average_on_time_delivery_rate = new_total_on_time_completed_order / new_total_completed_order
        vendor.on_time_delivery_rate = new_average_on_time_delivery_rate
        vendor.save()


@receiver(pre_save, sender=PurchaseOrder)
def update_vendor_quality_rating(sender, instance: PurchaseOrder, **kwargs):
    vendor = instance.vendor
    if not instance.pk:
        return
    old_instance = PurchaseOrder.objects.get(pk=instance.pk)

    if instance.quality_rating != old_instance.quality_rating:
        old_quality_rating_average = vendor.quality_rating_avg
        old_rating_count = PurchaseOrder.objects.filter(vendor_id=vendor.pk, status=StatusChoice.COMPLETED).exclude(quality_rating__isnull=True).count()
        old_quality_rating = old_quality_rating_average * old_rating_count

        current_quality_rating = old_quality_rating + instance.quality_rating
        current_quality_rating_count = old_rating_count + 1
        current_quality_rating_average = current_quality_rating / current_quality_rating_count

        vendor.quality_rating_avg = current_quality_rating_average
        vendor.save()
    
@receiver(pre_save, sender=PurchaseOrder)
def update_vendor_average_response_time(sender, instance: PurchaseOrder, **kwargs):
    vendor = instance.vendor
    if not instance.pk:
        return
    old_instance = PurchaseOrder.objects.get(pk=instance.pk)
    
    if instance.acknowledgment_date !=  old_instance.acknowledgment_date:
        old_average_response_time = vendor.average_response_time
        print(instance.acknowledgment_date,instance.issue_date)
        issue_date = instance.issue_date.replace(tzinfo=None)

        current_response_time = (instance.acknowledgment_date - issue_date).total_seconds() / 3600
        total_orders = PurchaseOrder.objects.filter(vendor_id=vendor.pk, acknowledgment_date__isnull=False).count()
        new_average_response_time =  (current_response_time + old_average_response_time*total_orders) / (total_orders + 1)
        vendor.average_response_time = new_average_response_time
        vendor.save()
    

@receiver(pre_save, sender=PurchaseOrder)
def update_vendor_fulfillment_rate(sender, instance: PurchaseOrder, **kwargs):
    vendor = instance.vendor
    if not instance.pk:
        return
    old_instance = PurchaseOrder.objects.get(pk=instance.pk)
    
    if old_instance.status !=instance.status:
        completed_order_count = PurchaseOrder.objects.filter(status=StatusChoice.COMPLETED, vendor_id=vendor.pk).count()
        total_order_count = PurchaseOrder.objects.filter(vendor_id=vendor.pk).count()

        vendor.fulfillment_rate = completed_order_count / total_order_count
        vendor.save()
    






