from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story
from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/question')
def get_input_place():

    return render_template("questions.html",
                user_inputs = silly_story.prompts)

@app.get('/story')
def generate_story():
    """ generates story """

    result = silly_story.generate(request.args)

    return render_template('results.html',result = result)







