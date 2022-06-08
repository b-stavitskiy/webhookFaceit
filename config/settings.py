import os, dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
dotenv.load_dotenv(dotenv_path)

FACEIT_API_KEY = os.environ.get('FACEIT_API_KEY')
