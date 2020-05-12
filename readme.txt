#test API on terminal 
curl -X POST http://0.0.0.0:5000/predict/ -H "Content-Type: application/json" -d '[35,"female",35,3,"yes","southwest"]'
