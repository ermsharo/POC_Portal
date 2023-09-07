from flask import Flask, request, send_file
from flask_cors import CORS 

# Create a Flask application
app = Flask(__name__)
CORS(app)


# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World! :)'

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('uploads/' + uploaded_file.filename)
        return 'File uploaded successfully'

@app.route('/download/<filename>')
def download_file(filename):
    return send_file('uploads/' + filename, as_attachment=True)


# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)


