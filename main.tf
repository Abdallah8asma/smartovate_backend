# Déclaration de l'instance EC2 avec une interface réseau
resource "aws_instance" "app" {
  ami           = "ami-04cdc91e49cb06165"
  instance_type = "t3.medium"
  key_name      = "feriel_key"

  tags = {
    Name = "smartovate-backend"
  }

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.example.id
  }

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World!" > index.html
              nohup busybox httpd -f -p 80 &
              EOF
}

# Exemple de réseau pour l'interface réseau
resource "aws_network_interface" "example" {
  subnet_id       = aws_subnet.public-subnet-1.id
  security_groups = [aws_security_group.main.id]

  tags = {
    Name = "example-network-interface"
  }
}

# Exemples de sorties
output "ec2_instance_id" {
  value = aws_instance.app.id
}

output "ec2_public_ip" {
  value = aws_instance.app.public_ip
}
