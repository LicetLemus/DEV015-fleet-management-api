# define the configuration of the app, including the database URL

from dotenv import load_dotenv
import os # for os.environ is used to access the environment variables

load_dotenv()

database_url = os.getenv("DATABASE_URL")

# use the database_url variable to connect to the database not the DATABASE_URL variable with the value