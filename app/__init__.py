from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']           = os.environ.get('SECRET_KEY', 'cv-analyzer-secret-2024')
    app.config['MAX_CONTENT_LENGTH']   = int(os.environ.get('MAX_FILE_SIZE_MB', 5)) * 1024 * 1024
    app.config['UPLOAD_FOLDER']        = os.path.join(app.root_path, 'uploads')
    app.config['GEMINI_API_KEY']       = os.environ.get('GEMINI_API_KEY', '')
    app.config['ALLOWED_EXTENSIONS']   = {'pdf', 'docx', 'png', 'jpg', 'jpeg'}

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    CORS(app)

    from app.routes.main     import main_bp
    from app.routes.analyze  import analyze_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(analyze_bp, url_prefix='/api')

    return app
