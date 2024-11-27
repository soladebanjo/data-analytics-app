import sys
import os
from flask import Flask, render_template
import os
from src.analysis import run_analysis

# Explicitly set the template folder path
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

@app.route('/')
def index():
    results = run_analysis()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

print("Template folder:", app.template_folder)
