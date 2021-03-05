#!/bin/bash

export KAGGLE_USERNAME=bubulibubulle
export KAGGLE_KEY=cf8b6f313e12641849239181d43adf47
app="bubulibubulle/tp_gregor"
export KAGGLE_USERNAME=bubulibubulle
export KAGGLE_KEY=cf8b6f313e12641849239181d43adf47
docker build -t ${app} .
export KAGGLE_USERNAME=bubulibubulle
export KAGGLE_KEY=cf8b6f313e12641849239181d43adf47
docker run -d -p 50000:80 ${app}
export KAGGLE_USERNAME=bubulibubulle
export KAGGLE_KEY=cf8b6f313e12641849239181d43adf47
