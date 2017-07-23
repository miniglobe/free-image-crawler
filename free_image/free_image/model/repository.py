# -*- coding: utf-8 -*-
from urllib import request
from google.cloud import storage
from google.cloud import datastore
from datetime import datetime
import uuid

DATA_STORE_KEY_PATH = "/home/vagrant/.json_keys/persian-3a9988725cae.json"
STORAGE_STORE_KEY_PATH = "/home/vagrant/.json_keys/persian-efe392f65854.json"
PROJECT_ID = "persian-172808"
BUCKET_NAME = "persian-172808.appspot.com"


class Repository(object):
  
  def __init__(self):
    self.storage_client = storage.Client()
    self.datastore_client = datastore.Client.from_service_account_json(DATA_STORE_KEY_PATH, project=PROJECT_ID)
    self.bucket = self.storage_client.get_bucket(BUCKET_NAME)
    self.key = self.datastore_client.key('free_image_data')

  
  def _register(self, items):
    '''登録処理
    '''
    if not items['origin_url'] or self._duplicate(items):
      return
    self._put(items)


  def _put(self, items):
    '''Cloudにデータを保存します
    '''
    self._put_storage(items)
    self._put_datastore(items)


  def _put_storage(self, items):
    '''Cloud Storageに画像を保存
    '''
    res = request.urlopen(items['origin_url'])
    blob = self.bucket.blob('free_image' + '/' + uuid.uuid4().hex)
    blob.upload_from_string(res.read())
    blob.make_public()
    items['image_url'] = blob.public_url


  def _put_datastore(self, items):
    '''DataStoreにEntityを生成
    '''
    entity = datastore.Entity(self.key, exclude_from_indexes=('text', 'title'))
    entity.update({
      'image_url': items['image_url']
      , 'origin_url': items['origin_url']
      , 'created': datetime.now()
    })
    self.datastore_client.put(entity)


  def _duplicate(self, items):
    '''データの重複をチェックします
    重複データ対してにTrue、新規データに対してFalseを返却
    '''
    query = self.datastore_client.query(kind='free_image_data')
    query.add_filter('origin_url', '=', items['origin_url'])
    return len(list(query.fetch())) != 0

  
  def __call__(self, items):
    '''Repositoryクラスのデータ保存用の関数のエントリーポイント
    self._register()のエイリアス
    こっちをcallしてください
    '''
    self._register(items)