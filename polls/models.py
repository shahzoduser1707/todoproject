from django.db import models
from datetime import datetime
# Create your models here.




class todoModel(models.Model):
    todo_name = models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    description = models.TextField(default='write here')

    def __str__(self) -> str:
        return self.todo_name
