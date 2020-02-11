FROM tiangolo/uwsgi-nginx-flask:python3.7
# RUN apk --update add bash nano
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static
COPY . /app
RUN pip install -r /app/requirements.txt