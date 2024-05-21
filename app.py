from flask import Flask, request, send_file
from flask_cors import CORS
from models import db , create_files_list_model
import datetime
from sqlalchemy.exc import SQLAlchemyError

# Create a Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
CORS(app)



#Inserir um novo arquivo no banco de dados

def create_file_register(
    name,
    updated_by,
):
    current_time = datetime.datetime.now().isoformat()
    File_register = create_files_list_model()
    new_file_register = File_register(
        name= name,
        updated_by = updated_by,
        created_at=current_time,
        updated_at=current_time
    )
    try:
        db.session.add(new_file_register)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()  # Roll back the changes in case of an error
        error_message = f"An error occurred while adding the job: {str(e)}"
        # Handle the error, log it, or provide feedback to the user

        print(error_message)
        return False
    finally:
        print("\n \n Registro inserido")

        db.session.close()  # Always close the session when done
    return True



def filter_files(page, per_page):
    Files = create_files_list_model()

    # Construct the base query
    base_query = Files.query.filter()

    # Apply pagination
    paginated_files = base_query.paginate(page=page, per_page=per_page)
    files_records = paginated_files.items  # Get the records for the current page
    total_pages = paginated_files.pages

    # trunk-ignore(ruff/F821)
    file_dicts = [file.__dict__ for file in files_records]

    # Convert model instances to dictionaries
    serialized_files = []
    for file_dict in file_dicts:
        serialized_files.append(
            {key: value for key, value in file_dict.items() if not key.startswith("_")}
        )

    response_data = {
        "file_records": serialized_files,
        "total_pages": total_pages,
        "page": page,
    }

    return response_data

    # Se a url acessada tiver easy apply


# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World! :)'

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    print("Update by", request)
    if uploaded_file.filename != '':
        create_file_register(uploaded_file.filename, "Professor Carvalho")
        uploaded_file.save('uploads/' + uploaded_file.filename)
        return 'File uploaded successfully'

@app.route('/download/<filename>')
def download_file(filename):
    return send_file('uploads/' + filename, as_attachment=True)

@app.route('/file_list', methods=['GET'])
def get_file_list():
    filtered_files = filter_files(1,10)
    return filtered_files

# Run the application if this script is executed directly
if __name__ == '__main__':
    # trunk-ignore(bandit/B201)
    app.run(debug=True)


