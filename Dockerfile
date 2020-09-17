# Use an existing docker image as a base
FROM python:3.7-alpine AS builder

# Download and install a dependency
## Don't litter /
WORKDIR /app

## Only copy requirements.txt
## So that cache till the installation is preserved
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

FROM python:3.8-alpine

COPY --from=builder /root/.local/bin /root/.local

COPY ./ ./

# This is for inter-container communication
# EXPOSE 8001

# Tell the image what to do when it starts as a container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
