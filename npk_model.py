# npk_model.py

import pandas as pd

def set_optimal_values(cropname, data_moisture, data_crop):
    optimal_values = {}
    print('Scottt')
    print(cropname.lower())
    print(data_moisture[data_moisture['label'].str.lower() == cropname.lower()])
    moisture_data = data_moisture[data_moisture['label'].str.lower() == cropname.lower()]
    print('Michael')
    if not moisture_data.empty:
        optimal_values['moisture_optimal'] = moisture_data['Soil Moisture'].iloc[0]
    else:
        optimal_values['moisture_optimal'] = None

    n_data = data_crop[data_crop['Crop'].str.lower() == cropname.lower()]
    if not n_data.empty:
        optimal_values['n_optimal'] = n_data['N'].iloc[0]
        optimal_values['p_optimal'] = n_data['P'].iloc[0]
        optimal_values['k_optimal'] = n_data['K'].iloc[0]
    else:
        optimal_values['n_optimal'] = None
        optimal_values['p_optimal'] = None
        optimal_values['k_optimal'] = None

    return optimal_values

def output_npk(data_insoil,n_optimal, p_optimal, k_optimal):
    messages = []
    cropname = data_insoil.pop(-1)
    data_insoil = pd.json_normalize(data_insoil)
    n_median = data_insoil['N'].median()
    p_median = data_insoil['P'].median()
    k_median = data_insoil['K'].median()
    try:
        if n_optimal is not None:
            n_diff = float(n_median) - n_optimal
            messages.append(f'You have to {"decrease" if n_diff > 0 else "increase"} the value of N in the soil by {abs(n_diff)}')
        else:
            messages.append("Optimal value for N is not available.")
        
        if p_optimal is not None:
            p_diff = float(p_median) - p_optimal
            messages.append(f'You have to {"decrease" if p_diff > 0 else "increase"} the value of P in the soil by {abs(p_diff)}')
        else:
            messages.append("Optimal value for P is not available.")
        
        if k_optimal is not None:
            k_diff = float(k_median) - k_optimal
            messages.append(f'You have to {"decrease" if k_diff > 0 else "increase"} the value of K in the soil by {abs(k_diff)}')
        else:
            messages.append("Optimal value for K is not available.")
    except ValueError as e:
        messages.append(f"Error processing NPK data: {e}")
    return messages

def output_moisture(data_insoil,moisture_optimal):
    messages = []
    data_insoil = pd.json_normalize(data_insoil)
    print(data_insoil['moisture'])
    moisture_median = float(data_insoil['moisture'].median())
    try:
        if moisture_optimal is not None:
            moisture_diff = float(moisture_median) - float(moisture_optimal)
            print('qwqwqwqwqwqwq', moisture_diff)
            messages.append(f'You have to {"decrease" if moisture_diff > 0 else "increase"} the value of moisture in the soil by {abs(moisture_diff)}')
        else:
            messages.append("Optimal value for moisture is not available.")
    except ValueError as e:
        messages.append(f"Error processing moisture data: {e}")
    return messages



# optimal_values = set_optimal_values(data_insoil,cropname, data_moisture, data_crop)