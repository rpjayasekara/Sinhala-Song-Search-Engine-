from flask import Flask, request, render_template
from search_engine import _search


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    hits = _search(search_query=query)
    num = len(hits)
    print(len(hits))
    return render_template('results.html',query=query,hits=hits,num_results=num)

if __name__ == "__main__":
    app.run(debug=True)