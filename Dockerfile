FROM python:3.10

WORKDIR /app

COPY flask_project/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY flask_project/ .
EXPOSE 5000
CMD ["python", "app.py"]
