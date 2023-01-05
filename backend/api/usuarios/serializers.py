from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True,
        required=True,
    )
    password = serializers.CharField(
        label="Password",
        style={
            "input_type": "password"
        },  # Isso será usado quando a API navegável DRF estiver habilitada
        trim_whitespace=False,
        write_only=True,
        required=True,
    )

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get("request"),
            username=attrs.get("username"),
            password=attrs.get("password"),
        )
        if not user:
            msg = "Acesso Negado: usuário ou senha inválidos."
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True,
        required=True,
    )
    password = serializers.RegexField(
        label="Password",
        style={
            "input_type": "password"
        },  # Isso será usado quando a API navegável DRF estiver habilitada
        trim_whitespace=False,
        write_only=True,
        required=True,
        regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
    )
    email = serializers.EmailField(
        label="E-mail",
        write_only=True,
        required=True,
    )
    first_name = serializers.CharField(
        label="Primeiro Nome",
        write_only=True,
        required=True,
    )
    last_name = serializers.CharField(
        label="Último Nome",
        write_only=True,
        required=True,
    )

    def validate(self, attrs):
        User.objects.create_user(
            username=attrs.get("username"),
            password=attrs.get("password"),
            email=attrs.get("email"),
            first_name=attrs.get("first_name"),
            last_name=attrs.get("last_name"),
        )
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
        ]
