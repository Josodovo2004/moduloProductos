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

# Expose the port the app runs on
EXPOSE 8000

# Apply database migrations
RUN python manage.py migrate

# Load the CSV data using the management command
RUN python manage.py load_products  # <-- This runs the command to load the CSV data

# Command to run the Django app with HTTPS
CMD ["gunicorn", "--bind", "0.0.0.0:8000",  "ModuloProductos.wsgi:application"]
