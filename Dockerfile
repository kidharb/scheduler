FROM python:alpine3.20
COPY . /scheduler
WORKDIR /scheduler
RUN pip install -r requirements.txt
CMD ["python", "./scheduler.py"]
