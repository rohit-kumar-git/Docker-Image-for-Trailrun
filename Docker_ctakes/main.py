# from pprint import pprint
# import datetime
# import random
import logging
import json
from re import S
# from azure.storage.filedatalake import DataLakeServiceClient
# from azure.storage.blob import BlobServiceClient
import os
#import string
# import pprint
#BlobClient
#ContainerClient

message = str(os.environ['blobDownload']) 
print(message)
logging.info(message) 
# pprint(message)

json_data = json.dumps(message).encode('utf-8')
logging.info(json_data)
print(json_data)
# pprint(json_data)


exit(0)
