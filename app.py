from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, render_template_string
from hack.frontend import Frontend
from hack.constants import LANG
from wtforms import SelectField
import os
import numpy as np
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ubuntu/pytorch-hackathon/data'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

fe = Frontend()

app = Flask(__name__)
app.secret_key = 'some secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SESSION_TYPE'] = 'filesystem'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filestr = file.read()
            #lang = SelectField('Language', choices=LANG, default=1)
            lang = request.form.get('lang')
            npimg = np.fromstring(filestr, np.uint8)
            translated_sentence, wav_audio = None, None
            if 'text' in request.form:
                translated_sentence = fe.get_caption(npimg, lang)
            elif 'speech' in request.form:
                wav_audio = fe.get_speech(npimg, lang)
            else:
                translated_sentence, wav_audio = fe.get_speech_and_caption(npimg, lang)
            #flash(translated_sentence)
            return render_template_string('{{ x }}', x=str(translated_sentence))
            #return render_template('success.html', translated_sentence=translated_sentence)
            #return redirect(url_for('uploaded_file', filename=filename))
    return render_template('basic.html', LANG=LANG)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/get_previous_caption')
def get_previous_caption():
    return fe.get_previous_caption()

#@app.route('/')
#def hello_world():
#    fe = Frontend()
#    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
