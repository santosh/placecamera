# Use an existing docker image as a base
FROM python:3.7-alpine

# Download and install a dependency
## Don't litter /
WORKDIR /app

## Only copy requirements.txt
COPY ./requirements.txt ./
## So that cache till the installation is preserved
RUN pip install -r requirements.txt
## And the changes we make any project file only copies those files,
## not the dependencies
COPY ./ ./

# This is for inter-container communication
# EXPOSE 8001

# Tell the image what to do when it starts as a container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

