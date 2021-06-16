from flask import Flask, render_template, request, json
from logic import Bostonlogic
from model import Boston

app = Flask(__name__, template_folder='templates')

boston_logic = Bostonlogic.BostonLogic()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predictPrice', methods=['POST'])
def predict_price():
    boston_data = Boston.BostonDto(
        CrimeRate=request.form["crime-rate"],
        ZonedLand=request.form["zoned-land"],
        NonRetailAcres=request.form["non-retail-acres"],
        CharlesRiver=request.form["charles-river"],
        Nox=request.form["nox"],
        NoOfRooms=request.form["rooms"],
        BuildingAge=request.form["age"],
        DistanceToEmpCenters=request.form["distance-to-emp-centers"],
        Accessibility=request.form["accessibility"],
        Tax=request.form["property-tax"],
        TeacherRatio=request.form["pupil-teacher-ratio"],
        BlacksProposition=request.form["black-proportion"],
        LowerStatus=request.form["lower-status-population"],
    )

    home_value = boston_logic.predict_price(boston_data)

    return json.dumps({'status': 'OK', 'homeValue': home_value})


if __name__ == '__main__':
    print('Application Started')
    app.run(debug=True)
