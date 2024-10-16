# Use official Python image as a base
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Copy the SSL certificates into the container
COPY /ssl_certificates/cert.pem /app/cert.pem
COPY /ssl_certificates/key.pem /app/key.pem

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django app with HTTPS
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--certfile=/app/cert.pem", "--keyfile=/app/key.pem", "ModuloProductos.wsgi:application"]
