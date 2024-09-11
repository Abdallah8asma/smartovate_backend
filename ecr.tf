#provider "aws" {
#  region = "eu-north-1"
#}

resource "aws_ecr_repository" "main" {
  name = "my-ecr-repo"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name        = "my-ecr-repo"
    Environment = "Production"
  }
}

output "repository_url" {
  value = aws_ecr_repository.main.repository_url
}
