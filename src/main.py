from vocabulary_resource import VocabularyResource
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(VocabularyResource, "/vocabulary/<vocab>")
if __name__ == "__main__":
    app.run(debug=True)
