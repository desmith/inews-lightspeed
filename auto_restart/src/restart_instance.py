import boto3

region = 'us-east-1'
topic_arn = 'arn:aws:sns:us-east-1:793753096261:my-topic'

ec2 = boto3.client('ec2', region_name=region)
sns = boto3.client('sns', region_name=region)

_filter = [
    {'Name': 'tag:auto_restart', 'Values': ['True']}
]

response = ec2.describe_instances(Filters=_filter)
instances = []

for instance in response['Reservations']:
    for i in instance['Instances']:
        instances.append(i['InstanceId'])


def lambda_handler(event, context):  # pylint: disable=unused-argument
    ret = ec2.reboot_instances(InstanceIds=instances)
    print(f'stopped your instances: {instances}')
    print(f'{ret=}')

    str_msg = f'Instances {instances} restarted'
    msg_response = sns.publish(TopicArn=topic_arn, Message=str_msg)
    print(f'Message published: {msg_response}')
