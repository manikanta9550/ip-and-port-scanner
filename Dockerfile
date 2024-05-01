# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY portscan.py /app/

# Install dependencies (if any)
# RUN pip install ...

# Set the entry point for the container
ENTRYPOINT ["python", "portscan.py"]
