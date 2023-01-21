from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

 

# class employeeSerializer(serializers.Serializer):
    
#     eid = serializers.IntegerField()
#     ename = serializers.CharField(max_length = 100)
#     eemail = serializers.EmailField(max_length = 100)
#     econtact = serializers.IntegerField()
    
    
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.eid = validated_data.get('eid', instance.eid)
#         instance.ename = validated_data.get('ename', instance.ename)
#         instance.eemail = validated_data.get('eemail', instance.eemail)
#         instance.econtact = validated_data.get('econtact', instance.econtact)
#         instance.save()
#         return instance



class employeeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Employee
        fields = ['eid', 'ename', 'eemail', 'econtact', 'owner']
        


class UserSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'employees']    
        

        
        
    