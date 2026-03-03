# Use a specific Python version as the base image
FROM python:3.12-slim-bookworm AS builder

# Set the working directory
WORKDIR /app

# Install uv for dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the lockfile and pyproject.toml
COPY pyproject.toml uv.lock ./

# Install dependencies into a virtual environment
RUN uv sync --frozen --no-dev

# Final stage
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv /app/.venv

# Add the virtual environment to the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables for the application
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "Application/app.py"]
