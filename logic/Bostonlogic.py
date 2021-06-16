import pandas as pd
from model import Boston
import pickle


class BostonLogic:
    model = None

    def __init__(self):
        self.load_data()

    def load_data(self):
        # global carInfo
        # global model
        with open("artifacts/boston_model.pickle", "rb") as f:
            BostonLogic.model = pickle.load(f)

    def predict_price(self, boston: Boston.BostonDto):

        x_test = pd.DataFrame([[boston.CrimeRate, boston.ZonedLand, boston.NonRetailAcres, boston.CharlesRiver, boston.Nox,  boston.NoOfRooms, boston.BuildingAge,
                               boston.DistanceToEmpCenters, boston.Accessibility, boston.Tax, boston.TeacherRatio, boston.BlacksProposition, boston.LowerStatus]],
                              columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                                       'PTRATIO', 'B', 'LSTAT'], dtype=object)
        # x_test = pd.DataFrame([[0.38214, 0.0, 6.20, 0.0, 0.504,
        #                             8.040	, 86.5, 3.2157, 8.0, 307.0, 17.4, 387.38, 3.13]],
        #                           columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
        #                            'PTRATIO', 'B', 'LSTAT'], dtype=object)
        try:
            result = BostonLogic.model.predict(x_test)[0]
            return "Predicted value of owner occupied home is <b>" + str(result) + "</b>"
        except Exception as error:
            print(error)
            return error
