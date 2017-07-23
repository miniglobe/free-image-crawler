# -*- coding: utf-8 -*-
from urllib import request
from google.cloud import storage

DATA_STORE_KEY_PATH = "/home/vagrant/.json_keys/persian-3a9988725cae.json"
STORAGE_STORE_KEY_PATH = "/home/vagrant/.json_keys/persian-efe392f65854.json"
PROJECT_ID = "persian-172808"

class Repository(object):
  
  def __init__(self):
    self.storage_client = storage.Client()
    self.datastore_client = datastore.Client.from_service_account_json(DATA_STORE_KEY_PATH, project=PROJECT_ID)
    self.bucket = self.storage_client.get_bucket(BUCKET_NAME)
    self.key = self.datastore_client.key('free_image')

  