from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    def validate_mobile(self, value):
        if User.objects.filter(mobile=value).exists():
            raise serializers.ValidationError('این شماره قبلا ثبت شده است')
        return value

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': False,
            },
            'email': {
                'required': False,
            },
            'password': {
                'required': False,
            },
            'gender': {
                'required': False,
            },
            'full_name': {
                'required': False,
            },
            'expire_at': {
                'required': False,
            },
            'status': {
                'required': False,
            },
            'verify_code': {
                'required': False,
            },
            'cart_number': {
                'required': False,
            },
            'shaba': {
                'required': False,
            },
            'is_admin': {
                'required': False,
            },
            'last_send_sms_at': {
                'required': False,
            },
            'gallery_id': {
                'required': False,
            },
            'profile_photo_path': {
                'required': False,
            },
            'created_at': {
                'required': False,
            },
            'updated_at': {
                'required': False,
            },
        }
