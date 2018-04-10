from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inquiry')
def inquiry():
    videos = [
        {
            'title': 'LHC',
            'link': '<iframe width="100%" src="https://www.youtube.com/embed/qXWWgZ-nnEs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is the LHC? What questions arose from this experiment?'
        },
        {
            'title': 'Quantum mechanics',
            'link':  '<iframe width="100%" src="https://www.youtube.com/embed/qO_W70VegbQ?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is quantum mechanics? Who thought of this first?'
        },
        {
            'title': 'Maximum heart rate',
            'link':  '<iframe width="100%"" src="https://www.youtube.com/embed/0on5LV3k26o?showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is the maximum heart rate? What is the role of the heart?'
        }
    ]
    return render_template('inquiry.html', videos = videos)



@app.route('/assessments')
def assessments():
    return render_template('assessments.html')



if __name__ == '__main__':
    app.run(debug = True)
