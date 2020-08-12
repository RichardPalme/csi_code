import pickle as pkl
import os
import json

# kann nicht geshuffled werden
data_x_vgenome = []

# die zugehörige range (lo, hi) (hi is exclusive) zu jeder region description
data_x_vgenome_ranges = []

with open('region_descriptions.json') as json_file:
    data = json.load(json_file)

    k = 0
    for datum in data:
        lo = k
        for region in datum['regions']:
            data_x_vgenome.append(region['phrase'].split())
            k += 1
        hi = k # exclusive!!!
        data_x_vgenome_ranges.extend([(lo, hi)] * (hi-lo))
        if len(data_x_vgenome) != len(data_x_vgenome_ranges):
            print('error')

    pkl.dump(data_x_vgenome, open('data_x_vgenome.pkl', 'wb'))
    pkl.dump(data_x_vgenome_ranges, open('data_x_vgenome_ranges.pkl', 'wb'))
