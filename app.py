from flask import Flask, render_template, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "super_secret_key_123"

facts = [
    "Осьминог имеет три сердца.",
    "Банан с точки зрения ботаники считается ягодой.",
    "У акул нет костей — их скелет состоит из хрящей.",
    "Пчёлы умеют передавать информацию с помощью танца.",
    "У жирафа очень длинный язык — до 45 сантиметров.",
    "Некоторые черепахи могут дышать не только лёгкими.",
    "Сердце синего кита может весить больше 100 килограммов.",
    "Муравьи могут переносить вес во много раз больше собственного.",
    "Кошки не чувствуют сладкий вкус так, как люди.",
    "У улитки могут быть тысячи маленьких зубов."
]


def get_random_fact():
    previous_fact = session.get("last_fact")
    available_facts = [fact for fact in facts if fact != previous_fact]

    if not available_facts:
        available_facts = facts

    fact = random.choice(available_facts)
    session["last_fact"] = fact
    return fact


@app.route("/")
def home():
    if "views" not in session:
        session["views"] = 1
    else:
        session["views"] += 1

    fact = get_random_fact()
    return render_template("index.html", fact=fact, views=session["views"])

@app.route("/api/fact")
def api_fact():
    if "views" not in session:
        session["views"] = 1
    else:
        session["views"] += 1

    fact = get_random_fact()

    return jsonify({
        "fact": fact,
        "views": session["views"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)