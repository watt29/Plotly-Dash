import dash
from dash import dcc, html  # ใช้การนำเข้าจาก dash โดยตรง
import plotly.express as px

# สร้างกราฟตัวอย่าง
fig = px.bar(x=["A", "B", "C"], y=[10, 20, 30], labels={"x": "Category", "y": "Value"})

# สร้างแอป Dash
app = dash.Dash(__name__)

# สร้างฟังก์ชัน navbar (ตัวอย่างง่าย ๆ)
def create_navbar():
    return html.Nav([
        html.Ul([
            html.Li(html.A("Home", href="#")),
            html.Li(html.A("About", href="#")),
            html.Li(html.A("Contact", href="#")),
        ], className="navbar")
    ])

# กำหนด layout ของแอป
app.layout = html.Div([
    create_navbar(),  # เพิ่ม Navbar
    dcc.Graph(figure=fig)  # แสดงกราฟ
])

# รันแอป
if __name__ == '__main__':
    app.run_server(debug=True)
