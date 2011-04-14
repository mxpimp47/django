import sys, os



sys.path.append('/path/to/django')

sys.path.append('path/to/testproject')

os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'



from testproject.links import utils

client = urils.DeliciousClient('username','passwd')

data = client.fetch()

utils.create_link(data)