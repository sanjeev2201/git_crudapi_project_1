from django.shortcuts import render, redirect
from .serializers import Student_Serializer
from .models import StudentModel
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response


# create a new project
@api_view(['POST'])
def Student_detail(request):
    student_serializer = Student_Serializer(data=request.data)
    if student_serializer.is_valid():
        student_serializer.save()
        return Response(student_serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Retrieve object
@api_view(['GET'])
def Student_List(request):
    # if request.method == 'GET':
    student_retrive = StudentModel.objects.all()
    student_serializer = Student_Serializer(student_retrive, many=True)
    return Response(student_serializer.data)


# update object
@api_view(['PUT'])
def Student_update(request, pk):
    student_retrive = StudentModel.objects.get(roll=pk)
    student_serializer = Student_Serializer(instance=student_retrive, data=request.data)
    if student_serializer.is_valid():
        student_serializer.save()
        return redirect('/retrieve/')
    return Response(student_serializer.data)
    # return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def Student_delete(request, pk):
    student_retrieve = StudentModel.objects.get(roll=pk)
    student_retrieve.delete()
    return Response("Delete is successfully")
