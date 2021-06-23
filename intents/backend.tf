#######################################
# Terraform backend configuration
#######################################
terraform {
  required_version = "1.0"

  backend "s3" {
    bucket = "st-hackdays-tf"
    key    = "intents"
    region = "us-east-1"
  }
}



