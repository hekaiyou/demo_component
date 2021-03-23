FROM python:3.8.7
WORKDIR /app
ADD . /app
ARG TZ=Asia/Shanghai
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--log-file", "-", "--access-logfile", "-", "--error-logfile", "-"]
EXPOSE 8000
