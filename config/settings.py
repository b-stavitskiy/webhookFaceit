import os, dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
dotenv.load_dotenv(dotenv_path)

FACEIT_API_KEY = os.environ.get('FACEIT_API_KEY')
FACEIT_OWNER_KEY = os.environ.get('FACEIT_OWNER_KEY')
FACEIT_ENDPOINT_URL = os.environ.get('FACEIT_ENDPOINT_URL')

FACEIT_APP_ID = os.environ.get('FACEIT_APP_ID')
FACEIT_WEBHOOK_ID = os.environ.get('FACEIT_WEBHOOK_ID')
FACEIT_WEBHOOK_NAME = os.environ.get('FACEIT_WEBHOOK_NAME')
FACEIT_WEBHOOK_URL = os.environ.get('FACEIT_WEBHOOK_URL')
