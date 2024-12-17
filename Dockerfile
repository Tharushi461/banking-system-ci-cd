# Use the official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy files
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
