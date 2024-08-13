FROM python:3.9-slim
WORKDIR /app
COPY generator.py .
RUN pip install flask
CMD ["python", "generator.py"]