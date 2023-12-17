# Use the official Python image as the base image
FROM python:3.10

# Create and set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
