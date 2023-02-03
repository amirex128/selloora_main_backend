from datetime import datetime, timedelta
from random import randint

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from user.models import User
from user.serializers import UserRegisterLoginSerializer, UserVerifyCodeSerializer, UserPasswordSerializer
from utils.sms import sendSMS
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password


class UserRegisterLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserRegisterLoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=serializer.data['username']).all()
        if user.count() == 0:
            user = User(username=serializer.data['username']).save()
            code = randint(1000, 9999)
            user.verify_code = code
            sendSMS(serializer.data['username'], f"کد تائید سلورا {code}")
            user.save()
            return Response({
                "message": "کد تایید به شماره همراه شما ارسال گردید",
                "has_password": False,
                "verify_code": True,
            }, status=status.HTTP_200_OK)
        user = user[0]
        if user.password:
            return Response({
                "message": "لطفا گذرواژه خود را برای ورود وارد نمایید",
                "has_password": True,
                "verify_code": False,
            }, status=status.HTTP_200_OK)
        ten_min_ago = datetime.now() - timedelta(minutes=10)
        last_send_smm_at = datetime.strptime(user.last_send_sms_at, '%Y-%m-%d %H:%M:%S')
        if last_send_smm_at < ten_min_ago:
            code = randint(1000, 9999)
        else:
            code = user.verify_code
        user.verify_code = code
        try:
            sendSMS(serializer.data['username'], f"کد تائید سلورا {code}")
        except Exception as e:
            return Response({
                "message": "خطا در ارسال پیامک",
            }, status=status.HTTP_400_BAD_REQUEST)
        user.save()
        return Response({
            "message": "کد تایید به شماره همراه شما ارسال گردید",
            "has_password": False,
            "verify_code": True,
        }, status=status.HTTP_200_OK)


class UserVerifyCodeAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserVerifyCodeSerializer(data=data)
        if serializer.is_valid():
            valid_user = User.objects.filter(username=serializer.data['username'],
                                             verify_code=serializer.data['verify_code']).all()
            if valid_user.count() == 0:
                return Response({
                    "message": "کد تایید اشتباه است",
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "message": "شما با موفقیت وارد شدید",
                    **get_tokens_for_user(valid_user[0])
                }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserPasswordSerializer(data=data)
        if serializer.is_valid():
            valid_user = User.objects.filter(username=serializer.data['username']).all()
            if valid_user.count() == 0:
                return Response({
                    "message": "شما ثبت نام نکرده اید",
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                if check_password(serializer.data['password'], valid_user[0].password):
                    return Response({
                        "message": "شما با موفقیت وارد شدید",
                        **get_tokens_for_user(valid_user[0])
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "message": "کلمه عبور اشتباه میباشد",
                    }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
