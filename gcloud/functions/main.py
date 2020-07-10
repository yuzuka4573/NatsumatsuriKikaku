import json
import os

import googleapiclient.discovery

compute = googleapiclient.discovery.build('compute', 'v1')
project = os.getenv('GCP_PROJECT')
zone = 'us-central1-a'
instance = 'instance-1'

def get(request):
    result = compute.instances() \
        .get(project=project, zone=zone, instance=instance) \
        .execute()
    return result['status']

def start(request):
    result = compute.instances() \
        .start(project=project, zone=zone, instance=instance) \
        .execute()
    return result['status']

def stop(request):
    result = compute.instances() \
        .stop(project=project, zone=zone, instance=instance) \
        .execute()
    return result['status']
