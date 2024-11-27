from flask import Flask, render_template
import analysis

app = Flask(__name__)

@app.route('/')
def index():
    results = analysis.run_analysis()
    
    # Handle errors in results
    if 'error' in results:
        return f"<h1>Error: {results['error']}</h1>"
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
