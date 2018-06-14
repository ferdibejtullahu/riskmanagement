# Run a test server.
import os
from app import app

if os.environ.get('FLASK_PRODUCTION'):
    app.run(host='0.0.0.0')
else:
    if __name__ == '__main__':
        app.run()
