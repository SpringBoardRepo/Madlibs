from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route('/')
def ask_questions():
    questions = story.prompts
    return render_template('base.html', questions=questions)


@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('story.html', text=text)
