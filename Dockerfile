FROM python

WORKDIR /app/

# Copy the current directory contents into the container at /app
COPY app.py requirements.txt /app/

# Install any needed packages as specified in requirements.txt
# Ensure you have a requirements.txt with any necessary dependencies listed
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]
