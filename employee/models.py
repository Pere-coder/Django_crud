from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    owner = models.ForeignKey('auth.User', related_name='employees', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    
    
    
    # def save(self, *args, **kwargs):
        
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title}
    
    # def __str__(self):
    #     return self.eid + ' ' + self.ename
    
    
    class Meta:  
        db_table = "employee"  
        
       
  
    
    