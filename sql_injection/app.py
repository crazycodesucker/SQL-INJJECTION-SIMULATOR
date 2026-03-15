from flask import Flask, render_template, request, redirect
from database import login_secure, login_unsecure
app = Flask(__name__)

@app.route("/")
def home():
    error = request.args.get("error")
    return render_template("index.html", error=error)

@app.route("/login.html", methods=["GET", "POST"] )
def login():
    if request.method == "POST":
        username = request.form["username"] 
        password = request.form["password"]
        protection = request.form.get("protection")

        if protection:
            result = login_secure(username, password)
        else:
            result = login_unsecure(username, password)
            
        if result:
            return render_template("login.html")
        else:
            return redirect("/?error=INVALID CREDENTIALS")
    return redirect("/")    
    







if __name__ == "__main__":
    app.run(debug=True)