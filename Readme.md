
Customer Attrition Forecasting (Banking Domain)


1. Prerequisites
Python 3.6 or higher
AWS account with appropriate permissions
Terraform 0.12.x or higher
Jupyter Notebook

2. Required Python libraries:
numpy
pandas
scikit-learn
tensorflow
Keras


3. Project Structure
data: contains the dataset used for training and testing the ML model.
model: contains the code for training and testing the ML model.
terraform: contains the code for deploying the trained model on AWS using Terraform.

4. Deployment Steps
Install all the required Python libraries.
Open the Jupyter Notebook file model/attrition_forecasting.ipynb.
Run the cells in the notebook to train and test the ML model.
Once the model is trained, navigate to the terraform directory.
Update the variables.tf file with your AWS credentials and desired settings for the deployment.
Initialize the Terraform configuration by running the command terraform init.
Validate the Terraform configuration by running the command terraform validate.
Preview the Terraform deployment plan by running the command terraform plan.
Deploy the trained model on AWS by running the command terraform apply.
Once the deployment is complete, you should see the AWS resources created in your account.
To destroy the AWS resources, run the command terraform destroy.
Run code pipeline in AWS to deploy the application 
