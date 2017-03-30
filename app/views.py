from app import app
from models import *
from forms import *

@app.route('/')
def home():
    nform=nurseForm()
    return render_template('create_nurse.html',form=nform)
