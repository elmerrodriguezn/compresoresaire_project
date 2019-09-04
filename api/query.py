from api_connection import *


class Connection:
    models, db, uid, password = (models, db, uid, password)

    def execute(self, model, operation, query, fields=''):
        return models.execute_kw(self.db, self.uid, self.password, model, operation, [query], fields)


class Query(Connection):
    def get(self, model, operation, query, fields=''):
        return super().execute(model, operation, query, fields)

    def create(self, model, operation, query):
        super().execute(model, operation, query)
        pass
