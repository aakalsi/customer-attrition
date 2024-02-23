locals {
  code_build_service_role = "arn:aws:iam::964597617122:role/churn-application-role"
  code_commit_repo_name   = "churn_code_repo"
  code_commit_location    = "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/churn_code_repo"
  code_pipeline_role      = "arn:aws:iam::964597617122:role/codepipeline-service-role"
  ecs_service_role        = "arn:aws:iam::964597617122:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS"
  ecs_task_role           = "arn:aws:iam::964597617122:role/ecsTaskExecutionRole"
  vpc_id                  = "vpc-078ca2eab9c3ec172"
  tags = {
    application = "churn-prediction"
  }
}

