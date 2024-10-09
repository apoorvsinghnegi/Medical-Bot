# Medical-Bot

A conversational medical bot leveraging LangChain, GPT, and Pinecone to offer AI-powered medical assistance.

## How to Run the Project

Follow the steps below to clone the repository, set up the environment, and deploy the application.

### Steps to Run Locally

#### STEP 01- Clone the Repository

Clone the repository using the following command:

git clone https://github.com/apoorvsinghnegi/Medical-Bot

#### STEP 02- Create a conda environment after opening the repository

conda create -n medibot python=3.10 -y

conda activate medibot

#### STEP 03- Install the Requirements

pip install -r requirements.txt

#### STEP 04- Configure API Keys

PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#### STEP 05- Store Embeddings in Pinecone

run the following command to store embeddings to pinecone
python store_index.py

#### STEP 06- Run the Application

Finally, run the application using the following command:
python app.py

#### STEP 07- Access the Application

Once the application is running, open your browser and go to:
http://localhost:8080

#### Techstack Used:

Python
LangChain
Flask
GPT
Pinecone


#### AWS-CICD-Deployment-with-Github-Actions
##### 1. Login to AWS console.
##### 2. Create IAM user for deployment
The IAM user should have specific access permissions for deployment:

EC2 Access: For launching virtual machines.
ECR Access: For storing Docker images in AWS Elastic Container Registry (ECR).

Description: About the deployment

1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2

Policy:

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

##### Create ECR repo to store/save docker image

Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

##### Create EC2 machine (Ubuntu)

##### Open EC2 and Install docker in EC2 Machine:

Update and upgrade the system (optional)

sudo apt-get update -y
sudo apt-get upgrade -y

Install Docker (required)

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

##### Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

##### Setup github secrets:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY