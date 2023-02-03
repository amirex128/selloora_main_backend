from rest_framework import serializers


class UserRegisterLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)


class UserVerifyCodeSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    verify_code = serializers.CharField(required=True)


class UserPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)


class UserForgetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
