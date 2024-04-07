# Scalable Video Streaming Service

## Overview
This repository contains the foundational code for a basic video streaming service backend, designed with scalability and adaptability in mind. The service aims to provide a framework for streaming educational content with low latency and adaptive streaming quality.

## Features
- Flask web server for handling HTTP requests.
- Redis integration for caching video content.
- Adaptive bitrate streaming to adjust video quality based on user bandwidth.
- Placeholder functions for simulating video content fetching and quality determination.

## Approach
The service is structured around a Flask application, which serves as the entry point for all video streaming requests. The application is designed to be stateless, allowing it to scale horizontally by adding more instances behind a load balancer.

### Content Delivery
- Video content is streamed through the `/stream/<video_id>` endpoint.
- Redis is used as a caching layer to store and quickly retrieve video content, reducing the load on the storage backend.

### Adaptive Bitrate Streaming
- The `/adaptive_stream/<video_id>` endpoint simulates adaptive bitrate streaming.
- The service estimates the user's bandwidth and selects an appropriate video quality.
- A manifest file is generated dynamically, pointing to video segments of the selected quality.

## Assumptions
- The code assumes the existence of a separate storage service (like AWS S3) for video content.
- Bandwidth estimation and video quality selection are simulated with placeholder functions.
- The actual implementation of video segment fetching and streaming is not included.

## Installation
To run this project, you'll need Python 3 and the following Python packages: Flask and Redis.

Install the required packages using:

pip install Flask redis


Running the Service
Start the service by running the Flask application:

python app.py

Security Note
This code is intended for educational purposes and does not include security features necessary for a production environment, such as authentication, encryption, and protection against common web vulnerabilities.

Future Work
Integrate with a real video storage service.
Implement actual bandwidth estimation and video quality switching logic.
Add security features for production readiness.
Set up a load balancer and auto-scaling policies for handling high traffic.