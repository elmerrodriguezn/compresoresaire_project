from api_connection import *

class Connection:
    models = models
    db = db
    uid = uid
    password = password

    def execute(self, model, operation, query, fields=''):
        return models.execute_kw(db, uid, password, model, operation, [query], fields)

class Query(Connection):
    def get(self, model, operation, query='', fields=''):
        return super().execute(model, operation, query, fields)
    def create(self, model, operation, query):
        super().execute(model, operation, query)
        pass