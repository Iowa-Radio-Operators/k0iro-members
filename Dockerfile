# Use an official Python image as a base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1

# Run migrations and collect static files (optional, based on your needs)
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Define the command to run the app
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8150", "core.wsgi"]