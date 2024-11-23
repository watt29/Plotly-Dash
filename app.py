import dash
from dash import dcc, html  # เปลี่ยนจาก dash_core_components และ dash_html_components
import plotly.express as px

# สร้างแอป Dash
app = dash.Dash(__name__)

# สร้างกราฟด้วย Plotly Express (กราฟเส้นเป็นตัวอย่าง)
fig = px.line(x=[1, 2, 3, 4], y=[10, 11, 12, 13], title="ตัวอย่างกราฟเส้น")

# เลย์เอาท์ของแอป
app.layout = html.Div(children=[
    html.H1("กราฟใน Dash"),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# รันแอป
if __name__ == '__main__':
    app.run_server(debug=True)
