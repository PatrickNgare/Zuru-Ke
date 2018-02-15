import os


class Config:
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      SECRET_KEY='jdhbfhhbfnbfdhfdhdhbhcbdbvd44555'

      @staticmethod
      def init_app(app):
            pass

class ProdConfig(Config):
      SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
      pass

class DevConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pasco:12345@localhost/zuru'
      DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}