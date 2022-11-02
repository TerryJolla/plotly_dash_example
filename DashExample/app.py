import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

def tiaoxing():
    return html.Div([
        html.P([]),
    dcc.Graph(
    id='tx',
        figure={
            'data':[
                {'x':[4,6,8],'y':[12,16,18],'type':'bar','name':'chart one'},
                {'x':[4,6,8],'y':[20,24,28],'type':'bar','name':'chart two'}
            ],
            'layout':{
                'title':'simple bar chart',
            }
        }
    )
],className='tiaoxing')

def zhexiantu():
    return html.Div([
        html.P([]),
        dcc.Graph(
            id='xtq',
            figure={
                'data':[
                    {'x':[1,2,3,4,5,6,7,8,9,10,11],'y':[5,8,11,32,41,5,2,7,16,4,8],'type':'Scatter','name':'one'},
                    {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'y': [5,6,3,7,1,5,48,2,3,58,4,],'type': 'Scatter', 'name': 'two'}
                ],
                'layout':{
                    'title':'折线图'

                }
            }
        )
    ],className='zhexiantu')
a=16
def bink():
    return html.Div([
        html.P([]),
        dcc.Graph(
            id='btk',
            figure={
                'data': [
                    {'labels': ['one', 'two', 'three', 'four', 'five', 'six'],
                     'values': [50, 34, 86, 75, 64, 39], 'type': 'pie', 'hole': '0.8', 'name': '饼图', 'size': '100'}
                ],
                'layout': {'title':'bingtu1'}
            }
        )
    ], className='bintuk')

def sandiantu():
    import numpy as np
    b = np.random.uniform(1, 3, size=300)
    c = 0.5 * b ** 2 + b + 2 + np.random.normal(0, 1, size=300)
    return html.Div([
        html.P([]),
        dcc.Graph(
            id='sdt',
            figure={
                'data':[
                    {'x':b,'y':c,'type':'Scatter','mode':'markers','name':"散点图"}
                ],
                'layout':{
                    'title':'sandian'
                }
            }
        )
    ],className='sandiantu')
def bintu():
    return html.Div([
        html.P([]),
        dcc.Graph(
            id='bt',
            figure={
                'data':[
                    {'labels':['one', 'two', 'three', 'four', 'five', 'six'],'values':[280, 25, 10, 100, 250, 270],'type':'pie','name':'bingtu','size':'100'}
                ],
                'layout':{'title':'bingtu'}
            }
        )
    ],className='bintu')
def row1():
    return html.Div([
        tiaoxing(),
        bink(),
        sandiantu()
    ], className='row')
def row2():
    return html.Div([
            zhexiantu(),
            bintu()
    ],className='row')
def row3():
    return html.Div([
        row1(),
        row2()
    ],className='di')
app.layout=html.Div([
    html.H1(["交互式电子信息可视化"],style={'margin':'2% auto','color':'white'}),
    row3(),
],className='card')

if __name__ =='__main__':
    app.run_server(port=4050)