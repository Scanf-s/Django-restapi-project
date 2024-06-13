# Django DB 연결 실패 시, 재시도 하는 로직 추가
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
import time

# Operation Error & Psycopg2 Operation Error
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OPsycopgpError

class Command(BaseCommand):
    def handle(self, *args, **options):
        # 콘솔에 다음 문장을 출력해준다.
        self.stdout.write('Wating for DB connection ...')

        is_db_connected = None
        # 연결이 완료될 때 까지 계속 loop
        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except (OperationalError, Psycopg2OPsycopgpError):
                self.stdout.write("Retrying DB connection ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("PostgreSQL Connection Success."))


