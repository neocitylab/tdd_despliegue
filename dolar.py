import json
import boto3
from urllib.request import urlopen

def f(event, context):
    with urlopen("https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario") as response:
        body = response.read() 
    
    print(body)
    
    s3 = boto3.resource('s3')
    object=s3.Object('dolar-raw-127', 'dolar_timestamp.txt')
    object.put(Body=body)
    print("file uploaded successfully")
    
    return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
    }
