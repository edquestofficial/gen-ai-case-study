#!/bin/bash

set -e

# Update system packages
echo "Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install nvidia device drivers

sudo apt update --fix-missing && apt-get install alsa-utils -y
sudo apt install ubuntu-drivers-common -y
sudo ubuntu-drivers autoinstall 

# Install prerequisites for Docker
echo "Installing prerequisites for Docker..."
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    gnupg

# Add Docker's official GPG key
echo "Adding Docker's official GPG key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the Docker stable repository
echo "Setting up Docker stable repository..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
echo "Installing Docker..."
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Create /etc/docker directory
echo "Creating /etc/docker directory..."
sudo mkdir -p /etc/docker
sudo chmod 0755 /etc/docker

# Set up Docker daemon.json
echo "Setting up Docker daemon.json..."
cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
EOF
sudo chown root:root /etc/docker/daemon.json
sudo chmod 0644 /etc/docker/daemon.json

# Restart Docker
echo "Restarting Docker..."
sudo systemctl restart docker

# Add NVIDIA's GPG key
echo "Adding NVIDIA's GPG key..."
"curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list"

# Install NVIDIA Container Toolkit
echo "Installing NVIDIA Container Toolkit..."
sudo apt-get update -y
sudo apt --yes install \
    nvidia-container-runtime=$(apt-cache madison nvidia-container-runtime | grep 3.14.0-1 | head -1 | awk '{print $3}') \
    nvidia-container-toolkit-base=$(apt-cache madison nvidia-container-toolkit-base | grep 1.17.4-1 | head -1 | awk '{print $3}') \
    nvidia-container-toolkit=$(apt-cache madison nvidia-container-toolkit | grep 1.17.4-1 | head -1 | awk '{print $3}')

# Configure NVIDIA Container Runtime
echo "Configuring NVIDIA Container Runtime..."
sudo nvidia-ctk runtime configure --runtime=docker

# Restart Docker to apply changes
echo "Restarting Docker..."
sudo systemctl restart docker

echo "Docker, NVIDIA Docker, and NVIDIA Container Runtime setup completed successfully!"

# Reboot system to load nvidia-smi and it's configuration as runtime
echo "Rebooting system, Refresh after 60 seconds ..."
sudo reboot
