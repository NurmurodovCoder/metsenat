from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'\+998\d{9}$',
    message="Telefon raqam xato: '+998xxxxxxxxx'"
)
class Donator(models.Model):
     
     status = (
          ('Yangi', 'Yangi'),
          ('Moderatsiya', 'Moderatsiya'),
          ('Tasdiqlangan', 'Tasdiqlangan'),
          ('Bekor qilingan', 'Bekor qilingan')
     )

     legil = (
          ('Yuridik', 'Yuridik'),
          ('Jismoniy', 'Jismoniy')
     )

     full_name = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=15)  # , validators=phone_validator
     company = models.CharField(max_length=100)
     balance = models.IntegerField(default=0)
     donat = models.IntegerField(default=0)

     legil = models.CharField(max_length=40, choices=legil)
     status = models.CharField(max_length=50, choices=status, default='Yangi')

     create_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.full_name
     
     @property
     def residual(self):
          residual = self.balance-self.donat
          if residual:
               return residual
          return 0
          


class Universitet(models.Model):
     title = models.CharField(max_length=300)

     def __str__(self):
          return self.title

class Student(models.Model):
     statuc = (
          ('Bakalavr', 'Bakalavr'),
          ('Magistr', 'Magistr')
     )

     full_name = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=15)  #  , validators=phone_validator
     universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE)
     statuc = models.CharField(max_length=20, choices=statuc)
     contract = models.IntegerField(default=0)
     balance = models.IntegerField(default=0)

     create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

     def __str__(self):
          return self.full_name
     
     @property
     def residual(self):  # qoldiq degani ekan - residual
          residual = self.contract-self.balance
          if residual:
               return residual
          return 0


class Donat(models.Model):
     donator = models.ForeignKey(Donator, on_delete=models.CASCADE, related_name='donator')
     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
     donate = models.IntegerField()
     create_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f"{self.donator} { self.student } ga { self.donate } sum pul otkazdi ."
     
     # def save(self, *args, **kwargs):
     #      if self.donator.residual >= self.donate and self.donate <= self.student.residual:
     #           print(self.donator.residual, '-------' ,self.donate, '--------', self.student.residual , 'True')
     #           super(Donat, self).save(*args, **kwargs)
     #      elif self.donator.residual < self.donate:
     #           print('Donatorni puli kam')
     #      elif self.donate > self.student.residual:
     #           print('Studentga bu pul kop')
     #      else:
     #           print(self.donator.residual, '-------' ,self.donate, '--------', self.student.residual, 'False')


