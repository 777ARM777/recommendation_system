FROM python:3.9-slim
WORKDIR /app
COPY invoker.py .
RUN pip install flask cachetools redis requests
CMD ["python", "invoker.py"]