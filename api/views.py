from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# from rest_framework.response import JSONResponse
from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

# Function Bsed

# @csrf_exempt
# def emp_api(request):
#     if request.method=='GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             emp=Employee.objects.get(id=id)
#             serializer=EmployeeSerializer(emp)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         emp=Employee.objects.all()
#         serializer=EmployeeSerializer(emp,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
        
    
    # if request.method=='POST':
    #     json_data=request.body
    #     stream=io.BytesIO(json_data)
    #     pythondata=JSONParser().parse(stream)
    #     serializer=EmployeeSerializer(data=pythondata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res={'msg':'Done'}
    #         json_data=JSONRenderer().render(res)
    #         return HttpResponse(json_data,content_type='application/json')
    #     json_data=JSONRenderer().render(serializer.error)
    #     return HttpResponse(json_data,content_type='application/json')
    
    # if request.method == 'PUT':
    #     json_data=request.body
    #     stream=io.BytesIO(json_data)
    #     pythondata=JSONParser().parse(stream)
    #     id=pythondata.get('id')
    #     emp=Employee.objects.get(id=id)
    #     serializer=EmployeeSerializer(emp,data=pythondata,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res={'msg': 'Updated'}
    #         json_data=JSONRenderer().render(res)
    #         return HttpResponse(json_data,content_type='application/json')
    #     json_data=JSONRenderer().render(serializer.error)
    #     return HttpResponse(json_data,content_type='application/json')
    
    # if request.method == 'DELETE':
    #     json_data=request.body
    #     stream=io.BytesIO(json_data)
    #     pythondata=JSONParser().parse(stream)
    #     id=pythondata.get('id')
    #     emp=Employee.objects.get(id=id)
    #     emp.delete()
    #     res={'msg': 'Delete Success!'}
    #     json_data=JSONRenderer().render(res)
    #     return HttpResponse(json_data,content_type='application/json')
    #     # return JSONResponse(res,safe=False)
    # json_data=JSONRenderer().render(serializer.error)
    # return HttpResponse(json_data,content_type='application/json')
    

    #Class Based
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeAPI(View):
    def get(self,request, *args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request, *args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Done'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg': 'Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        emp=Employee.objects.get(id=id)
        emp.delete()
        res={'msg': 'Delete Success!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        # return JSONResponse(res,safe=False)
 



