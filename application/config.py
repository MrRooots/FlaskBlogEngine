import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))


class Config:
  DEBUG = True
  SECRET_KEY = 'SS+3)KmnR4#+XaKj2KM1`XR)^[4=9]qt/".`4[c(*ks3)l7;&qC8%ARl}~^lE*q'

  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SECURITY_PASSWORD_SALT = 'somewordstosaythatshitisshitafterall'
  SECURITY_PASSWORD_HASH = 'sha512_crypt'
