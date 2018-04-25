from flask import Flask, render_template, url_for
import datetime
import numpy as np
import test_info
app = Flask(__name__)

app.debug = True

def lookup(find, pol):
    # if any(find in p for p in pol):
        # print('yes')
    matching = [s for s in pol if any(f in s for f in find.split(' '))]
    # print(matching)
    return [pol.index(s) for s in pol if any(f in s for f in find.split(' '))]

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
            'link':  '<iframe width="100%" src="https://www.youtube.com/embed/0on5LV3k26o?showinfo=0", frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is the maximum heart rate? What is the role of the heart?'
        }
    ]
    return render_template('inquiry.html', videos = videos)

@app.route('/chem/<year>/<question>')
def chem(year, question):
    return render_template(f'chem/{year}/{question}.html')

@app.route('/phys/<year>/<question>')
def phys(year, question):
    return render_template(f'phys/{year}/{question}.html')



# -----------------------------------------

@app.route('/search/<test>/<text>')
def search(test, text):
    if test == 'A11':
        t = 0
    elif test == 'A09':
        t = 1
    elif test == 'A05':
        t = 2
    elif test == 'A04':
        t = 3
    elif test == 'A03':
        t = 4
    elif test == 'A02':
        t = 5
    elif test == 'pA11':
        t = 6
    elif test == 'pA09':
        t = 7
    elif test == 'pA06':
        t = 8

    if test[0]=='p':
        te = test[1:]
    else:
        te = test

    info = test_info.TestInfo(t)
    l = np.unique(lookup(text, info.all()[t]['POL']))
    return render_template(f'zoom.html', test_info = info.all(), l=l, t=t, test=te)
    # this get the list l of found searched POL's and sends it to the page.


# ------------------------------------------

@app.route('/assessments/<test>')
def assessments(test):
    if test == 'A11':
        t = 0
    elif test == 'A09':
        t = 1
    elif test == 'A05':
        t = 2
    elif test == 'A04':
        t = 3
    elif test == 'A03':
        t = 4
    elif test == 'A02':
        t = 5
    elif test == 'pA11':
        t = 6
    elif test == 'pA09':
        t = 7
    elif test == 'pA06':
        t = 8
    info = test_info.TestInfo(t)

    # l = lookup('Solubility reactions', test_info[0]['POL'])
    return render_template(f'{test}.html', test_info = info.all())
    # this get the list l of found searched POL's and sends it to the page.



if __name__ == '__main__':
    app.run()
