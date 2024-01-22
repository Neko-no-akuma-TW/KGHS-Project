from flask import Flask, request

app = Flask(__name__)


@app.route('/sampling', methods=["GET", "POST"])
def random_select():
    if request.method == 'GET':
        return """
        <form method="POST">
        學生名單
        <textarea name="students" rows="7" cols="50"></textarea></br>
        選取人數
        <select name="nums">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
        </select>
        <input type="submit">
        <input type="reset">
        </form>
        """
    else:
        import random
        students = request.values["students"].split("\r\n")
        num = int(request.values["nums"])
        a = random.sample(students, num)
        a.sort()
        html = "本次選到的有：<ol>\n"
        for line in a:
            html += "<li>" + line + "</li>\n"
        return html
