```python
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class PrankCallScript(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    script = db.Column(db.String(500), nullable=False)

def storePrankCallScript(script):
    new_script = PrankCallScript(script=script)
    db.session.add(new_script)
    db.session.commit()

@app.route('/store_script', methods=['POST'])
def handle_store_script_request():
    script = request.json.get('script')
    storePrankCallScript(script)
    return {"message": "Script stored successfully."}, 200

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```