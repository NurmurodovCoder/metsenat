# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from rest_framework.response import Response
# from .models import Donat


# @receiver(pre_save, sender=Donat)
# def my_model_pre_save(sender, instance, *args, **kwargs):
#      if instance.donator.residual >= instance.donate and instance.donate <= instance.student.residual:
#           super(Donat, instance).save(*args, **kwargs)

#      elif instance.donator.residual < instance.donate:
#           return Response({"message":'Donatorni puli kam'})
#      elif instance.donate > instance.student.residual:
#           # response = {'message': 'Delete function is not offered in this path.'}
#           # return Response(response, status=status.HTTP_403_FORBIDDEN)
#           return Response({"message":'Studentga bu pul kop'})
#      else:
#           return Response({"message":'Xatolik'})





    #      if self.donator.residual >= self.donate and self.donate <= self.student.residual:
     #           print(self.donator.residual, '-------' ,self.donate, '--------', self.student.residual , 'True')
     #           super(Donat, self).save(*args, **kwargs)
     #      elif self.donator.residual < self.donate:
     #           print('Donatorni puli kam')
     #      elif self.donate > self.student.residual:
     #           print('Studentga bu pul kop')
     #      else:
     #           print(self.donator.residual, '-------' ,self.donate, '--------', self.student.residual, 'False')
