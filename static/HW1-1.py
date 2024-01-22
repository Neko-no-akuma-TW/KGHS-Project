from flask import Flask

app = Flask(__name__)


@app.route('/')
def t9():
    html = "<table border>\n"
    for i in range(1, 10):
        html += "<tr>"
        for j in range(1, 10):
            if (i + j) % 2 == 0:
                html += f'<td style="background-color: pink;">{i} * {j} = {i*j}</td>'
            else:
                html += f"<td>{i} * {j} = {i*j}</td>"
        html += "</tr>\n"
    html += "</table>\n"
    return html
