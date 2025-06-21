import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table    = dynamodb.Table('t_alumnos')
    # Eliminar el ítem
    table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    # Confirmación
    return {
        'statusCode': 200,
        'message': 'Alumno eliminado correctamente'
    }
