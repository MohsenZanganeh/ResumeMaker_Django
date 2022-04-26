from djoser import serializers

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name','user_type']

class UserSerializer(serializers.UserSerializer):
    class Meta(serializers.UserSerializer.Meta):
        fields = ['id','username','password','email','first_name','last_name','user_type']

