from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed, TEXT
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)
# docs = UploadSet('docs', TEXT)

app.config['UPLOADED_PHOTOS_DEST'] = 'pictures'
app.config['UPLOADED_PHOTOS_ALLOW'] = ['text', 'py']
# app.config['UPLOADED_PHOTOS_DENY'] = ['jpg']
# app.config['UPLOADED_PHOTOS_DEST'] = 'other'
app.config['UPLOADS_AUTOSERVE'] = True

configure_uploads(app, photos)
# configure_uploads(app, (photos, docs))

@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST' and 'thefile' in request.files:
        try:
            image_filename = photos.save(request.files['thefile'])
            # return '<h1>' + photos.path(image_filename) + '</h1>'
            return '<h1>' + photos.url(image_filename) + '</h1>'

        except UploadNotAllowed:
            return '<h1>File is not allowed!</h1>'
    return render_template('uploads.html')

if __name__ == '__main__':
    app.run(debug=True)
