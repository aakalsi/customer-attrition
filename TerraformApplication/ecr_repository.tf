resource "aws_ecr_repository" "churn_ecr_repo" {
  name                 = "churn_ecr_repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}