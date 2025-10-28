FROM python:3.10-slim

WORKDIR /app

# Copy requirements dan install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh aplikasi
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
