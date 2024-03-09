from django.contrib.auth.models import User
from .models import Profile
import random
from .helper import MessageHandler
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



@api_view(['POST'])
def login(request):
        if request.method == "POST":
                try:
                        try:
                                phone_number = request.POST['phone_number']
                        except Exception as e:
                                context = {'message': 'Phone number not provided', 'status': 'Error'}
                                return Response(context, status=status.HTTP_400_BAD_REQUEST)

                        if(Profile.objects.filter(phone_number = phone_number).exists()):
                                profile = Profile.objects.filter(phone_number = phone_number)[0]
                                otp=random.randint(1000,9999)
                                profile.otp = otp
                                profile.save()
                                try:
                                        messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
                                        user = User.objects.get(username=profile.user)
                                        refresh = RefreshToken.for_user(user)
                                        context = {'messgae':'OTP send successfully on your phone no', 'status': 'Success'}
                                        return Response(context, status=status.HTTP_200_OK)
                                except Exception as e:
                                        context = {'message': 'Please make sure your phone number is registered on Twilio to get messages on phone', 'status': 'Information'}
                                        return Response(context, status=status.HTTP_200_OK)

                        else:
                                context = {'message': 'User does not exist', 'status':'Error'}
                                return Response(context, status=status.HTTP_404_NOT_FOUND)

                except Exception as e:
                        context = {'message':'Something went wrong while processing your request', 'status': 'Error'}
                        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
def register(request):
        if request.method=="POST":
                try:
                        try:
                                phone_number = request.POST['phone_number']
                                username = request.POST['user_name']
                        except Exception as e:
                                context = {'message': 'Phone number or username not provided', 'status': 'Error'}
                                return Response(context, status=status.HTTP_400_BAD_REQUEST)

                        if (Profile.objects.filter(phone_number = phone_number).exists()):
                                context = {'message': 'User already exists', 'status': 'Error'}
                                return Response(context, status=status.HTTP_409_CONFLICT)

                        user=User.objects.create(username=request.POST['user_name'])
                        profile=Profile.objects.create(user=user,phone_number=phone_number)
                        context = {'message': 'User Successfully Registered', 'status': 'Success'}
                        return Response(context, status=status.HTTP_201_CREATED)

                except Exception as e:
                        context = {'message': 'Something went wrong while processing your request', 'status': 'Error'}
                        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def otpVerify(request):
        if request.method=="POST":
                try:
                        try:
                                phone_number = request.POST['phone_number']
                                otp_value = request.POST['otp']
                        except Exception as e:
                                context = {'message': 'Phone number or otp not provided', 'status': 'Error'}
                                return Response(context, status=status.HTTP_400_BAD_REQUEST)

                        profile=Profile.objects.get(phone_number=phone_number)
                        if(profile.otp==otp_value):
                                profile.is_login = True
                                profile.save()
                                user = User.objects.get(username=profile.user)
                                refresh = RefreshToken.for_user(user)
                                context = {'message': 'User Successfully Log In', 'status': 'Success', 'token': str(refresh.access_token)}
                                return Response(context, status=status.HTTP_200_OK)
                        context = {'message': 'Wrong OTP', 'status': 'Error'}
                        return Response(context, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                        context = {'message': 'Something went wrong while processing your request', 'status': 'Error'}
                        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def logout(request):
        try:
                try:
                        phone_number = request.data['phone_number']
                except Exception as e:
                        context = {'message': 'Phone number not provided', 'status': 'Error'}
                        return Response(context, status=status.HTTP_400_BAD_REQUEST)
                profile = Profile.objects.get(phone_number=phone_number)
                profile.is_login = False
                profile.save()

                context = {'message': 'User Successfully Log out', 'status': 'Success'}
                return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
                context = {'message': 'Something went wrong while processing your request', 'status': 'Error'}
                return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
