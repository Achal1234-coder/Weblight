from django.shortcuts import render
from .models import Payment
from razorpay import Client
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from trust.settings import RAZORPAY_KEY_ID, RAZORPAY_SECRET
from rest_framework import status



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment(request):
    if(request.method == 'POST'):
        try:

            try:
                phone_number = request.POST['phone_number']
                amount = request.POST['amount']
            except Exception as e:
                context = {'message': 'phone number or amount not provided', 'status': 'Error'}
                return Response(context, status=status.HTTP_400_BAD_REQUEST)

            if not amount or float(amount) < 1 :
                context = {'message': 'At least 1 rupee required to donate', 'status': 'Information'}
                return Response(context, status=status.HTTP_200_OK)

            profile = Profile.objects.get(phone_number=phone_number)

            if(profile.is_login):
                amount = float(amount)*100
                client = Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET))

                response_payment = client.order.create(dict(amount=amount, currency='INR'))
                if(response_payment['status'] == 'created'):
                    Payment.objects.create(profile=profile, amount=amount / 100, razorpay_payment_id = response_payment['id'], paid=True)
                else:
                    Payment.objects.create(profile=profile, amount=amount / 100, razorpay_payment_id = response_payment['id'])

                context = {'messgae': 'Payment is done', 'status': 'Success'}
                return Response(context, status=status.HTTP_201_CREATED)

            else:
                context = {'messgae': 'User not authorize', 'status': 'Error'}
                return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(e)
            context = {'message':'Something went wrong while processing your request', 'status': 'Error'}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payement_history(request):
    try:
        try:
            phone_number = request.data['phone_number']
        except Exception as e:
            context = {'message': 'Phone number not provided', 'status': 'Error'}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.get(phone_number=phone_number)

        if(profile.is_login):
            user_payment_history = Payment.objects.filter(profile=profile, paid=True).values()
            return Response(user_payment_history, status=status.HTTP_200_OK)

        else:
            context = {'messgae': 'User not authorize', 'status': 'Error'}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        print(e)
        context = {'message':'Something went wrong while processing your request', 'status': 'Error'}
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def data_visualization(request):
    try:
        try:
            phone_number = request.data['phone_number']
        except Exception as e:
            context = {'message': 'Phone number not provided', 'status': 'Error'}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        profile = Profile.objects.get(phone_number=phone_number)

        if(profile.is_login):
            yearly_monthly_data = {}

            month = {1:'Jan', 2: 'Feb', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

            user_payment_history = list(Payment.objects.filter(profile=profile, paid=True).values())

            for payment in user_payment_history:
                if(payment['date'].year not in yearly_monthly_data):
                    yearly_monthly_data[payment['date'].year] = []

                is_month_present_in_dict = False
                for item in yearly_monthly_data[payment['date'].year]:
                    if(item['month'] == month[payment['date'].month]):
                        is_month_present_in_dict = True
                        item['total_donation_in_month'] += float(payment['amount'])
                        break

                if(not is_month_present_in_dict):
                    yearly_monthly_data[payment['date'].year].append({'month': month[payment['date'].month], 'total_donation_in_month': float(payment['amount'])})

            return Response(yearly_monthly_data, status=status.HTTP_200_OK)

        else:
            context = {'messgae': 'User not authorize', 'status': 'Error'}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        context = {'message':'Something went wrong while processing your request', 'status': 'Error'}
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
