# Use the official Python image as the base image
FROM python:3.11

# Set an environment variable to avoid buffering Python output to console
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements /app/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements

# Copy the whole Django project into the container
COPY . /app/

# Expose the port that the Django development server will be running on (default: 8000)
EXPOSE 8000
EXPOSE 5432

# Run the Django development server when the container starts
CMD ["python", "accu/manage.py", "runserver", "0.0.0.0:8000"]
