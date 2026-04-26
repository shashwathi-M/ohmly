from flask import Flask, render_template

# The '.' tells Flask to look for HTML files in the main folder, not a 'templates' folder
app = Flask(__name__, template_folder='.')

@app.route('/')
def input_page():
    return render_template('input.html')

@app.route('/loading.html')
def loading_page():
    return render_template('loading.html')

@app.route('/overview.html')
def overview_page():
    return render_template('overview.html')

@app.route('/insights.html')
def insights_page():
    return render_template('insights.html')

@app.route('/actions.html')
def actions_page():
    return render_template('actions.html')

@app.route('/report.html')
def report_page():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)