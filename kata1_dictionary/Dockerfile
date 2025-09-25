# ====  Step 1: Run Python script and generate HTML   ====
FROM python:3.12-slim-bookworm AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY ./kata1_dictionary.py .

# Run the Python script, write it to console and save its output as HTML
RUN python ./kata1_dictionary.py | tee index.html

# ========  Step 2: Serve with Nginx   ========
FROM nginx:1.27-alpine

# Copy generated HTML from builder stage into Nginx's web root
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html

# Add non-root user so the container doesn't run as a root user. 
RUN groupadd -r nonroot \ 
    && useradd -r -g nonroot nonroot

# Expose port 80
EXPOSE 80

# Run Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
