from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
# TDD : Test Driven Development (테스트 주도 개발 방법)

class UserTestCase(TestCase):

    # 일반 유저 생성 방식
    def test_create_user(self):
        email = 'test@test.com'
        password = '123123'

        # get_user_model()을 통해서 User.objects.create()쓰는것처럼 생각하면 된다.
        new_user = get_user_model().objects.create_user(email=email, password=password)

        # 유저가 정상적으로 생성되었는지 여부를 테스트
        self.assertEqual(new_user.email, email)
        # User model이 AbstractBaseUser를 상속받는데, 그 안에 check_password라는 함수가 구현되어 있다.
        self.assertTrue(new_user.check_password(password))
        self.assertEqual(new_user.is_superuser, False) # False 이어야함
        self.assertFalse(new_user.is_superuser) # 위에 코드랑 같은 동작

        # 테스트 실행하기 전에, migration 안했으면 migration부터 해야함
        # docker-compose run --rm app sh -c 'python manage.py test users'
        # makemigrations할 때, email을 USERNAME_FIELD로 설정했음에도 불구하고, Unique 제약조건을
        # 설정하지 않아서 에러가 발생했었다. unique=True를 설정해주자.

        # makemigrations를 수행한 후에 migrations 폴더의 migration 파일을 항상 열어서 확인하는 습관을 가지자.
        # 원래 username 필드가 있어야하는데, email로 바뀌었음을 확인할 수 있다.

        # migrate 오류 :
        # django.db.migrations.exceptions.InconsistentMigrationHistory:
        # Migration admin.0001_initial is applied before its dependency users.0001_initial
        # on database 'default'.
        # 즉, 도커를 사용해서 구성한 migrate 명령을 통해 기존에 설정된 User 클래스와
        # 내가 만든 커스텀 유저 모델과 충돌이 났다는 의미라고 생각하자.
        # 해결 방법 : https://legend-palm-1f1.notion.site/85-2-c4aa83349e8e4f4eae3e8b2e9c06dc29
        # 다 해결했으면, 주석 해제하고 migrate 한번 해주면 된다.
        # docker-compose run --rm app sh -c 'python manage.py test users'

    # 수퍼 유저 생성 방식
    # python manage.py createsuperuser 방식 말고, 코드로 생성하는 방식
    def test_create_superuser(self):
        email = 'super@super.com'
        password = '123123'

        new_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        # Syperuser 제대로 만들었는지 확인
        self.assertTrue(new_user.is_superuser)
        self.assertTrue(new_user.is_staff)
