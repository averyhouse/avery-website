from .app import app, constitution_hook
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events/')
def events():
    return render_template('events.html')

@app.route('/constitution/')
def constitution():
    return render_template('constitution.html')

@app.route('/constitution/update', methods=["GET", "POST"])
def constitution_update():
    constitution_hook()
    return redirect(url_for('constitution'))

@app.route('/rotation_video/')
def rotation_video():
    return render_template('rotation_video.html')

@app.route('/valentine_video/')
def valentines_video():
    return render_template('valentines_video.html')

@app.errorhandler(404)
def page_not_found(err):
    return 'This route does not exist {}'.format(request.url), 404
