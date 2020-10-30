from rest_framework import serializers
from .models import Tutorial

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('title', 'description', 'image', 'content','Author','url','pub_date','updated_date','Published','Unpublished')
