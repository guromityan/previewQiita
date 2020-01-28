import boto3
from botocore.exceptions import ClientError

import http_client
import md2html_converter


AWS_S3_BUCKET_NAME = 'YOUR S3 BUCKET NAME'
AWS_S3_REGION = 'YOUR S3 REGION'

s3 = boto3.resource('s3')


class S3Client(object):
    def __init__(self, url):
        self.get_s3_obj_name(url)
        self.get_s3_obj_url()
        self.s3_obj = s3.Object(AWS_S3_BUCKET_NAME, self.s3_obj_name)

    def get_s3_obj_name(self, url):
        metadata = url.split('/')
        user = metadata[3]
        item_id = metadata[5]
        self.s3_obj_name = f'{ user }_{ item_id }.html'

    def get_s3_obj_url(self):
        self.s3_obj_url = f'https://{ AWS_S3_BUCKET_NAME }.s3-{ AWS_S3_REGION }.amazonaws.com/{ self.s3_obj_name }'


    def check_s3_object(self):
        try:
            self.s3_obj.get()
            return self.s3_obj_url

        except ClientError as e:
            return None

    def put_to_s3(self, html):
        self.s3_obj.put(
            Body = html.encode('utf-8'),
            ContentEncoding = 'utf-8',
            ContentType = 'text/html'
        )
        return self.s3_obj_url

