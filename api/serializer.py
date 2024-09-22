from rest_framework import serializers
from .models import tbl_login


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tbl_login
        fields = '__all__'

