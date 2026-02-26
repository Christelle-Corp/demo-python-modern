"""
Demo Python Application - GHAS Security Testing

WARNING: This application contains intentionally vulnerable dependencies.
Do not deploy to production!
"""

from flask import Flask, jsonify
import requests
import yaml
import jinja2

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'warning': 'This is a demo app with intentionally vulnerable dependencies'
    })

@app.route('/')
def home():
    return """
    <h1>Demo Python Application</h1>
    <p><strong>⚠️ WARNING:</strong> This application contains intentionally vulnerable dependencies.</p>
    <p>Endpoints:</p>
    <ul>
        <li><a href="/health">/health</a> - Health check</li>
    </ul>
    """

if __name__ == '__main__':
    print("Demo Python App - GHAS Security Testing")
    print("WARNING: This application contains intentionally vulnerable dependencies")
    print("Do not deploy to production!")
    app.run(debug=True, host='0.0.0.0', port=5000)
