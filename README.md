# previewQiita
社内プロキシのせいで Qiita が見れない。。。

そんな方のために、AWS Lambda で使える関数を作成


# 使い方
以下のファイルを編集

**credentials**
```ini:credentials
[default]
aws_access_key_id = <YOUR KEY ID>
aws_secret_access_key = <YOUR ACCESS KEY>
```

**s3_client.py**
```python:s3_client.py
AWS_S3_BUCKET_NAME = 'YOUR S3 BUCKET NAME'
AWS_S3_REGION = 'YOUR S3 REGION'
```

編集したら、以下のコマンドを実行
```
$ docker-compose build
$ docker-compose up -d
```

あとは好きなように編集し、`lambda_function` ディレクトリ内で以下を実行し固める
```
$ zip -r lambda.zip ./*
```

zip に固めた物を、AWS Lambda にアップロードして使用



