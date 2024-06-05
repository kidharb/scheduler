FROM python:alpine3.20
RUN mkdir -p /scheduler
COPY scheduler.py requirements.txt /scheduler
WORKDIR /scheduler
RUN pip install -r requirements.txt
CMD ["python", "./scheduler.py"]
