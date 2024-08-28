## Redis Environment Setup using Docker
This guide will walk you through setting up a Redis environment on your local system using Docker. Whether you're a beginner or an experienced user, this guide will provide clear instructions to get Redis up and running quickly.

## Prerequisites
Before you start, ensure you have the following installed on your local machine:

Docker: Docker allows you to run containers on your machine. You can install Docker from the official website.
Basic Command Line Knowledge: Familiarity with terminal or command prompt is helpful.

## Step 1: Verify Docker Installation
First, verify that Docker is installed and running on your machine.

Open a terminal (or command prompt on Windows) and run the following command:

```bash
docker --version
```

You should see the Docker version installed on your machine. If not, make sure Docker is installed correctly.

## Step 2: Pull the Redis Docker Image
Docker images are pre-built templates that you can use to run containers. Redis provides an official Docker image that we can use.

To pull the Redis image, run the following command:

```bash
docker pull redis
```
This command downloads the Redis image from Docker Hub to your local machine. You should see the download progress, and once completed, the image will be ready for use.

## Clone the Course Git Repository

```bash
git clone https://github.com/redislabs-training/ru402.git
```
Now, change to the directory containing the course files:

```bash
cd ru402
```

## Step 3: Run Redis in a Docker Container
Now that the Redis image is downloaded, you can create and run a Redis container.
Run the following command to start a Redis container:

```bash
docker run --name my-redis-container -d redis
```
```bash
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 -e REDIS_ARGS="--requirepass mypassword" redis/redis-stack:latest
```

## Explanation:
```bash
--name redis-stack: This names your container "redis-stack". You can choose any name you like.
```
```bash
-d: This runs the container in detached mode, meaning it runs in the background.
```
```bash
redis-stack: This specifies the image to use, which is the official Redis image you pulled earlier.
```
```bash
After running this command, Redis should be up and running in the container.
```

# Step 4: Check that the container is running like this command:

```bash
docker ps
```
```bash
CONTAINER ID   IMAGE                        COMMAND            CREATED        STATUS       PORTS                                            NAMES
3309f829b90a   redis/redis-stack:7.2.0-v0   "/entrypoint.sh"   2 months ago   Up 7 weeks   0.0.0.0:6379->6379/tcp, 0.0.0.0:8001->8001/tcp   redis-stack
```

## Step 5: Use the Web Interface
If you used the Docker or local install of Redis Stack options to get your Redis instance, you can choose to use RedisInsight as a web application with no further software to install.

First, ensure that the Docker container or your local Redis Stack installation is running.
Now, point your browser at http://localhost:8001/ and you should see the RedisInsight terms and conditions:

<img width="1015" alt="Screenshot 2024-08-28 at 9 49 34 AM" src="https://github.com/user-attachments/assets/ca824cfa-b483-4d8f-940f-2ed34b742155">

Accept the terms and click "Submit". RedisInsight will automatically connect to the local Redis Stack instance and display the key browser:

<img width="945" alt="Screenshot 2024-08-28 at 9 50 59 AM" src="https://github.com/user-attachments/assets/16899471-742c-49ea-aaf3-93b1523dcca8">

