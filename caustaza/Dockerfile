# Use the official Python base image
FROM python:3.9



WORKDIR /app/
# Copy the Django project code to the working directory
COPY requirements.txt  requirements.txt


# Set the working directory in the container

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install translate
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install Pillow
COPY . . 

# Expose the port that the Django application will run on
EXPOSE 8000
# Run the Django development server
CMD python ./caustaza/manage.py migrate && python ./caustaza/manage.py runserver 0.0.0.0:8000

