from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import employeeSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

# Create your views here.
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('empDetail')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form':form})


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()    
    serializer_class = UserSerializer
    
    

class employeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class employeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()    
    serializer_class = employeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  
  
  
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': reverse('user-list', request=request, format=format),
            'employees': reverse('empList', request=request, format=format)
        
        }
    )
  
  
from rest_framework import renderers

# class  EmployeeHighlight(generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]
    
#     def get(self, request, *args, **kwargs):
#         employee = self.get_object()
#         return Response(employee.highlighted)
    
    

    

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
# class employeeList(APIView):
    
#     def get(self, request, format=None):
#         employees = Employee.objects.all()
#         serializer = employeeSerializer(employees, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = employeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class employeeDetail(APIView):
    
#     def get_object(self, id):
#         try:
#             return Employee.objects.get(eid=id) 
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self, request, id, format = None):
#         employee = self.get_object(id)
#         serializer = employeeSerializer(employee)
#         return Response(serializer.data)
    
#     def put(self, request, id, format= None):
#         employee = self.get_object(id)
#         serializer = employeeSerializer(employee, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id, format=None):
#         employee = self.get_object(id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
















































# def show(request):
#     if request.method == 'GET':
        
#         employees = Employee.objects.all()
#         serializer = employeeSerializer(employees, many=True)
#         return JsonResponse(serializer.data, safe=False )
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = employeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializers.errors, status=400)
    # return render(request, 'show.html', {'employees':employees})
    
# @api_view(['GET', 'POST'])
# def show(request, format=None):
    
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = employeeSerializer(employees, many=True)
#         return Response(serializer.data)
    
#     elif request.method  == 'POST':
#         serializer = employeeSerializer(employees, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  




# def edit(request, id):
#     employee = Employee.objects.get(id=id)
#     return render(request, 'edit.html', {'employee':employee})

# def update(request, id):
#     employee = Employee.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance=employee)
#     if form.is_valid():
#         form.save()
#         return redirect('/show')
#     return render(request, 'edit.html', {'employee':employee})

# def destroy(request, id):
#     employee = Employee.objects.get(id = id)
#     employee.delete()
#     return redirect('/show')

# def details(request, id):
#     try:
#         employee = Employee.objects.get(id = id)
#     except employee.DoesNotExist:
#         return HttpResponse(status = 404)
#     if request.method == 'GET':
#         serializer = employeeSerializer(employee)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer =  employeeSerializer(employee, data=data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         employee.delete()
#         return HttpResponse(status = 204)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def details(request, id, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     # test = Employee.objects.all()
#     # for item in test:
#     #     item = item.eid
#     #     id = int(item)
#     try:
#         employee = Employee.objects.get(eid=id)
#         print(employee)
#     except employee.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = employeeSerializer(employee)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = employeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
        






