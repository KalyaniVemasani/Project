# Web Server Security Group (for EC2 / ALB)
resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Allow HTTP, HTTPS, and SSH"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # You can restrict this to your IP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web-sg"
  }
}

# Database Security Group (for RDS)
resource "aws_security_group" "db_sg" {
  name        = "db-sg"
  description = "Allow MySQL/PostgreSQL from private subnets"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    description = "Allow DB access from EC2 in VPC"
    from_port   = 3306 # Change to 5432 if using PostgreSQL
    to_port     = 3306
    protocol    = "tcp"
    security_groups = [aws_security_group.web_sg.id] # Allow access from web SG
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "db-sg"
  }
}
