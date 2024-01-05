name             = "ec2_restart"
app              = "inews"
component        = "infra"
env              = "prod"
schedule         = "cron(0 */6 ? * * *)" # every 4 hours
email_recipients = "devaprastha@iskcon.org"
lambda_runtime   = "python3.12"
lambda_handler   = "restart_instance.py.lambda_handler"