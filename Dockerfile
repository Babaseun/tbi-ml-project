# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install pipenv and dependencies for pipenv to run
RUN pip install --no-cache-dir pipenv

# Copy only Pipfile and Pipfile.lock first (to leverage Docker cache)
COPY Pipfile Pipfile.lock ./

# Install dependencies in a production environment, without dev packages
RUN pipenv install --system --deploy --ignore-pipfile

# Copy your app source code excluding tests
COPY server.py ./
COPY your_flask_module ./your_flask_module

# Expose port (adjust if your app uses a different port)
EXPOSE 5000

# Run the Flask app
CMD ["python", "server.py"]
