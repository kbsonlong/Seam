FROM python:3.7
ADD ./ /data/Seam
WORKDIR /data/Seam
RUN pip install -r requirements && pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000