from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story
from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/question')
def get_input_place():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_nouns = request.args.get("plural_noun")


    return render_template("results.html",
                place=place,
                noun = noun,
                verb = verb,
                adjective = adjective,
                plural_nouns = plural_nouns)





