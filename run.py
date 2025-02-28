import os
from app import create_app  # ✅ Import from the app package

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port, debug=False)
