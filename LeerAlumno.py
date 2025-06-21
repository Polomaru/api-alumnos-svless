import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    # Obtener el ítem
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    item = response.get('Item')
    if not item:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }
    # Devolver alumno
    return {
        'statusCode': 200,
        'alumno': item
    }
