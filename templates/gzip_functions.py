import sys
import tarfile
import cStringIO
import base64
import re

base_template = 'linux-base-userdata.sh.tmpl'
func_template = 'linux-base-functions.sh'

buffer = cStringIO.StringIO()
tar = tarfile.open(fileobj=buffer, mode="w:gz")
tar.add('%s' % func_template)
tar.close()

buffer.reset()
enc_functions = base64.b64encode(buffer.read())

buffer.close()

new_data = None
with open('%s' % base_template,'r') as userdata:
    data = userdata.read()
    new_data = re.sub('GZIP_FUNCTIONS=.*\n', 'GZIP_FUNCTIONS="%s"\n' % enc_functions, data)

if new_data is None:
    print 'Failed in getting original file content'
    sys.exit(1)

with open('%s' % base_template,'w') as userdata:
    userdata.write(new_data)
    print 'File content is updated'
