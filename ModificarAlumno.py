import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id    = event['body']['tenant_id']
    alumno_id    = event['body']['alumno_id']
    nuevos_datos = event['body']['alumno_datos']
    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table    = dynamodb.Table('t_alumnos')
    # Actualizar únicamente el mapa alumno_datos
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression='SET alumno_datos = :datos',
        ExpressionAttributeValues={
            ':datos': nuevos_datos
        },
        ReturnValues='ALL_NEW'
    )
    actualizado = response.get('Attributes')
    # Devolver versión actualizada
    return {
        'statusCode': 200,
        'alumno_actualizado': actualizado
    }
