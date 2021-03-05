# from app import app
#
# @app.route('/')
# def home():
#    return "hello world!"

# import kaggle
#
from flask import Flask, render_template, jsonify
from app import app
# import csv

@app.route('/')
def home():
    # kaggle.api.authenticate()
    # kaggle.api.dataset_download_files('mrdew25/pokemon-dataset', unzip=True)
    # dict = dict()
    i = 0

    dict={ 'Name' : 'Type'}

    test={1:1}
    with open("Pokemon Database.csv") as csv_file:
        for row in csv_file:
            l = row.split(',')
            dict[l[2]]=l[9]
        test={1:2}
        # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # for row in spamreader:
        #     #print(', '.join(row))
        #     dict[i]=', '.join(row)
        # i+=1
    return jsonify(dict)
