from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import StudentSerializers, DonatorSerializers, DonatSerializers, UniversitetSerializers, StudentCreateSerializers, DonatorCreateSerializers
from .models import Student, Donat, Donator ,Universitet
from rest_framework.decorators import api_view


from rest_framework.views import APIView
from django.db.models import Sum


from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

class UniversitetView(viewsets.ModelViewSet):
     queryset = Universitet.objects.all()
     serializer_class = UniversitetSerializers


class StudentView(viewsets.ModelViewSet):
     queryset = Student.objects.all()
     serializer_class = StudentSerializers

     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['universitet', 'statuc']

     def create(self, request, *args, **kwargs):
          serializer = StudentCreateSerializers(data=request.data)
          serializer.is_valid(raise_exception=True)
          self.perform_create(serializer)
          headers = self.get_success_headers(serializer.data)
          return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DonatView(viewsets.ModelViewSet):
     queryset = Donat.objects.all()
     serializer_class = DonatSerializers


class DonationsView(APIView):
    
    @swagger_auto_schema(request_body=DonatSerializers)
    def get(self, request):
        r = request.GET
        student_id = r['student_id']
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializers(student)
        donation = student.student.all()
        serializer_donations = DonatSerializers(donation, many=True)

        return Response({
            'student': serializer.data,
            'donations': serializer_donations.data
        })

    @swagger_auto_schema(request_body=DonatSerializers)
    def post(self, request):
        
        r = request.data.get
        student_id = r('student_id')
        sponsor_id = r('sponsor_id')
        summa = int(r('summa'))
        sponsor = Donator.objects.get(id=sponsor_id)
        student = Student.objects.get(id=student_id)

        if sponsor.residue >= summa and summa <= student.residual:
               donation = Donat.objects.create(student=student, donator=sponsor, donate=summa)
        
        elif sponsor.residual < summa:
               return Response({'result': "Homiymizda buncha pul yoq"})
        
        elif student.residual > summa:
               return Response({'result': "Contrakt pulidan kop pul bu"})
        else:
          return Response({'result': "xxxxxxxxxxx"})
        serializer = DonatSerializers(donation).data
        
        return Response(serializer)


class DonatorView(viewsets.ModelViewSet):
     queryset = Donator.objects.all()
     serializer_class = DonatorSerializers

     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['status', 'balance', 'create_at']


     def create(self, request, *args, **kwargs):
          serializer = DonatorCreateSerializers(data=request.data)
          serializer.is_valid(raise_exception=True)
          self.perform_create(serializer)
          headers = self.get_success_headers(serializer.data)
          return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
     



@api_view(['GET'])
def dashboard(request):
     donat_total = Donat.objects.aggregate(total=Sum('donate'))['total']
     contract_total = Student.objects.aggregate(total=Sum('contract'))['total']
     money = contract_total - donat_total

     count_sponsor = {}
     count_student = {}

     for i in range(1, 13):
          sponsor = Donator.objects.filter(create_at__month=i).count()
          student = Student.objects.filter(create_at__month=i).count()

          count_sponsor[i]=sponsor
          count_student[i]=student

     return Response({
          'donat_total': donat_total,
          'contract_total': contract_total,
          'money': money,
          'count_sponsor':count_sponsor,
          'count_student':count_student
          
          })  # , 'donat': serializer_donat.data, 'contract': serializer_contract.data})




#     donat_queryset = Donat.objects.all()
#     student_queryset = Student.objects.all()

#     serializer_donat = DonatSerializers(donat_queryset, many=True)
#     serializer_contract = StudentSerializers(student_queryset, many=True)
