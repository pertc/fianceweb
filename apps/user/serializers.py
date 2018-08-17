


from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from apps.user.models import Users


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model=Users
		fields='__all__'

		validators = [
			UniqueTogetherValidator(
				queryset=Users.objects.all(),
				fields=('mobile',),
				message="手机号重复！"
			),
			UniqueTogetherValidator(
				queryset=Users.objects.all(),
				fields=('username',),
				message="用户名重复！"
			),
		]

