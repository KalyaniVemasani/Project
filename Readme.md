 

 Deploying a Scalable AWS Architecture with Infrastructure as Code 
Overview:
This project is about designing and implementing a scalable cloud architecture on AWS using Infrastructure as Code. I used Terraform for networking setup, CloudFormation for resource deployment, Python Boto3 scripts for AWS interactions, and GitHub for version control.
Description:
In this project, my main goal was to build a scalable and reliable cloud environment on AWS. I started by setting up a secure network using a VPC with public and private subnets. Then, I deployed EC2 instances behind an Application Load Balancer to handle web traffic efficiently. To manage data storage, I used an RDS database hosted inside the private subnet.
I also configured an S3 bucket for storing static files, logs, and backups. To make the architecture more automated, I created a Lambda function that triggers whenever a new file is uploaded to S3, and logs the details in CloudWatch.
For deployment, I used Terraform to build the networking components and CloudFormation templates to launch EC2 instances, RDS, and Lambda. I wrote Python scripts using Boto3 to automate simple AWS tasks like uploading files to S3 and listing EC2 instances.
All my scripts were pushed regularly to GitHub. 
Architecture Overview
The project includes:
- VPC with Public and Private Subnets
- Application Load Balancer routing traffic to Auto-Scaling EC2 Instances
- RDS Database inside the private subnet
- S3 Bucket for storing static files, logs, and backups
- Lambda function triggered on S3 uploads to log events in CloudWatch
- Security Groups for access control
- Terraform for networking setup
- CloudFormation for provisioning EC2, RDS, and Lambda
- GitHub to store all project files
Tools and Technologies Used
- AWS Management Console and CLI
- Terraform
- AWS CloudFormation
- Python with Boto3
- GitHub
Project Structure
 terraform/              
 cloudformation/         
 boto3-scripts/           
 architecture         
 README.md                 
