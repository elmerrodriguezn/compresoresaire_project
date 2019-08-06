import xmlrpc.client

db = 'mailync-lymservicios-master-66054'
username = 'LymServicios'
password = 'Buk27593'
url = 'https://lymservicios.odoo.com'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})