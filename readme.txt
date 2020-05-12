## How to use the api
(after you clone or download the project and install the required libraries)
1. start flask api
    $ python app.py
2. test the api 
  2.1 from terminal using curl (with the input data)
    $ curl -X POST http://0.0.0.0:5000/predict/ -H "Content-Type: application/json" -d '[35,"female",35,3,"yes","southwest"]'
  2.2 from testapi.py file
    adjust your input in the file first, then run the file on terminal
    $ python testapi.py

Note: input data is list of age, sex, bmi, children, smoker, and region
      age: age in year
      sex: "male" or "female"
      bmi: Body mass index,calculated from weight(kg)/height(m)^2
      children: Number of children covered by health insurance / Number of dependents
      smoker: Smoking "yes" or "no"
      region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest
      
Note: test on my heroku app in your terminal
    $ curl -X POST https://flask-medicalcost-api.herokuapp.com/predict/ -H "Content-Type: application/json" -d '[35,"female",35,3,"yes","southwest"]'
