from koyeb import Sandbox
import os
from dotenv import load_dotenv

load_dotenv()

sandbox = Sandbox.create(
    image="ubuntu",
    name="hello-world",
    wait_ready=True,
    api_token=os.getenv("KOYEB_API_TOKEN")
)

result = sandbox.exec('ls')
print(result.stdout.strip())