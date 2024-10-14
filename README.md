# Port Scanning Application

## Overview

This project is a **Port Scanning Application** built using Python, Docker, and Jenkins. It scans a specified range of ports on a target IP address to determine which ports are open or closed. This application can be used for network security assessments and monitoring.

## Features

- Efficient port scanning using Python's socket programming and multithreading.
- Containerized application using Docker for easy deployment.
- CI/CD pipeline integration with Jenkins for automated builds and testing.

## Technologies Used

- **Python**: For developing the port scanning logic.
- **Docker**: To containerize the application.
- **Jenkins**: For continuous integration and continuous deployment (CI/CD).
- **Concurrent Futures**: To handle multiple threads for efficient scanning.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your machine.
- Jenkins installed and configured.
- Basic understanding of Python and networking concepts.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/manikanta9550/Breadcrumbsip-and-port-scanner.git

Navigate to the project directory:
cd your-repository

Build the Docker image:
docker build -t portscan-image .

Usage
To run the port scanning application in a Docker container, execute the following command:
docker run -it --rm portscan-image

The application will prompt you to enter the target IP address and the port range you wish to scan (e.g., 1-1000).
Example
Enter the target IP address: 192.168.1.1
Enter port range (e.g., '1-1000'): 1-100

Jenkins Integration
This project includes a Jenkins pipeline configuration (Jenkinsfile) to automate the build and deployment process. Follow these steps to set up the pipeline:

Ensure Jenkins is running and Docker is installed on your Jenkins server.
Create a new Jenkins job and point it to this repository.
Configure the job to use the Jenkinsfile included in the repository.
Jenkins Pipeline Stages
Clone Repository: Clones the repository containing the port scanning code.
Build Docker Image: Builds the Docker image for the application.
Run Docker Container: Runs the Docker container with the port scanning application.
Contributing
Contributions are welcome! To contribute to this project, follow these steps:

Fork the repository.
Create a new branch:
git checkout -b feature/YourFeature
Make your changes and commit them:
git commit -m 'Add your feature'
Push to the branch:
git push origin feature/YourFeature
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Manikanta - manikantareddy1090@gamil.com
GitHub: manikanta9550

Acknowledgments
Python Socket Programming Documentation
Concurrent Futures Documentation
Docker Documentation
Jenkins Documentation
