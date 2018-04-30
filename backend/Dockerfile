FROM tiangolo/uwsgi-nginx-flask:python3.6
# create web folder
RUN mkdir -p /var/www
# add app
COPY ./app /var/www/app
WORKDIR /var/www/app
# install requirements
RUN pip install -r requirements.txt