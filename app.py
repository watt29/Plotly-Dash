import dash
from dash import dcc, html
import plotly.graph_objects as go

# สร้างแอป Dash
app = dash.Dash(__name__)

# ข้อมูลที่ใช้ในกราฟ
categories = ['อาหาร', 'ค่าเช่า', 'ค่าพลังงาน', 'ค่าสื่อสาร', 'บันเทิง']
expenses = [5000, 15000, 3000, 1500, 2000]

# สร้างกราฟแท่ง
fig = go.Figure(data=[go.Bar(x=categories, y=expenses)])

# กำหนด layout ของแอป
app.layout = html.Div(children=[
    html.H1('เปรียบเทียบค่าใช้จ่าย', style={'textAlign': 'center'}),
    dcc.Graph(
        id='expense-bar-chart',
        figure=fig
    ),
])

# รันแอปพลิเคชัน
if __name__ == '__main__':
    app.run_server(debug=True)
