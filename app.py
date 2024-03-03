from roboflow import Roboflow
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    rf = Roboflow(api_key="rf_f15BJEWAwWfdLgpt85YBpvWNAkP2")
    project = rf.workspace().project("hardhatsample/3")
    model = project.version(3).model
    output = model.predict("1.jpeg", confidence=50, overlap=50).json()
    return output