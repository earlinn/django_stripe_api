import os

from dotenv import load_dotenv

from .base import *

load_dotenv()

MODE = os.getenv("MODE", default="prod")

if MODE == "dev":
    from .dev import *
else:
    from .prod import *
