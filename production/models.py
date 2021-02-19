from django.db import models

# Create your models here.
class Production(models.Model):
    env = models.CharField(max_length=50, blank=False, default= 'Production')
    Q1 = models.CharField(max_length=50, blank=True, default= '')
    Q2 = models.CharField(max_length=50, blank=True, default='')
    Q3 = models.CharField(max_length=50, blank=True, default='')
    Q4 = models.CharField(max_length=50, blank=True, default='')
    LQA = models.CharField(max_length=50, blank=False, default= 'Q1')#ultima intrebare pusa
    Status= models.CharField(max_length=50, blank=False, default='a')  # la ce intrebare a parasit linkul

    def __str__(self):
        return self.env+self.id

    class Meta:
        ordering = ('id', )