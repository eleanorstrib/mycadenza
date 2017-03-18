from rest_framework import serializers
from signup.models import CadenzaUser

class CadenzaUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CadenzaUser
        fields = ('email', 'mobile', 'username', 'tracker_name', 'id',)
