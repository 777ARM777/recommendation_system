# Recommendation System

## Overview

This repository contains a simple recommendation system consisting of two main services:

1. **Generator Service**: Generates recommendations based on a model name and viewer ID.
2. **Invoker Service**: Retrieves and merges recommendations, using caching for efficiency.

The solution is containerized using Docker and orchestrated with Docker Compose.

## Services

### Generator Service

The Generator service generates recommendations and provides a single POST endpoint:

- **Endpoint**: `/generate`
- **Method**: POST
- **Parameters**:
  - `model_name` (string): The name of the recommendation model.
  - `viewerid` (string): The ID of the viewer.
- **Response**:
  ```json
  {
    "reason": "<MODELNAME>",
    "result": <RANDOMNUMBER>
  }
  ```

### Invoker Service

The Invoker service retrieves recommendations and manages caching. It includes:

- **Endpoint**: `/recommend`
- **Method**: GET
- **Parameters**:
  - `viewerid` (string): The ID of the viewer.
- **Response**:
  {
    "recommendations": [
      {"reason": "<MODELNAME>", "result": <RANDOMNUMBER>}
    ]
  }

## Caching

The Invoker service uses two levels of caching:

- **Local Cache**:
  - TTL: 10 seconds
  - Limit: 3 keys

- **Redis Cache**: Used if data is not found in the local cache.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Running the Services

1. **Clone the Repository**:
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_NAME>

2. **Build and Start the Services**:
   docker-compose up --build

3. **Verify the Services**:

   - **Generator Service**: Ensure it is running and accessible at `http://localhost:5000/generate`.
   - **Invoker Service**: Ensure it is running and accessible at `http://localhost:5000/recommend`.

## Testing

### Testing with Postman or cURL

1. **Test the Generator Service**:
   - **URL**: `http://localhost:5000/generate`
   - **Method**: POST
   - **Body**:
     {
       "model_name": "model1",
       "viewerid": "user123"
     }
   - **Expected Response**:
     {
       "reason": "model1",
       "result": <RANDOMNUMBER>
     }

2. **Test the Invoker Service**:
   - **URL**: `http://localhost:5000/recommend`
   - **Method**: GET
   - **Parameters**: `viewerid=user123`
   - **Expected Response**:
     {
       "recommendations": [
         {"reason": "model1", "result": <RANDOMNUMBER>}
       ]
     }

### Testing Caching

- **Local Cache**: Verify that repeated requests within 10 seconds return cached results.
- **Redis Cache**: Verify that data is correctly retrieved from Redis if not present in the local cache.

## Troubleshooting

- **404 Not Found**: Ensure the service is running and the URL is correct. Check the logs for errors.
- **Service Logs**: Use `docker logs <container_id>` to view logs and diagnose issues.

## Docker Compose Configuration

The `docker-compose.yml` file defines the services and their configurations. Review it for details on service definitions, port mappings, and environment variables.

## Conclusion

This recommendation system demonstrates a basic setup with caching to improve performance. Adjust the implementation and configuration as needed for your specific requirements.
