from fabric.api import env, sudo, task, run, put, get, parallel
from ConfigParser import ConfigParser


config = ConfigParser()
config.read('nbssh.ini')
section = 'default'
# print config.get(section, 'hosts').split(',')
env.hosts = config.get(section, 'hosts').split(',')
env.port = config.getint(section, 'port')
env.user = config.get(section, 'user')
env.password = config.get(section, 'password')
env.sudo_password = env.password


@task(default=True)
def default():
    run('pwd')
