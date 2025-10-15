from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route 1
@app.route('/')
def index():
    return render_template('index.html')

# Route 2
@app.route('/profile', methods=['POST'])
def build_profile():
    if request.method == 'POST':
        profile_info = {
            'fname': request.form.get('fname'),
            'lname': request.form.get('lname'),
            'sex': request.form.get('sex'),
            'status': request.form.get('status'),
            'loc': request.form.get('loc')
        }

        return render_template('profile.html', profile = profile_info)

if __name__ == '__main__':
    app.run(debug=True)
