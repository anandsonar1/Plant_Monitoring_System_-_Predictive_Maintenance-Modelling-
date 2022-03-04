from application import app
from flask import render_template, url_for, request ,session, redirect ,g, Flask
import pandas as pd 
import json
import plotly
import plotly.express as px
import os

rootpath=os.getcwd()
print(rootpath)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='abhi', password='abhi'))
users.append(User(id=2, username='pratik', password='pratik'))
users.append(User(id=3, username='rohit', password='rohit'))
users.append(User(id=3, username='anand', password='anand'))
app.secret_key = 'evendeadiamthehero'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']] 
        g.user = user

@app.route('/', methods=['GET','POST'])
def login():
    if request.method =='POST':
        session.pop('user_id', None)
        username= request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username==username] [0]
        
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('index'))
        return redirect(url_for('/'))
    
    return render_template('login.html')

@app.route("/index")
def index():
    if not g.user:
        return redirect(url_for('/'))
        
#graph 1 
    #df = pd.read_csv('D:/Canspirit AI/Data set/PdM_machines.csv')
    df=pd.read_csv(os.path.join(rootpath,"application/static/PdM_machines.csv"))
    fig1 = px.scatter(df, x='machineID', y='model', color='age',title='Machine Age') 
    fig1.update_traces(mode='markers+lines')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

#graph 2
    #df = pd.read_csv('D:/Canspirit AI/Data set/PdM_failures.csv')
    df=pd.read_csv(os.path.join(rootpath,"application/static/PdM_failures.csv"))
    fig2 = px.scatter(df, x = 'datetime', y = 'machineID', color='failure' ,title='Failures')
    #fig2 = px.box(df, x = 'failure', y = 'machineID' )
    #fig2.update_traces(quartilemethod="inclusive")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

#graph 3
    #df = pd.read_csv('D:/Canspirit AI/Data set/PdM_errors.csv')
    df=pd.read_csv(os.path.join(rootpath,"application/static/PdM_errors.csv"))
    fig3 = px.scatter(df, x="datetime", y="machineID",color='errorID',title='Errors')
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

#graph 4
    #df = pd.read_csv('D:/Canspirit AI/Data set/PdM_maint.csv')
    df=pd.read_csv(os.path.join(rootpath,"application/static/PdM_maint.csv"))
    fig4 = px.scatter(df, x='datetime', y='machineID', color='comp',title='Maintenance')
    #fig4.update_traces(mode='markers+lines')
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

# #graph 5
#     df = pd.read_csv('D:/Canspirit AI/Data set/PdM_telemetry.csv')
#     fig5 = px.box(df, x='machineID', y='volt', title='Voltage')
#     # fig5.update_traces(mode='markers+lines')
#     graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

# #graph 6
#     df = pd.read_csv('D:/Canspirit AI/Data set/PdM_telemetry.csv')
#     fig6 = px.line(df, x='machineID', y='rotate', title='Rotation')
#     #fig6.update_traces(mode='markers+lines')
#     graph6JSON = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

# #graph 7
#     df = pd.read_csv('D:/Canspirit AI/Data set/PdM_telemetry.csv')
#     fig7 = px.box(df, x='machineID', y='pressure', title='Pressure')
#     # fig7.update_traces(mode='markers+lines')
#     graph7JSON = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)

# #graph 8
#     df = pd.read_csv('D:/Canspirit AI/Data set/PdM_telemetry.csv')
#     fig8 = px.scatter(df, x='datetime', y='machineID', color='vibration',title='Vibration')
#     # fig8.update_traces(mode='markers+lines')
#     graph8JSON = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)
#return render_template('index.html', graph1JSON = graph1JSON , graph2JSON = graph2JSON, graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON, graph6JSON=graph6JSON, graph7JSON=graph7JSON, graph8JSON=graph8JSON )


    return render_template('index.html', graph1JSON = graph1JSON , graph2JSON = graph2JSON, graph3JSON=graph3JSON, graph4JSON=graph4JSON )