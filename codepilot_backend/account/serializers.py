from rest_framework import serializers

from account.models import User,StudentProfile

class AdminSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","password","email","phone","role"]

        read_only_fields =["id","role"]


    def create(self, validated_data):

        return User.objects.create_superuser(**validated_data)      


class StudentSerilaizer(serializers.ModelSerializer):


    class Meta:
   

        model = User

        fields = ["id","username","password","email","phone","role"]
        
        read_only_fields =["id","role"]
        

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)



class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudentProfile

        fields = "__all__"

        read_only_fields = ["created_at","updated_at"]

   
    

