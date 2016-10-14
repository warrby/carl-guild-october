from flask import request, Flask, jsonify
from flask_testing import TestCase
from Task import Task
import uuid

app = Flask(__name__)
tasks = {}

def create_task(data):
    t = Task(uuid.uuid4(), data["title"], data["desc"], data["done"])
    print('\nTask Added:\n id: %s,\n title: %s,\n desc: %s,\n done: %s\n' % (t.id, t.title, t.desc, t.done))
    return (str(t.id), t)

def update_task(data):
    if(data["id"] in tasks):
        t = Task(data["id"], data["title"], data["desc"], data["done"])
        tasks.update({t.id:t})
        print('\nTask Updated:\n id: %s,\n title: %s,\n desc: %s,\n done: %s\n' % (t.id, t.title, t.desc, t.done))

@app.route('/')
def index():
    return "Tasks API!"

@app.route('/api')
@app.route('/api/getTasks')
def get_tasks():
    for key, value in tasks.iteritems():
        print('\nTask:\n id: %s,\n title: %s,\n desc: %s,\n done: %s\n' % (value.id, value.title, value.desc, value.done))
    return jsonify(tasks=[e.serialize() for (i,e) in tasks.iteritems()])

@app.route('/api/removeTask', methods=['POST'])
def remove_tasks():
    _id = request.get_json()["id"]
    if _id in tasks:
        del tasks[_id]
    return jsonify(tasks=[e.serialize() for (i,e) in tasks.iteritems()])

@app.route('/api/addTask', methods=['POST'])
def add_task():
    (_id, _user) = create_task(request.get_json())
    tasks.update({_id:_user})
    return jsonify(tasks=[e.serialize() for (i,e) in tasks.iteritems()])

@app.route('/api/updateTask', methods=['POST'])
def update_single_task():
    json = request.get_json()
    update_task(json)
    return jsonify(tasks=[e.serialize() for (i,e) in tasks.iteritems()])


if __name__ == '__main__':
    app.run(debug=True, port=88)
