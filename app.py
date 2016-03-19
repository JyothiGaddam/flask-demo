from flask import Flask, render_template, request, redirect
import pandas as pd
from bokeh.plotting import figure
import jinja2
from bokeh.embed import components
import requests

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/analysis',methods = ['POST'])
def analysis():
    stock = request.form['stock']
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
    session = requests.Session()
    session.mount('http://',requests.adapters.HTTPAdapter(max_retries=3))
    resp_data = session.get(api_url)
    #resp_data = getdata(stock)
    j = resp_data.json()
    df = pd.DataFrame(j["data"])
    df.columns = j["column_names"]
    return render_template("analysis.html", name=stock, data=x.to_html())
                                                                # ^^^^^^^^^


"""
@app.route('/graph', methods = ['POST'])
def graph():
    
    stock = request.form['stock']
    #print stock
    #plttype = request.form.tickerdetails
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
    session = requests.Session()
    session.mount('http://',requests.adapters.HTTPAdapter(max_retries=3))
    resp_data = session.get(api_url)
    #resp_data = getdata(stock)
    j = resp_data.json()
    df = pd.DataFrame(j["data"])
    df.columns = j["column_names"]
    
    
    
    p = figure(title='Data from Quandl WIKI set',x_axis_type='datetime')
    p.line(df['Date'],df['Close'], color='#A6CEE3', legend='stock')
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Price' 
    p.legend.orientation = "top_left"
    script, div = components(p)
    
    return render_template('graph.html')
    

def getdata(stock):
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
    session = re.Session()
    session.mount('http://',re.adapters.HTTPAdapter(max_retries=3))
    raw_data = session.get(api_url)
    return raw_data

def getdf(resp_data):
     j = resp_data.json()
     df = pd.DataFrame(j["data"])
     df.columns = j["column_names"]
     return df   
"""     
if __name__ == '__main__':
  app.run(port=33507,debug=True)
