import os
import uuid
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.utils.extractor import extract_text
from app.utils.gemini    import analyze_resume

analyze_bp = Blueprint('analyze', __name__)

ALLOWED = {'pdf', 'docx', 'png', 'jpg', 'jpeg'}

def _allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED


@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file uploaded'}), 400

    file = request.files['resume']
    jd   = request.form.get('job_description', '')

    if not file.filename or not _allowed(file.filename):
        return jsonify({'error': 'Invalid file type. Upload PDF, DOCX, PNG, or JPG'}), 415

    api_key = current_app.config.get('GEMINI_API_KEY', '')
    if not api_key:
        return jsonify({'error': 'Gemini API key not configured. Add GEMINI_API_KEY to .env'}), 500

    # Save temp file
    fname  = str(uuid.uuid4()) + '_' + secure_filename(file.filename)
    fpath  = os.path.join(current_app.config['UPLOAD_FOLDER'], fname)
    file.save(fpath)

    try:
        text   = extract_text(fpath)
        result = analyze_resume(api_key, text, jd)
    finally:
        if os.path.exists(fpath):
            os.remove(fpath)   # clean up immediately

    return jsonify(result), 200


@analyze_bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'app': 'AI Resume Analyzer'}), 200
