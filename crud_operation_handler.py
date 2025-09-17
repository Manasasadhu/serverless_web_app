import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    http_method = event['httpMethod']

    if http_method == 'POST':
        # Create a new student record
        student = json.loads(event['body'])
        table.put_item(Item=student)
        return {
            'statusCode': 200,
            'body': json.dumps('Student record added successfully')
        }

    elif http_method == 'GET':
        # Fetch student record by student_id
        student_id = event['queryStringParameters']['student_id']
        response = table.get_item(Key={'student_id': student_id})
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Student record not found')
            }

    elif http_method == 'PUT':
        # Update an existing student record
        student = json.loads(event['body'])
        student_id = student['student_id']

        update_expression = "set #nm = :n, course = :c"
        expression_attribute_values = {
            ':n': student['name'],
            ':c': student['course']
        }
        expression_attribute_names = {
            '#nm': 'name'  # 'name' is a reserved word in DynamoDB
        }

        table.update_item(
            Key={'student_id': student_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Student record updated successfully')
        }

    elif http_method == 'DELETE':
        # Delete a student record by student_id
        student_id = event['queryStringParameters']['student_id']

        table.delete_item(Key={'student_id': student_id})
        return {
            'statusCode': 200,
            'body': json.dumps('Student record deleted successfully')
        }

    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported HTTP method')
        }