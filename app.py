# Your code here
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df1 = pd.read_excel('premises-list-Aug-2022.xlsx', skiprows=[0, 1, 2])
df1['Licence type'] = df1['Licence type'].str.split(" - ").str.get(1)
df1['Licence type'] = df1['Licence type'].str.title()

# post_unique = df1['Postcode'].unique().tolist()
# list1 = (sorted(df1['Postcode'].dropna().unique()))
df_drop_option = pd.Series(df1['Postcode'].unique()).sort_values(ascending=True)

app.layout = html.Div([
    dcc.Dropdown(
        df_drop_option,
        # post_unique.sort(),
        multi=True,
        value=[],
        id='postcodes',
        placeholder = 'Select postcodes'
    ),
    dcc.Graph(
        id='graph'
    )
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='postcodes', component_property='value')
)
def dropdown_changed(postcode):
    if len(postcode) == 0:
        fig = px.histogram(
            df1,
            x='Licence type',
            y='EGMs',
            histfunc='avg',
            color_discrete_sequence=['#002664'],
            title='EGMs by Licence Type in NSW'
        )

        fig.update_layout(plot_bgcolor='#EAEDF4')
        fig.update_xaxes(title_text=None)
        fig.update_yaxes(title_text='Average EGMs')
        return fig
    else:
        # df2 = df1.query('Postcode in @postcode')
        df2 = df1[df1['Postcode'].isin(postcode)]

        fig = px.histogram(
            df2,
            x='Licence type',
            y='EGMs',
            histfunc='avg',
            # color_discrete_sequence=['#002664'],
            color='Postcode',
            labels={'Postcode': 'Postcode'},
            title='EGMs by Licence Type in NSW',
            barmode='group'
        )

        fig.update_layout(plot_bgcolor='#EAEDF4')
        fig.update_xaxes(title_text=None)
        fig.update_yaxes(title_text='Average EGMs')
        return fig


app.title = 'EGMs in NSW'

if __name__ == '__main__':
    app.run_server(debug=True)
