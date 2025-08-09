# Your Project Name

This project is containerized using Docker to ensure consistent and reproducible environments across different machines.
link for docker image to pull : docker pull prem11121992/iris_api:latest 

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Working with Data](#working-with-data)
- [Running Scripts](#running-scripts)
- [Stopping and Removing Containers](#stopping-and-removing-containers)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The project [briefly explain the purpose — e.g., trains a machine learning model, processes data, runs an app] using Docker to simplify setup and execution.

---

## Prerequisites

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop) on your system.
- Basic familiarity with Docker commands.

---

## Building the Docker Image

From the root directory of the project, build the Docker image with:

```bash
docker build -t your-project-name .
```

This creates a Docker image tagged as `your-project-name`.

---

## Running the Docker Container

Run the container interactively with:

```bash
docker run -it your-project-name
```

To run a specific Python script (e.g., training the model):

```bash
docker run your-project-name python src/train.py
```

---

## Working with Data

To access your local data inside the container, mount the folder:

```bash
docker run -v /absolute/path/to/local/data:/app/data your-project-name
```

Replace `/absolute/path/to/local/data` with your actual path.

---

## Running Scripts

You can run any Python script inside the container like this:

```bash
docker run your-project-name python src/<script_name>.py
```

For example:

```bash
docker run your-project-name python src/preprocess.py
```

---

## Stopping and Removing Containers

To list running containers:

```bash
docker ps
```

To stop a running container:

```bash
docker stop <container_id>
```

To remove a stopped container:

```bash
docker rm <container_id>
```
---

## License

[Specify your license here, e.g., MIT License]
