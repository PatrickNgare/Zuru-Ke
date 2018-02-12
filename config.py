import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'hskjksnicnhdhjdsuhgcbuye87'
    SQLALCHEMY_DATABASE_URI = ''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
   

    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

    pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''    
    pass
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}