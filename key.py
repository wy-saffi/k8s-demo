import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def get_item(id):
  dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
  table = dynamodb.Table('HON_JNL_TBL')

  try:
    resp = table.get_item(Key={'JNL_ID': id})
  except ClientError as e:
    print(e.response['Error']['Message'])
  else:
    print(resp)

if __name__=='__main__':
  get_item("1")
  
