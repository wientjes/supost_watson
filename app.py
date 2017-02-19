from flask import Flask, request, render_template
import supost_watson as watson
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_classification(): 
	image_url = request.form['url']
	result = watson.get_classification(image_url)
	return render_template('index.html',text=result)

if __name__ == "__main__":
    app.run(debug=True)