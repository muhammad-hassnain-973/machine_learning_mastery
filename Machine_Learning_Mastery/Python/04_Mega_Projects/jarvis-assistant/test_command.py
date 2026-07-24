# test_command.py (temporary file, project root)
from dotenv import load_dotenv
load_dotenv()
from engine.command import process_command

result = process_command("news")
print(result)