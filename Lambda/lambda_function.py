import json
import pprint
import boto3
# from boto3.dynamodb.conditions import Key

USER_TABLE_NAME = "self_introduction_tutorial"
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    pprint.pprint(event, width=40)

    response = {'statusCode': 200, 'body': ''}
    user_table = dynamodb.Table(USER_TABLE_NAME)

    if ('method' in event) and (event['method'] == 'update'):
        validate_event_attribute_list = ['hobbyList', 'selfIntroductionMessage']
        if not all((attribute in event) for attribute in validate_event_attribute_list):
            response['body'] = json.dumps("Error Message: Not include hobbyList or selfIntroductionMessage")
            response['statusCode'] = 400
            return response

        try:
            user_table.update_item(
                Key={"id": "1"},
                UpdateExpression="SET hobbyList = :hobbyList, selfIntroductionMessage = :selfIntroductionMessage",
                ExpressionAttributeValues={
                    ":hobbyList": event['hobbyList'],
                    ":selfIntroductionMessage": event['selfIntroductionMessage']
                })
            response['body'] = json.dumps("Update Success")
            response['statusCode'] = 200
        except Exception as err:
            print("Error Message: {0}".format(err))
            response['body'] = json.dumps("Error Message: {0}".format(err))
            response['statusCode'] = 500
    else:
        try:
            response['body'] = user_table.get_item(Key={"id": "1"})["Item"]
            response['statusCode'] = 200
        except Exception as err:
            print("Error Message: {0}".format(err))
            response['body'] = json.dumps("Error Message: {0}".format(err))
            response['statusCode'] = 500
    return response
