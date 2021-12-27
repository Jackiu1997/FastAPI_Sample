from config.config import Config, DevelopmentConfig, ProductionConfig, TestConfig

CONFIG = DevelopmentConfig

CONFIGS_ALL = {
    'DEV': DevelopmentConfig,
    'PRODUCT': ProductionConfig,
    'TEST': TestConfig,
}


def init_config(env: str = 'DEV'):
    if CONFIGS_ALL.get(env):
        CONFIG = CONFIGS_ALL[env]