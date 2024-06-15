# Python 3.12와 Alpine Linux 3.20을 기반으로 하는 이미지 사용
FROM python:3.12-alpine3.20

# 이미지의 유지 관리자를 지정
LABEL maintainer="sullungim"

# Python의 표준 입출력 버퍼링을 비활성화하여 로그가 즉시 출력되도록 설정
ENV PYTHONUNBUFFERED=1

# 로컬 파일 시스템의 requirements.txt와 requirements.dev.txt 파일을 컨테이너로 복사
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
COPY ./scripts /scripts

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

# curl 설치를 위한 추가
RUN apk add --no-cache curl

# 컨테이너가 8000번 포트를 노출하도록 설정
EXPOSE 8000

# DEV 인수를 false로 설정 (기본값)
ARG DEV=false

# 패키지 설치 및 이미지 최적화
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# 경로 설정
ENV PATH="/scripts:/py/bin:$PATH"

# django-user로 실행
USER django-user

# 컨테이너가 실행될 때 run.sh 스크립트를 실행하도록 설정
CMD ["run.sh"]

