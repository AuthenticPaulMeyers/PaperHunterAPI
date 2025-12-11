
# This module handles file uploads to Supabase storage
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(override=True)

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt'}

# Load Supabase connection variables
SUPABASE_URL=os.getenv('SUPABASE_URL')
SUPABASE_KEY=os.getenv('SUPABASE_KEY')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Check allowed file types and return the file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload image function
def upload_files_to_supabase(file):

    bucket_name = 'files'
    folder_in_bucket = 'papers'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path_in_bucket = f"{folder_in_bucket}/{filename}"
        file_bytes = file.read()
        response = supabase.storage.from_(bucket_name).upload(
            file_path_in_bucket,
            file_bytes,
            {'content-type': file.content_type}
        )

        file_url = f"{SUPABASE_URL}/storage/v1/object/public/{response.fullPath}"

        return file_url
    else:
        return None


