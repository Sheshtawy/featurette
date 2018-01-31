import os

def get_env():
    env = os.environ.get('FEATURETTE_ENV', 'dev')
    return os.path.abspath('settings/{0}.py'.format(env))
