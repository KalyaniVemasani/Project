import boto3


ec2 = boto3.client('ec2')


response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)


print(" Running EC2 Instances:\n")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        public_ip = instance.get('PublicIpAddress', 'No Public IP')
        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")
        print(f"Public IP: {public_ip}")
        print("-" * 30)
