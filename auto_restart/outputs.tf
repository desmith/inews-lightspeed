output "lambda_arn" {
  value = aws_lambda_function.lambda.arn
}

output "trigger_schedule" {
  value = aws_cloudwatch_event_rule.schedule.schedule_expression
}
