FROM python:3.13-alpine
WORKDIR /src
COPY . /src/
RUN pip install --no-cache-dir --upgrade --quiet pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
