FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
RUN pip install kaggle 
RUN export KAGGLE_USERNAME=bubulibubulle && export KAGGLE_KEY=cf8b6f313e12641849239181d43adf47 && kaggle datasets download mrdew25/pokemon-database && unzip pokemon-database.zip && ls
COPY . /app
