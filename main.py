from cumulio.cumulio import Cumulio
from dotenv import load_dotenv
from flask import Flask
import os

app = Flask(__name__)


load_dotenv()

client = Cumulio(os.getenv('CUMUL_KEY'), os.getenv('CUMUL_TOKEN'), "https://api.cumul.io")

properties = {}
properties["integration_id"] = os.getenv('INTEGRATION_ID')
properties["type"] = "sso"
properties["expiry"] = "24 hours"
properties["inactivity_interval"] = "10 minutes"
properties["name"] = os.getenv('USER_NAME')
properties["email"] = os.getenv('USER_EMAIL')
properties["suborganization"] = "< user suborganization >"
properties["role"] = "viewer"


@app.route('/')
def hello_world():
  authorization = client.create("authorization", properties)
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()