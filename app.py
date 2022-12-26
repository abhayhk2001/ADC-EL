from flask import Flask
from py_minIO import run_data_process 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/run')
def run():
	run_data_process()
	return 'Process Completed'
    

if __name__ == '__main__':
    app.run()