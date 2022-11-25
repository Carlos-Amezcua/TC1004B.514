import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import time 
from datetime import datetime
import random

cred = credentials.Certificate('credentials.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

while True:
  print ("Sending data")
  current_date = datetime.now()
  date = current_date.strftime('%Y-%m-%d')
  hour = current_date.strftime('%H')
  collectionName = u'sensor_1_${0}'.format(date)
  encendido = bool(random.getrandbits(1))
  
  totals_ref = db.collection(collectionName).document(hour)
  totals_doc = totals_ref.get()
  totals_data = totals.to_dict()
  if totals_data == None:
    totals_ref.set({
      u'minutos_encendido': 1 if encendido else 0,
      u'minutos_apagado': 1 if not encendido else 0
    })
  else:
    if encendido:
      totals_ref.update({
        u'minutos_encendido': totals_data[u'minutos_encendido'] + 1
      })
    else:
      totals_ref.update({
        u'minutos_apagado': totals_data[u'minutos_apagado'] + 1
      })
  hour_ref = bd.collection(collectionName).document(hour)
  
  if hour_data == None:
    hour_ref.set({
      u'minutos_encendido': 1 if encendido else 0,
      u'minutos_apagado': 1 if not encendido else 0
    })
  else:
    if encendido:
      hour_ref.update({
        u'minutos_encendido': hour_data[u'minutos_encendido'] + 1
      })
    else:
      hour_ref.update({
        u'minutos_apagado': hour_data[u'minutos_apagado'] + 1
      }) 