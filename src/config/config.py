class Config():
    pass
    # HOST = config('HOST')
    # PORT = config('PORT', cast=int)

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True