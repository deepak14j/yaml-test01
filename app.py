import azure.functions as func
#from azure.functions import HttpRequest
import json

app = func.FunctionApp()

@app.route('hello', methods=['GET'])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(f'Url of the caller is {json.dumps(req.url)}')

