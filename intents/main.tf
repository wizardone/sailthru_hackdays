provider "aws" {
  region = "us-east-1"
}

module "gpt3_sql" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "MaelStefanGPT3"
  description   = "SQL or other gpt3 flow"
  handler       = "sql.lambda_handler"
  runtime       = "python3.8"

  source_path = "./GPT3_sql"

  tags = {
    Name = "MaelStefanGPT3"
  }
}
