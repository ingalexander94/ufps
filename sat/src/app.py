from flask import Flask
from flask_cors import CORS
from util import environment
from routes.student_router import student_rest
from routes.teacher_router import teacher_rest

app = Flask(__name__)
CORS(app)  
app.config["SECRET_KEY"] = environment.SECRET_KEY

# Routes
app.register_blueprint(student_rest, url_prefix='/student')
app.register_blueprint(teacher_rest, url_prefix='/teacher')

@app.route('/') 
def ping():
    return f"Hola, {environment.PING}"

if __name__ == '__main__':
    app.run(debug=True, port=environment.PORT, host='0.0.0.0')