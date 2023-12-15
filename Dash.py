import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pyngrok import ngrok

# Загрузка данных из файлов CSV
df_computers = pd.read_csv('Data.csv')
df_vr = pd.read_csv('VR.csv')

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Определение макета дашборда
app.layout = html.Div([
    html.H1("Активность устройств за 22.12.2023"),

    html.Div([
        dcc.Graph(id='computers-activity-bar'),
        dcc.Graph(id='computers-activity-pie'),
        dcc.Graph(id='vr-activity-bar'),
        dcc.Graph(id='vr-activity-pie'),
        dcc.Graph(id='comparison-pie'),
    ]),
])


# Определение обработчиков событий и функций для обновления графиков
@app.callback(
    [Output('computers-activity-bar', 'figure'),
     Output('computers-activity-pie', 'figure'),
     Output('vr-activity-bar', 'figure'),
     Output('vr-activity-pie', 'figure'),
     Output('comparison-pie', 'figure')],
    [Input('computers-activity-bar', 'value')]
)
def update_graph(selected_computer):
    # График активности для компьютеров (столбчатая диаграмма)
    computers_activity_bar_fig = px.bar(df_computers,
                                        x='Устройство', y='Активность',
                                        title='Активность компьютеров')

    # График активности для компьютеров (круговая диаграмма)
    computers_activity_pie_fig = go.Figure(data=[go.Pie(labels=df_computers['Устройство'],
                                                        values=df_computers['Активность'],
                                                        title='Активность компьютеров')])

    # График активности для VR (столбчатая диаграмма)
    vr_activity_bar_fig = px.bar(df_vr,
                                 x='Устройство', y='Активность',
                                 title='Активность VR')

    # График активности для VR (круговая диаграмма)
    vr_activity_pie_fig = go.Figure(data=[go.Pie(labels=df_vr['Устройство'],
                                                 values=df_vr['Активность'],
                                                 title='Активность VR')])

    # График сравнения активности компьютеров и VR (круговая диаграмма)
    comparison_pie_fig = go.Figure(data=[go.Pie(labels=['Компьютеры', 'VR'],
                                                values=[df_computers['Активность'].sum(), df_vr['Активность'].sum()],
                                                title='Сравнение активности компьютеров и VR')])

    return computers_activity_bar_fig, computers_activity_pie_fig, vr_activity_bar_fig, vr_activity_pie_fig, comparison_pie_fig


# Запуск веб-приложения
if __name__ == '__main__':
    app.run_server(debug=True)
