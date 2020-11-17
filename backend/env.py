import os
from dotenv import load_dotenv

env_folder = os.path.normpath(os.getcwd() + os.sep + os.pardir)
env = load_dotenv(os.path.join(env_folder, ".env"))