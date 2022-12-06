from django.db import models

# Create your models here.
class query(models.Model):
    Name = models.CharField(max_length=30,blank=False,null=False),
    Contact = models.IntegerField(max_length=10,blank=False,null=False)
    From = models.CharField(max_length=30,blank=False,null=False)
    To = models.CharField(max_length=30,blank=False,null=False)
    Date = models.DateField(auto_now=False,auto_now_add=False)

    class Meta:
        db_table = 'query'