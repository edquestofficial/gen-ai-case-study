# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container
COPY . /app

# Step 4: Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Step 5: Expose the port FastAPI will run on
EXPOSE 8000

# Step 6: Command to run the FastAPI app using uvicorn
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
