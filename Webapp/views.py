from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework import status,generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employee
from .serializers import employeeSerializer

#GENERICS AND MIXINS
'''------------------------------------------------'''
class employeeList(generics.GenericAPIView,mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = employeeSerializer
    queryset = employee.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        print(request.data)
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)
'''--------------------------------------------------'''


#CLASS BASED VIEW
'''---------------------------------------------------'''
# class employeeList(APIView):
#     def get(self,request):
#         employees1=employee.objects.all()
#         serializer=employeeSerializer(employees1,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         data=request.data
#         serializer=employeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
# class employeeDetailList(APIView):
#     def get_object(self,id=None):
#         return get_object_or_404(employee,id=id)
#
#     def get(self,request,id=None):
#         instance=self.get_object(id)
#         serializer=employeeSerializer(instance)
#         return Response(serializer.data)
#
#     def put(self,request,id=None):
#         instance=self.get_object(id)
#         data=request.data
#         serializer=employeeSerializer(instance,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def delete(self,request,id=None):
#         instance=self.get_object(id)
#         instance.delete()
#         return HttpResponse(201)


