import optuna.integration.lightgbm as lgb
import numpy as np
#import createCSV
import teller

def load_model():
    bst = lgb.Booster(model_file='../model/model.h5')
    return bst

def predict(data):
    # load model
    bst = load_model()
    # predict
    y_pred = bst.predict(data, num_iteration=bst.best_iteration)
    # clamp 0 1
    y_pred = np.where(y_pred > 0.5, 1, 0)
    return y_pred

def Getdata():
    #result = createCSV.results
    result = teller.results
    data = []
    for id in result:
        data.append([result[id]["domain"], result[id]["network"], result[id]["extend"], result[id]["regex1"], result[id]["regex2"], result[id]["regex3"], result[id]["regex4"], result[id]["regex5"], result[id]["virustotal"]])
    
    return data

def makedict():
    data = Getdata()
    result = dict()
    for i in range(len(data)):
        """
        {
            1: {"ad": true or false},
            2: {"ad": true or false}
        }
        """
        id = i + 1
        if predict([data[i]]) == 1:
            result[id] = {"ad": True}
        elif predict([data[i]]) == 0:
            result[id] = {"ad": False}
    return result
       
if __name__ == '__main__':
    makedict()