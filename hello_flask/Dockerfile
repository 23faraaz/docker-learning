# ==============================
# Stage 1: Build Stage
# ==============================
# This stage installs all build-time dependencies
# These are required to compile Python packages like mysqlclient
# This stage will NOT be part of the final deployed image

FROM python:3.8-slim AS build

# Set working directory inside the container
WORKDIR /app

# Install system-level build dependencies
# These are needed only during build time
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files from host into the container
# First dot = current directory on host
# Second dot = /app directory inside container (because of WORKDIR)
COPY . .

# Install Python dependencies
# mysqlclient requires the build tools installed above
RUN pip install --no-cache-dir flask mysqlclient


# ==============================
# Stage 2: Production Stage
# ==============================
# This stage creates the final lightweight image
# Only runtime dependencies are included here

FROM python:3.8-slim

# Set working directory for the running application
WORKDIR /app

# Copy the built application and installed Python packages
# from the build stage into this clean image
COPY --from=build /app /app

# Document the port the Flask app listens on
EXPOSE 5002

# Command to run the Flask application
CMD ["python", "app.py"]
