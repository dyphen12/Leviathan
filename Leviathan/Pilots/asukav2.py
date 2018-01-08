


def LonginosSpear ():
    import numpy as np
    import matplotlib.pyplot as plt
    from pandas import read_csv
    import pandas as pd
    from keras.models import load_model
    from sklearn.preprocessing import MinMaxScaler
    from Angels.Armisael import fusion

    print('"Asuka" the pilot for the EVA_Prototype3')

    print('Loading model: EVA_Prototype3')

    model = load_model(
        r'C:\Users\Usuario\Documents\GitHub\Leviathan\Leviathan\Fortune Tellers\Models\Eva_prototype3.h5')

    print('model loaded')

    AsukaON = True

    print('Loading data from Angel: Armisael')

    while AsukaON == True:

        (ArmisaeltrainX, ArmisaeltestX, RawData, AngelStatus) = fusion()

        while AngelStatus == True:
            # make predictions
            trainPredict = model.predict(ArmisaeltrainX)
            testPredict = model.predict(ArmisaeltestX)

            scaler = MinMaxScaler(feature_range=(0, 1))
            scaler.fit(RawData)
            trainPredict = scaler.inverse_transform(trainPredict)

            print('THIS IS THE PREDICTION FOR THE NEXT 10 SECONDS\n')
            print('The most recent prediction\n')

            print(trainPredict[-1])

            recentprediction = trainPredict[-1]
            return recentprediction,RawData

            AngelStatus = False
            AsukaON = True  # ON/OFF Button