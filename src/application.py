from flask import Flask, Response, request, render_template
from datetime import datetime
import json
from columbia_student_resource import ColumbiaStudentResource
from qualifying_resource import F1
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)

@app.route('/')
def Home():
    return render_template('../../front-end/template/Home.html')

@app.route("/f1/qualifying/add/")
def ad():
    return render_template('../../front-end/template/add.html')

@app.route("/f1/qualifying_all", methods = ['GET'])
def qualifying():
    q = F1.get_qualifying()
    if q:
        rsp = Response(json.dumps(q), status=200, content_type="application/json")
    else:
        rsp = Response(json.dumps(q), status=404, content_type="text/plain")
    return rsp


@app.route("/f1/qualifying/add/", methods = ['POST'])
def add_circuits():
    qualifyId = request.form.get('qualifyId')
    raceId = request.form.get('raceId')
    driverId = request.form.get('driverId')
    constructorId = request.form.get('constructorId')
    number = request.form.get('number')
    position = request.form.get('position')
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    res = F1.append_new_circuits_name(qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3)
    if res:
        return '<script> alert("Fail to add data");location.href = "/";</script>'
    else:
        return '<script> alert("Success");location.hred = "/";</script>'


@app.route('/f1/qualifying/update')
def update():
    return render_template('PUT.html')
@app.route('/f1/qualifying/update/', methods = ['PUT'])
def update_circuits():
    qualifyId = request.form.get('qualifyId')
    driverId = request.form.get('driverId')
    res = F1.update_circuits(qualifyId, driverId)
    if res:
        return '<script> alert("Fail to update data");location.href = "/";</script>'
    else:
        return '<script> alert("Success");location.hred = "/";</script>'










@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/api/students/<uni>", methods=["GET"])
def get_student_by_uni(uni):

    result = ColumbiaStudentResource.get_by_key(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

