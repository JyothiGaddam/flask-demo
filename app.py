from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/graph', methods = ['POST'])
def graph():
  print(request.form.get('stock',none))
  print( request.form.get('tickerdetails',None),"checked")
  return render_template('graph.html')


if __name__ == '__main__':
  app.run(port=33507)
