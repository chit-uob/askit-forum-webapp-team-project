FROM python:3.11.2

# set environment variables
ENV PYTHONUNBUFFERED=1

# where your code lives
WORKDIR .
COPY .. .

# install dependencies
RUN pip install -r requirements.txt

# start server
CMD python manage.py runserver

# port where the Django app runs
EXPOSE 8000