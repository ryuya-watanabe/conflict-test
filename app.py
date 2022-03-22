from flask import Flask, render_template

app = Flask( _name_ )

@app.route("/")
def top_page():
    return render_template("index.html")

    if _name_ == "_main_":
        app.run(dobug=True)

from flask import Flask, render_template, request

@app.route("/circle_input")
def circle_result():
    return render_template("circle_input.html")

@add.route("circle_result")
def circle_result():
    radius = int(request.args.get("radius"))
    result = 3.14 * radius ** 2
    return render_template("circle_result.html", result=result)
