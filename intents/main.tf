provider "aws" {
  region = "us-east-1"
}

module "gpt3" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "MaelStefanGPT3"
  description   = "SQL or other gpt3 flow"
  handler       = "gpt3.lambda_handler"
  runtime       = "python3.8"

  source_path = "./GPT3"

  tags = {
    Name = "MaelStefanGPT3"
  }
}
