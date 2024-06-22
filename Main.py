import json
from npk_model import output_moisture, output_npk, set_optimal_values
print('ababababababab')
from Clustering import fert_pred, recommend_fert
print('1220293028309283092')
import csv
print('72137219738927397')
import pandas as pd
print('ppppppppppppppppppppppppppppppppppppppppppppppppppppppppp')
data_moisture = pd.read_csv('Datasets/merged_dataset.csv')
data_crop = pd.read_csv('Datasets/Crop_Pred.csv')
def thisIsAFunction(data_insoil,cropname):
    optimal_values = set_optimal_values(cropname,data_moisture,data_crop)
    print('michael')
    npk_messages = output_npk(data_insoil,optimal_values['n_optimal'], optimal_values['p_optimal'],optimal_values['k_optimal'])
    print('scottttt')
    print('qqqqqqqqqqqqqqq')
    moisture_message = output_moisture(data_insoil,optimal_values['moisture_optimal'])
    print('ossosososoosososososoososos')

    print(npk_messages)
    print('[][][][][][][][][][][[]]]')

    print(moisture_message)
    print('cvcvcvcvvcvcvcvcvcvcvcvcvcvcvc')

    with open("Datasets/TestFarm1.csv", "r") as f:
        reader = csv.DictReader(f)
        print('//////////////')
        data_insoil = list(reader)
    features_df = fert_pred(data_insoil)
    overall = features_df['Recommended Fertilizer'].mode()[0]
    response = {
        'npk_output': npk_messages,
        'moisture_output': moisture_message,
        'prediction': features_df.to_json(),
        'overall_Fert': overall
    }
    return json.dumps(response)
if __name__ == "__main__":
    print('MEMEMEMEMEMMEMEMEMMEMEMEMMEMEMEM')
    # print(thisIsAFunction(data_insoil,cropname))
    print("MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    
