from django.shortcuts import render

# Create your views here.
from .models import Category, Product, Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER


class OrderView(APIView):
    def post(self, request):
        try:
            serializer = OrderSerializer(data=request.data)

            subject = "New Order is Placed" 
            message = "Dear Customer" + " " + request.data['customer_name'] + " Your order is placed now. Thanks for your order"
            email = request.data['customer_email']
            recipient_list = [email]
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=False)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message":"Something went Wrong on creating order"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message":"Somethin went Wrong on getting orders"}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):
        try:
            order = Order.objects.get(id=request.data['id'])
            serializer = OrderSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"message": "Something went wrong on updating order"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            order = Order.objects.get(id=request.data['id'])
            order.delete()
            return Response({"message": "Order deleted successfully"}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"message": "Something went wrong on deleting order"}, status=status.HTTP_400_BAD_REQUEST)
        