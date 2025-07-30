# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose backend port
EXPOSE 5000

# Set environment variable (optional default Mongo URI)
ENV MONGO_URI=mongodb://mongodb:27017/

# Start the app
CMD ["python", "app.py"]
