# ====  Step 1: Run Python script and generate HTML   ====
FROM python:3.12.2-slim-bookworm

# Add non-root user so the container doesn't run as a root user.
RUN groupadd -r nonroot \
    && useradd -r -g nonroot nonroot
USER nonroot

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the rest of the application code into the container
COPY ./kata1_dictionary.py .

# Run the Python script and save its output as HTML
RUN python script.py > index.html

# ========  Step 2: Serve with Nginx   ========
FROM nginx:alpine

# Copy generated HTML from builder stage into Nginx's web root
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Run Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
