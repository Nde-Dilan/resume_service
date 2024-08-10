from flask_restful import Resource

class ResumeUploadAPI(Resource):
    def get(self):
        return {'message': 'List all resumes'}, 200

    def post(self):
        return {'message': 'Resume uploaded successfully'}, 201
