# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first for caching
COPY fastAPI/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all FastAPI files
COPY fastAPI/ .

# Ensure the model is inside /app
COPY fastAPI/model/model.pkl model/model.pkl

# Expose port
EXPOSE 8000

# Run FastAPI app using uvicorn
CMD ["uvicorn", "iris_api:app", "--host", "0.0.0.0", "--port", "8000"]
