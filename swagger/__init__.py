from eve import Eve
import platform
import json
from default_controller import *

settings = {'MONGO_HOST': 'localhost', 'MONGO_PORT': 27017, 'DOMAIN': {}}

app = Eve()

@app.route('/get_records')

if __name__ == '__main__':
    app.run()
