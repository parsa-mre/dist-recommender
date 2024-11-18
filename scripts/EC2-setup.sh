#!/bin/bash

# Update and install system packages
apt-get update
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    git

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Start Docker service
sudo systemctl start docker
sudo usermod -a -G docker $USER
sudo systemctl enable docker

# Clone the repository (replace with your actual repo URL)
git clone https://github.com/parsa-mre/dist-recommender /app

# Change to app directory
# Change to app directory
cd /app

# Create environment file
cat > .env << EOF
REDIS_URL=redis://${REDIS_HOST}:6379/0
EOF

# Start the appropriate service based on instance type
case "${INSTANCE_TYPE}" in
  "redis")
    sudo docker-compose up -d redis
    ;;
  "master")
    sudo docker-compose up -d master
    ;;
  "worker")
    sudo docker-compose up -d worker
    ;;
esac