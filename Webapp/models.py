from django.db import models

class employee(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    photo=models.ImageField(upload_to='images',)

    def __str__(self):
        return self.first_name+self.last_name
