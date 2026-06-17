from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

ENDPOINT_URL = os.getenv("ENDPOINT_URL")
API_KEY = os.getenv("API_KEY")
print("KEY:", API_KEY[:10])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Obavezna polja
    age = int(request.form["age"])
    studytime = int(request.form["studytime"])
    failures = int(request.form["failures"])
    absences = int(request.form["absences"])

    # Opcionalna polja
    sex = request.form.get("sex") or "F"

    Medu = request.form.get("Medu")
    Medu = int(Medu) if Medu else 4

    Fedu = request.form.get("Fedu")
    Fedu = int(Fedu) if Fedu else 4

    internet = request.form.get("internet") or "yes"

    Walc = request.form.get("Walc")
    Walc = int(Walc) if Walc else 1

    payload = {
        "input_data": {
            "columns": [
                "school","sex","age","address","famsize","Pstatus",
                "Medu","Fedu","Mjob","Fjob","reason","guardian",
                "traveltime","studytime","failures","schoolsup",
                "famsup","paid","activities","nursery","higher",
                "internet","romantic","famrel","freetime","goout",
                "Dalc","Walc","health","absences"
            ],
            "index": [0],
            "data": [[
                "GP",
                sex,
                age,
                "U",
                "GT3",
                "T",
                Medu,
                Fedu,
                "teacher",
                "teacher",
                "course",
                "mother",
                1,
                studytime,
                failures,
                "no",
                "yes",
                "no",
                "yes",
                "yes",
                "yes",
                internet,
                "no",
                4,
                3,
                3,
                1,
                Walc,
                5,
                absences
            ]]
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(
        ENDPOINT_URL,
        json=payload,
        headers=headers
    )

    print("STATUS:", response.status_code)
    print("TEXT:")
    print(response.text)

    prediction = response.json()[0]

    if prediction < 10:
        grade = 1
    elif prediction < 12:
        grade = 2
    elif prediction < 14:
        grade = 3
    elif prediction < 16:
        grade = 4
    else:
        grade = 5

    labels = {
        1: "Fail",
        2: "Sufficient",
        3: "Good",
        4: "Very Good",
        5: "Excellent"
    }

    return render_template(
    "index.html",
    prediction=round(prediction, 2),
    grade=grade,
    label=labels[grade],

    age=age,
    studytime=studytime,
    failures=failures,
    absences=absences,

    sex=sex,
    Medu=Medu,
    Fedu=Fedu,
    internet=internet,
    Walc=Walc
)


if __name__ == "__main__":
    app.run(debug=True)