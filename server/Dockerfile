# Use an appropriate base image with Python installed
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /server

# Copy the server code into the container
COPY . /server

# Install any dependencies required for the server
RUN pip install flask

# Command to run the server
CMD ["python", "server.py"]
