from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('working_ajax.html')


@app.route('/add', methods=['POST'])
def add():
    a = request.form.get('a', 0, type=float)
    b = request.form.get('b', 0, type=float)
    print(a+b)
    #return jsonify(result=a + b) # ooh, just change a div?!
    return render_template('working_ajax.html') # another option: leave the page alone.


if __name__ == '__main__':
	app.run(debug=True)


