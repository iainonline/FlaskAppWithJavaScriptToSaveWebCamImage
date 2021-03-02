from flask import Flask, request, Response
import time

PATH_TO_TEST_IMAGES_DIR = 'venv'
app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./venv/Static/getImage.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))

    return Response("%s saved" % f)

if __name__ == '__main__':
    app.run(debug=True)