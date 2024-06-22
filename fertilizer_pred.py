import pickle
# from server import a
import pandas as pd

MODEL_PATH = 'fertilizerPrediction.pkl'
def load_model(model_path):
    with open(model_path, 'rb') as file:
        return pickle.load(file)
model = load_model(MODEL_PATH)
a = {'temperature': '192', 'Humidity': '1222', 'moisture': '12111', 'N': '1200', 'K': '2', 'P': '0.01', 'cropname': 'Maize'}
features_df = pd.DataFrame([a])
prediction = model.predict(features_df.drop(columns=['cropname','Humidity','moisture']))
a['Fertilizer'] = prediction[0]

if __name__ == "__main__":
    print(prediction)