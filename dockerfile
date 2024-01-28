FROM python:3.9.18-bullseye

WORKDIR /smartnotes

COPY . /smartnotes

RUN pip3 install -r ./requirement.txt

CMD ["python3", "manage.py", "runserver", "smartnotes:8000"]