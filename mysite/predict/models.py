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
    pass

class Realtime(ModelBase):
    pass

    
