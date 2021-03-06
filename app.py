from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
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

def datetime(x):
    return np.array(x, dtype=np.datetime64)

@app.route('/graph', methods = ['POST'])
def graph():
    
    stock = request.form['stock']
    ytypes = request.form.getlist('tickerdetails')
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
    session = requests.Session()
    session.mount('http://',requests.adapters.HTTPAdapter(max_retries=3))
    resp_data = session.get(api_url)
    j = resp_data.json()
    df = pd.DataFrame(j["data"])
    df.columns = j["column_names"]
    
    x_list = pd.to_datetime(df["Date"])

       
    TOOLS = 'box_zoom,box_select,resize,reset,hover,wheel_zoom'
    p1 = figure(tools=TOOLS, title='Data from Quandl WIKI set',x_axis_type = "datetime")
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    
    colors=["firebrick", "navy", "Olive", "Pink"]
    i=0
    for item in ytypes:
        p1.line(x_list, df[item], color=colors[i], legend=stock+"-"+item)
        i=i+1
    
    script, div = components(p1)
    
    return render_template('graph.html', script=script, div=div)


    
if __name__ == '__main__':
  app.run(port=33507)
