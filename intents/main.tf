provider "aws" {
  region = "us-east-1"
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "MaelStefanGPT3"
  description   = "SQL or other gpt3 flow"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"

  source_path = "./GPT3"

  tags = {
    Name = "MaelStefanGPT3"
  }
}
