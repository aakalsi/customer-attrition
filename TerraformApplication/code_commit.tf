resource "aws_codecommit_repository" "code_repo" {
  repository_name = "churn_code_repo"
  description     = "This is a code comit repo"
  default_branch  = "master"
  tags = {
    application = "churn-prediction"
  }
}
output "code_repo_clone_url_http" {
  value       = aws_codecommit_repository.code_repo.clone_url_http
  description = " This is an ecr repo"
}
output "code_repo_clone_url_ssh" {
  value       = aws_codecommit_repository.code_repo.clone_url_ssh
  description = "The is the private IP address of the main server instance."
}