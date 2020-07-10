import os
import json
import googleapiclient.discovery

class CustomClient:
  def __init__(self):
    self.compute = googleapiclient.discovery.build('compute', 'v1')
    self.project = os.getenv('GCP_PROJECT')
    self.zone = 'us-central1-a'

def list(request):
    client = CustomClient()
    instances_list = client.compute. \
        instances(). \
        list(project=client.project, zone=client.zone). \
        execute()
    result = instances_list['items'] if 'items' in instances_list else []
    return json.dumps(result)
