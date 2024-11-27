import os
from flask import Flask, render_template
import analysis

# Explicitly set the template folder
app = Flask(__name__, template_folder='/app/templates')

@app.route('/')
def index():
    results = analysis.run_analysis()
    if 'error' in results:
        return f"<h1>Error: {results['error']}</h1>"
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


