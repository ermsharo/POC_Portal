from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Criando o modelo de empregos aqui
def create_files_list_model():
    FILES = db.Table('FILES', db.metadata, autoload=True, autoload_with=db.engine)

    class Files_list(db.Model):
        __table__ = FILES

        # Define any additional columns or methods here

    return Files_list
