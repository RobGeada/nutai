import os

import connexion

import nutai.api as api

app = connexion.FlaskApp(__name__)

# setup operationIds
nut = api.Nut()
api.similarById = nut.similarById
api.similarByContent = nut.similarByContent
api.addDocument = nut.addDocument
api.addDocuments = nut.addDocuments
api.status = nut.status

app.add_api('nutai.yaml')

app.run(port=os.getenv('PORT'))
