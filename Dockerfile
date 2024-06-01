# Use the official Python image from the Docker Hub
FROM python:3.8.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    netcat

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the working directory
COPY . /app/

# Copy certificates
COPY certs/root.crt /app/.postgresql/root.crt

# Run Django migrations and start the development server
# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Run gunicorn
# CMD ["gunicorn", "houston.wsgi:application", "--bind", "0.0.0.0", "--log-file", "-"]
CMD python manage.py migrate && gunicorn houston.wsgi --bind 0.0.0.0:$PORT

# Make port 8000 available to the world outside this container
EXPOSE 8000
