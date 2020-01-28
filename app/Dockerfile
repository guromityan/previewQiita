FROM python:3
WORKDIR /var/local/
COPY requirements.txt /var/local
COPY credentials /root/.aws/

RUN apt -y update && \
    apt -y install vim
RUN pip install -U pip && \
    pip install -r requirements.txt  -t lambda_function/packages/ --upgrade
RUN pip install boto3

CMD ["tail", "-f", "/dev/null"]

