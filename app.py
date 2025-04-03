from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/activity')
def activity():
    return render_template('activity.html')

@app.route('/publication/')
def publication():
    return render_template('publication.html')

@app.route('/publication/papers')
def papers():
    return render_template('papers.html')

@app.route('/publication/lectures')
def lectures():
    return render_template('lectures.html')

@app.route('/publication/presentations')
def presentations():
    return render_template('presentations.html')

@app.route('/publication/books')
def books():
    return render_template('books.html')

@app.route('/publication/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/activity/graduates')
def graduates():
    return render_template('graduates.html')
@app.route('/activity/history')
def history():
    return render_template('history.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/top')
def top():
    return render_template('index.html')  # index.htmlをテンプレートとして表示
if __name__ == '__main__':
    app.run(debug=True)