# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the container's working directory
COPY Menu_api.py /app

# Expose port 80 for HTTP communication
EXPOSE 80

# Set the entrypoint command to run the Python script
CMD ["python", "Menu_api.py"]

#Flask Dependency
RUN pip install flask

# Set the entrypoint command to run the Python script
CMD ["python", "Menu_api.py"]