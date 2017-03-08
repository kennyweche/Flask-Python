# config.py

class Config(object):
	""" Common configurations """

	# Puts any configurations here that are common on all environments
	DEBUG = True

class DevelopmentConfig(Config):
	""" Development configurations """

	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	""" Production configurations """

	DEBUG = False


class TestingConfig(Config):
	""" Testing configurations """

	TESTING = True


app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
 
