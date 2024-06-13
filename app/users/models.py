from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models

class UserManager(BaseUserManager):
    # 일반 유저 생성 함수
    def create_user(self, email, password):
        if not email:
            raise ValueError("이메일 주소를 입력하세요")

        user = self.model(email=email)
        # AbstractBaseUser의 set_password 사용
        user.set_password(raw_password=password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    email = models.CharField(max_length=255, unique=True) # 일단 최대로 잡아놓고 나중에 변경하면 된다!
    # password field는 이미 AbstractBaseUser에 구현되어 있으므로 선언할 필요X
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)

    # Permissions Mixin : 사용자 권한 관리 클래스
    is_active = models.BooleanField(default=True) # 사용자가 회원가입했다 -> active user로 설정
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # AbstartcBaseUser 클래스의 username 필드에 email로 받을것이라고 설정

    objects = UserManager() # 위에 있는 메서드 쓰기 위해 objects 변수 선언

    def __str__(self):
        return f"email : {self.email}, nickname : {self.nickname}"
