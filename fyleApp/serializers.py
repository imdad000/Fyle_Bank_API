from rest_framework import serializers
from .models import Banks,Branches


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city','district','state')


class BanksSerializer(serializers.ModelSerializer):
	class Meta:
		model=Banks
		fields=('name','id')
