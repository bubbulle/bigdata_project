# bigdata_project

Here are the lines to launch the project :

minikube start

minikube kubectl create deployment hello-minikube -- --image=bubulibubulle/tp_gregor

minikube kubectl expose deployment hello-minikube -- --type=NodePort --port=80

minikube service hello-minikube


you can choose how many replicas you want
minikube kubectl -- scale --replicas=10 deployment/hello-minikube
