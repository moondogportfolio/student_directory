from flask import Flask, render_template, make_response, jsonify, request, abort, Response
from pymongo import MongoClient
from json import dumps
import os
from sample_data import sample1, sample2, violation_sample

# sample API address
# source = 'mongodb+srv://<username>:<password>@cluster0.spy9n.mongodb.net/?retryWrites=true&w=majority'
# source = os.environ.get('API')
# client = MongoClient(source)
# db = client.testdb
# collection = db.testcoll
# violations = db.violations

app = Flask(__name__)




@app.route('/add_violation', methods=['POST'])
def add_violation():
    updateData = request.get_json()
    violation_sample.append({'name':updateData['name'], 'date':updateData['dates'], 'details':updateData['details'], 'infraction':updateData['infraction']})
    # db.violations.insert_one({'name':updateData['name'], 'date':updateData['dates'], 'details':updateData['details'], 'infraction':updateData['infraction']})
    return Response(status='200')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/certificate')
def certificate():
    #details = request.get_json()
    return render_template('report.html')



@app.route('/fetchData', methods=('GET', 'POST'))
def find():
    query = request.get_json()
    search = query['query']
    fetchedData = None
    if search.isnumeric():
        if int(search) == 200901010:
            fetchedData = sample1
        elif int(search) == 200971717:
            fetchedData = sample2
    else:
        if search == 'Edmondo Jamermer':
            fetchedData = sample2
        elif search == 'Josephine Bracken':
            fetchedData = sample1
    
    # SIMULATE DATA FETCH

    # if query['query'].isnumeric():
    #     fetchedData = collection.find_one({"student_number": int(query['query'])})
    # else:
    #     fetchedData = collection.find_one({"name": query['query']})
    if fetchedData == None:
        return abort(404)
    else:
        # fetchedData.pop('_id')
        # violationsData = list(violations.find({"name": fetchedData['name']}))
        # if violationsData:
        #     [(violationsData[idx].pop('_id'), violationsData[idx].pop('name')) for idx, val in enumerate(violationsData)]
        #     fetchedData['violations'] = violationsData
        violations = []
        for violation in violation_sample:
            if violation['name'] == fetchedData['name']:
                violations.append(violation)
        if violations:
            fetchedData['violations'] = violations
        print('fetched data is', dumps(fetchedData))
        return make_response(jsonify(fetchedData), 200)



if __name__ == '__main__':
    app.run(debug=True)
    #app.run()
