


from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from apps.user.models import Users,UserDetail,Verification


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
		]

class UsersDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserDetail
		fields='__all__'

		validators = [
			UniqueTogetherValidator(
				queryset=UserDetail.objects.all(),
				fields=('userid',),
				message="请勿重复填写资料！",
			),
		]

class VerificationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Verification
		fields='__all__'


