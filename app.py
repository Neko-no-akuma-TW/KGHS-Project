from flask import Flask, render_template, session, redirect, url_for, request
import json
from datetime import datetime

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
app.config["SECRET_KEY"] = "KGHS2024-7"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template("logged.html", error=error)
    return render_template('logged.html')

@app.route('/logout')
def logout():
    session.pop('logged_in')
    return redirect(url_for('index'))

@app.route('/selected', methods=['POST'])
def selected():
    role = request.form['identity']
    if role == "buyer":
        return render_template('buyer.html')
    else:
        return render_template('seller.html')

@app.route('/seller_dealed')
def seller_dealed():
    with open("seller_deal_log.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
    times = []
    prices = []
    for i in data:
        times.append(i.split(",")[0])
        prices.append(i.split(",")[1])
    return render_template('seller_dealed.html', times=times, prices=prices)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/seller_can_deal')
def seller_can_deal():
    with open("data.json") as f:
        data = json.load(f)
    return render_template('seller_can_deal.html', data=data)

@app.route('/seller_deal', methods=['GET', 'POST'])
def seller_deal():
    if request.method == "GET":
        return render_template('seller_deal.html')
    else:
        file = request.files['own']
        file.save(f'static/{file.filename}')
        return render_template('seller_num_choose.html')

@app.route('/seller_choosed', methods=['POST'])
def seller_choosed():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    data["seller_can_deal"] += int(request.form["num"])
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    with open("seller_deal_log.txt", "a", encoding="utf-8") as f:
        f.write(str(datetime.now()) + "," + request.form["num"] + "\n")
    return render_template('seller_choosed.html')

@app.route('/contact_leave', methods=['POST'])
def contact_leave():
    with open("contact.txt", "a", encoding="utf-8") as f:
        f.write(request.form["email"] + "\n")
    return render_template('contact_leave.html')

@app.route('/buyer_dealed')
def buyer_dealed():
    with open("buyer_deal_log.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
    times = []
    prices = []
    for i in data:
        times.append(i.split(",")[0])
        prices.append(i.split(",")[1])
    return render_template('buyer_dealed_record.html', times=times, prices=prices)

@app.route('/buyer_can_deal')
def buyer_can_deal():
    with open("data.json") as f:
        data = json.load(f)
    return render_template('buyer_dealed.html', data=data)

@app.route('/buyer_deal', methods=['GET', 'POST'])
def buyer_deal():
    return render_template('buyer_num_choose.html')

@app.route('/buyer_choosed', methods=['POST'])
def buyer_choosed():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    data["buyer_buyed"] += int(request.form["num"])
    data["seller_can_deal"] -= int(request.form["num"])
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    with open("buyer_deal_log.txt", "a", encoding="utf-8") as f:
        f.write(str(datetime.now()) + "," + request.form["num"] + "\n")
    with open("seller_deal_log.txt", "a", encoding="utf-8") as f:
        f.write(str(datetime.now()) + ",-" + request.form["num"] + "\n")
    return render_template('buyer_choosed.html')

if __name__ == '__main__':
    app.run(host="192.168.1.78", debug=True)
