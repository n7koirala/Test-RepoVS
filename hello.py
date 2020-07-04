import math
import sys
from os import rename

import requests


r = requests.get("https://google.com")
print(r.status_code)

