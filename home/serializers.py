from rest_framework import serializers
from .models import Person,Color



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color 
        fields  = ['color_name']



class PeopleSerializer(serializers.ModelSerializer):
    color = colorSerializer()
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        #exclude = ['name']
        fields = '__all__'
        depth = 1  

    def get_color_info(self,obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name':color_obj.color_name,'hex_code':'#000'}
        

    # def validate_age(self,data):
    #     print(data)
    #     return data
    def validate(self, data):

        special_characters = "!@#$%^&*()-+_=?,<>/"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('name cannot contain special characters')
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        return data
        


