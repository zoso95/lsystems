import os
import json
import numpy as np
import uuid

from tqdm import tqdm
from grammar import *
from plot import *

import pickle
import scipy

"""
elif x == '[':
    saved_states.append((pos, direction))
elif x == ']':
"""
def make_random_l_system():
    # TODO add []
    # TODO make it have different weights for different symbol classes
    # TODO make the number of dummy variable a parameter
    symbols = ["F", "+", "-", "*", "/", "|", "A"]
    probs = [0.4, 0.2, 0.2, 0.0, 0.0, 0.0, 0.2]

    a_len = np.random.randint(4, high=10, size=1)[0]
    b_len = np.random.randint(4, high=10, size=1)[0]

    rules = {
        'A':''.join(list(np.random.choice(symbols, a_len, p=probs))),
        #'B':''.join(list(np.random.choice(symbols, b_len, p=probs)))
        }

    parameters = {
        'axiom':'A',
        'rules':rules,
        'number_iterations':np.random.randint(3, high=7, size=1)[0],
        'filename': os.path.join("generated", str(uuid.uuid4())[0:5]),
        'angle':np.random.choice([25., 45., 90.]),
    }

    return parameters


def save_info(ls):
    with open(ls["filename"]+".txt", 'w') as file:
     file.write(json.dumps(ls))

def get_feature_vec(data):
    r = data["rules"]['A']
    symbols = ["F", "+", "-", "*", "/", "|", "A"]
    simple_features = [data["angle"], data["number_iterations"]]
    single_counts = [r.count(c) for c in symbols]

    double_counts = []
    for i, a in enumerate(symbols):
        for b in symbols[i+1:]:
            double_counts.append(r.count(a+b))
            double_counts.append(r.count(b+a))

    return np.array(simple_features+single_counts+double_counts)


def main():
    number_of_renders = 50

    model = pickle.load(open("classifer_model.pickle", "rb"))

    for _ in tqdm(range(number_of_renders)):

        while True:
            ls = make_random_l_system()
            x = get_feature_vec(ls).reshape(1,-1)
            prob = model.predict_proba(x)[0,1]
            #print(prob)
            if prob>= 0.5:
                break

        system = LSystem(ls['axiom'], ls['rules'])
        for _ in range(ls["number_iterations"]):
            system.step()

        render2d_and_save(system.state, ls["angle"], 0.5, np.array([0.1, 0]), fname = ls["filename"]+".png")
        save_info(ls)




if __name__ == '__main__':
	main()
