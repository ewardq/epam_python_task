FROM python:3.12.2-slim-bookworm

# Add non-root user so the container doesn't run as a root user.
RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot

USER nonroot

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the rest of the application code into the container
COPY ./kata1_dictionary.py .
COPY ./__init__.py .

CMD ["python", "./kata1_dictionary.py"]
