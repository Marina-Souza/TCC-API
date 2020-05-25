FROM python:3.6

WORKDIR /usr/src/app

COPY ./api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD python ./api/manage.py makemigrations && python ./api/manage.py runserver 0.0.0.0:8000