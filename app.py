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
    stock = request.POST['stock']
    print stock
    return render_template('graph.html')
"""
    #plttype = request.form.tickerdetails
    resp_data = getdata(stock)
    df = getdf(resp_data)
    df.plot = figure(tools=TOOLS,
	      title='Data from Quandl WIKI set',
	      x_axis_label='date',
	      x_axis_type='datetime')

     script, div = components(plot)

     return render_template('graph.html', script=script, div=div)
    

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
  app.run(port=33507)
