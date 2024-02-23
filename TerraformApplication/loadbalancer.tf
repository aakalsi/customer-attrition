resource "aws_lb_target_group" "churn_target_group" {
  deregistration_delay          = "300"
  load_balancing_algorithm_type = "round_robin"
  name                          = "churn-application-group"
  port                          = 5000
  protocol                      = "HTTP"
  protocol_version              = "HTTP1"
  tags                          = local.tags
  target_type                   = "ip"
  vpc_id                        = local.vpc_id

  health_check {
    enabled             = true
    healthy_threshold   = 5
    interval            = 30
    matcher             = "200"
    path                = "/health-status"
    port                = "traffic-port"
    protocol            = "HTTP"
    timeout             = 5
    unhealthy_threshold = 2
  }

  # stickiness {
  #   cookie_duration = 86400
  #   enabled         = false
  #   type            = "lb_cookie"
  # }
  depends_on = [
    aws_codebuild_project.churn_codebuild,
  ]
}

resource "aws_lb" "churn_load_balancer" {
  drop_invalid_header_fields = false
  enable_deletion_protection = false
  enable_http2               = true
  idle_timeout               = 60
  internal                   = false
  ip_address_type            = "ipv4"
  load_balancer_type         = "application"
  name                       = "churn-load-balancer"
  security_groups = [
    "sg-064c868d7198a8165",
  ]
  subnets = [
    "subnet-00c9bcb7a14f1b396",
    "subnet-0a074d6be4ea01da0",
    "subnet-09265dfbe13835049",
    "subnet-032aff34a77b9a30b",
    "subnet-09e9e85489a3c4459",
    "subnet-04163f6711a7eeef7",
  ]
  tags = local.tags
  depends_on = [
    aws_lb_target_group.churn_target_group,
  ]

}

resource "aws_lb_listener" "churn_connection" {
  load_balancer_arn = aws_lb.churn_load_balancer.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.churn_target_group.arn
  }
  depends_on = [
    aws_lb.churn_load_balancer,
  ]
}

output "churn_application_url" {
  value       = format("http://%s/churn-prediction", aws_lb.churn_load_balancer.dns_name)
  description = "Churn application's URL"
}