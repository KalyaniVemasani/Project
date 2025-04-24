import boto3

s3 = boto3.client('s3')
bucket_name = 'mys3bucketfor698'


s3.create_bucket(Bucket=bucket_name)
print(f"Bucket {bucket_name} created.")


s3.upload_file('examplefile.txt', bucket_name, 'examplefile.txt')
print("File uploaded.")
