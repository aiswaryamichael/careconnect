from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

    # TO ENCRYPT THE PASSWORD

    def create(self,validated_data):

        u=User.objects.create_user(**validated_data)

        u.save()
        return u