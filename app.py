from flask import Flask,render_template,request
import random

app = Flask(__name__)

odgovori=[
    "Da",
    "Ne",
    "Vprašaj kasneje",
    "Nevem",
    "Adijo"
]


besede=["ljubezen","vikend","denar","profesor","!"]


@app.route("/", methods=["GET", "POST"])
def vprasanja():

    odgovor=None
    if request.method == "POST":
        vnos = request.form.get("vprasanja")

        for beseda in besede:
            if beseda in vnos:
                if "ljubezen" in vnos:
                    odgovor="Raje kupi GPU."
                    return(render_template("index.html", odgovor=odgovor))
                if "vikend" in vnos:
                    odgovor="Tik tok all day."
                    return(render_template("index.html", odgovor=odgovor))
                if "denar" in vnos:
                    odgovor="Burek only."
                    return(render_template("index.html", odgovor=odgovor))
                if "profesor" in vnos:
                    odgovor="F speedrun."
                    return(render_template("index.html", odgovor=odgovor))
                if "!" in vnos:
                    odgovor="Ne kriči."
                    return(render_template("index.html", odgovor= odgovor))


        if vnos:
            odgovor= random.choice(odgovori)
        
    return(render_template("index.html", odgovor=odgovor))

    





if __name__ == "__main__":
    app.run(debug=True) 