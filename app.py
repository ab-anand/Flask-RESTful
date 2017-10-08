from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import json

app = Flask(__name__)
api = Api(app)



# dummy data for end points
input = open('data.json')
data = json.load(input)
hospital = data['hospital']

services = {
    'services': [{
        'service-name': 'Pradhan Mantri jannani suraksha yojna',
        'details': 'Provides financial assistance of Rs. 500 upto 2 births to pregnant women who have attend 19 years of age and below poverty level.'
    }, {
        'service-name': 'Electronic Health Record',
        'details': 'Govt. introduced electronic health record(EHR) to make digitalize health care sector with better efficiency.'
    }, {
        'service-name': 'Strategic Purchase',
        'details': 'Strategic Purchase of secondary and tertiary health care services.'
    }, {
        'service-name': 'Health and Wellness centre',
        'details': 'Hospitals stock and staff surgical suites that can be used for outpatient services or in-depth procedures, such as transplants, heart surgery and repairing broken bones. '
    }, {
        'service-name': 'National Digital Health Authority',
        'details': 'It regulates and deploy national degital health care.'
    },
    {
        'service-name': 'Notification',
        'details': 'Zika virus notification'
    }]
}

complaint = data['complaint']


class Services(Resource):
    def get(self):
        return services


class Complaints(Resource):
    def get(self):
        return complaint

    def post(self):
        print(request)
        complaint.append({
            "name":request.json['name'],
            "email":request.json['email'],
            "contact":request.json['contact'],
            "description":request.json['description']
            })

        with open('data.json', 'w') as data_file:    
            data['complaint'] = complaint
            json.dump(data, data_file)

        return {'status': 'success'}

class Hospital(Resource):
    def get(self):
        return hospital

    def post(self):
        hospital.append({
            "name":request.json['name'],
            "cleanliness":request.json['cleanliness'],
            "facilities":request.json['facilties'],
            "doc-behaviour":request.json['doc-behaviour'],
            "quality-of-service":request.json['quality-of-service']
        })

        with open('data.json', 'w') as data_file:    
            data['hospital'] = hospital
            json.dump(data, data_file)

        return {'status':'success'}

api.add_resource(Services, '/services')
api.add_resource(Complaints, '/complaints')
api.add_resource(Hospital, '/hospital')

if __name__ == '__main__':
    app.run()
