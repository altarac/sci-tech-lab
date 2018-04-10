from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inquiry')
def inquiry():
    videos = [
        {
            'title': 'LHC',
            'link': '<iframe width="100%" src="https://www.youtube.com/embed/qXWWgZ-nnEs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
        },
        {
            'title': 'Quantum mechanics',
            'link':  '<iframe width="100%" src="https://www.youtube.com/embed/qO_W70VegbQ?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
        }
    ]
    return render_template('inquiry.html', videos = videos)

if __name__ == '__main__':
    app.run(debug = True)
