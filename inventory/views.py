from django.shortcuts import render
from models import Question
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from inventory.serializers import UserSerializer, GroupSerializer


from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from inventory.models import Inventory
from inventory.serializers import InventorySerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def inventory_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Inventory.objects.all()
#         serializer = InventorySerializer(snippets, many=True)
#         return JSONResponse(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = InventorySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def inventory_detail(request, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Inventory.objects.get(pk=pk)
#     except Inventory.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = InventorySerializer(snippet)
#         return JSONResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = InventorySerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


class InventoryList(APIView):
    """
    List all inventory, or create a new snippet.
    """
    def get(self, request, format=None):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SaveLoginDetails(APIView):
    """"""
    def save_login_details(self):
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)
        print "asdfgsadf"
        import ipdb;ipdb.set_trace()
        print "im in function fuck you !!!!!!!!!!"