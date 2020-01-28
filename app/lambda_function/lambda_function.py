import os
import sys

# add path
sys.path.append(os.path.join(os.path.dirname(__file__), 'packages'))

import http_client
import md2html_converter
import s3_client


def lambda_handler(event, context):
    original_url = event['queryStringParameters']['target']
    client = s3_client.S3Client(original_url)
    s3_obj_url = client.check_s3_object()
    if s3_obj_url is not None:
        return get_response(s3_obj_url)

    original_md = http_client.get_original_md(original_url)
    html = md2html_converter.convert(original_md)
    s3_obj_url = client.put_to_s3(html)
    return get_response(s3_obj_url)


def get_response(s3_obj_url):
    return {
        'statusCode': 301,
        'headers': {
            'Location': s3_obj_url
        }
    }



def main():
    import json

    qiita = 'https://qiita.com/guromityan/items/5846fcefd87abcf76f7f'

    event = {
       'queryStringParameters': {
           'target': qiita
       }
    }
    context = None
    response = lambda_handler(event, context)
    print(json.dumps(response, indent=2))


if __name__ == '__main__':
    main()

