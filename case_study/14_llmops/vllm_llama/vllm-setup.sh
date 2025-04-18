#!/bin/bash

set -e

# Validate that HF Token is provided
if [ -z "$1" ]; then
    echo "Error: HUGGING_FACE_HUB_TOKEN is not provided."
    echo "Usage: $0 <HF_TOKEN>"
    exit 1
fi

#pull the latest image of vllm
sudo docker pull vllm/vllm-openai

#deploy the container
sudo docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=$1" \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model meta-llama/Llama-3.2-1B
    --dtype=half

# Install locust for performance testing

pip install locust

# Write locustfile.py
cat <<EOF > locustfile.py
from locust import HttpUser, task, between, events
import logging

class vLLMApiTestUser(HttpUser):

    wait_time = between(1, 2)

    host = None

    headers = {
            "Content-Type": "application/json"
            }


    @task
    def post_request(self):

        api_url = "/v1/completions"

        request_body = {
        "model": "meta-llama/Llama-3.2-1B",
        "prompt": "What is AWS?",
        "temperature": 0.7,
        "top_k": -1,
        "max_tokens": 500
        }

        with self.client.post(api_url, json=request_body, headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Request failed with status code {response.status_code}")  # Mark as failure if response is not 200

@events.request.add_listener
def on_request_event(request_type, name, response_time, response_length, exception, context, **kwargs):
    if exception:
        # Log failed requests
        logging.error(f"Request to {name} failed with exception: {exception}")
    else:
        # Log successful requests
        logging.info(f"Request to {name} succeeded in {response_time}ms with response length {response_length}")
EOF

# Run locust
python3 -m locust -f locustfile.py --host http://localhost:8000
