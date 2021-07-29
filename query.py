import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def query(memberid):
  dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
  table = dynamodb.Table('HON_JNL_TBL')

  try:
    resp = table.query(
      IndexName="MEM_INDEX",
      KeyConditionExpression=Key('JNL_PNT_MEM_NO').eq(memberid),
      ReturnConsumedCapacity='TOTAL', #ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    )
  except ClientError as e:
    print(e.response['Error']['Message'])
  else:
    print(resp)

if __name__=='__main__':

  query("2334")

