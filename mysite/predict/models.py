from django.db import models

# Create your models here.
class ModelBase(models.Model):
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateField(auto_now = True)
    modifed_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True
    
    def delete(self, *args, **kwargs):
        """Soft Delete"""
        self.is_deleted = True
        self.save()

class User(ModelBase):
    user_id = models.CharField()

class Historical(ModelBase):
    stock_id = CharField(max_length = 10)

class historical_stock_price(ModelBase):
    historical = models.ForeignKey(Historical, on_delete=models.CASCADE)
    close_price = models.FloatField(default = 0.0)
    datetime = models.DateTimeField('date recorded')

class Realtime(ModelBase):
    pass

    
