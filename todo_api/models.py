from django.db import models

# Create your models here.

class Todo(models.Model):

    status_option = (
    ('OPEN', 'OPEN'),
    ('WORKING', 'WORKING'),
    ('DONE', 'DONE'),
    ('OVERDUE','OVERDUE')
    )
    timestamp = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=status_option, default='OPEN')

    # function for interact model in with admin panal
    def __str__(self):
     return self.title

    
