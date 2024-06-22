import pandas as pd
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import csv
def fert_pred(data_insoil):
        # print('Thissss')
        # data_test = pd.read_csv("Datasets\TestFarm1.csv")
        features_df = pd.json_normalize(data_insoil)        
        # print(features_df)
        MODEL_PATH = 'fertilizerPrediction.pkl'
        # print('This is here')
        def load_model(model_path):
            with open(model_path, 'rb') as file:
                return pickle.load(file)
        # print('This is herwwwwwwwwwwwwwwwe')
        model = load_model(MODEL_PATH)
        # print('This is herxsssssssse')
        features_df['Fertilizer'] = model.predict(features_df.drop(['lat', 'lng','Humidity','moisture'], axis = 1))
        # print('HERRRRRRRRRRRRRRRRRREEEEEEEEE')
        print( features_df['Fertilizer'])

        features = features_df[['lat', 'lng', 'Fertilizer']]
        transformers = [('one_hot_encoder', OneHotEncoder(), ['Fertilizer']),
                        ('scaler', StandardScaler(), ['lat', 'lng'])]
        
        preprocessor = ColumnTransformer(transformers = transformers)

        features_preprocessed = preprocessor.fit_transform(features)

        ssd = []
        K = range(1, 10)
        for k in K:
            km = KMeans(n_clusters = k)
            km = km.fit(features_preprocessed)
            ssd.append(km.inertia_)

        elbow_point = ssd.index(min(ssd))

        kmeans_optimal = KMeans(n_clusters = elbow_point, random_state = 0).fit(features_preprocessed)

        features_df['clusters'] = kmeans_optimal.labels_
        clusters = features_df['clusters'].unique()
        for cluster in clusters:
            features_df.loc[features_df['clusters'] == cluster, 'Recommended Fertilizer'] = recommend_fert(cluster, features_df)


        for i in range(ssd.index(min(ssd))):
            print(features_df[features_df['clusters'] == i])
            print('------------------------------------------------')

        return features_df[['lat', 'lng', 'Recommended Fertilizer']]

def recommend_fert(cluster, data):

        cluster_data = data[data['clusters'] == cluster]
        if not cluster_data.empty:
            recom_fert = cluster_data['Fertilizer'].mode()[0]
        else:
            recom_fert = None
        return recom_fert

if __name__ == "__main__":
    with open("Datasets/TestFarm1.csv", "r") as f:
        reader = csv.DictReader(f)
    data_insoil = list(reader)
    print(fert_pred(data_insoil))

