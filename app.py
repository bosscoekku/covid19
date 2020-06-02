import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

# URL API from covid19.th-stat.com 
# Thank you for information
urlDataCovid19Today    = "https://covid19.th-stat.com/api/open/today"
urlDataCovid19Timeline = "https://covid19.th-stat.com/api/open/timeline"
urlDataCovid19Case     = "https://covid19.th-stat.com/api/open/cases"
urlDataCovid19Sum      = "https://covid19.th-stat.com/api/open/cases/sum"

# Call API and write to JSON file
responseDataCovid19Today    = requests.request("GET", urlDataCovid19Today)
responseDataCovid19Timeline = requests.request("GET", urlDataCovid19Timeline)
responseDataCovid19Case     = requests.request("GET", urlDataCovid19Case)
responseDataCovid19Sum      = requests.request("GET", urlDataCovid19Sum)

# Pandas read JSON file to DataFrame
dataCovid19Timeline     = pd.DataFrame(responseDataCovid19Timeline.json()['Data'],columns = ['Date', 'NewConfirmed','NewRecovered','NewHospitalized','NewDeaths','Confirmed','Recovered','Hospitalized','Deaths'])
dataCovid19Case         = pd.DataFrame(responseDataCovid19Case.json()['Data'],columns = ['ConfirmDate', 'No','Age','Gender','GenderEn','Nation','NationEn','Hospitalized','Province','ProvinceId','District','ProvinceEn','Detail','StatQuarantine'])
dataCovid19Today        = pd.DataFrame(responseDataCovid19Today.json().values(),responseDataCovid19Today.json().keys()).T
dataCovid19SumProvince  = pd.DataFrame(responseDataCovid19Sum.json()['Province'].values(),responseDataCovid19Sum.json()['Province'].keys()).T
dataCovid19SumNation    = pd.DataFrame(responseDataCovid19Sum.json()['Nation'].values(),responseDataCovid19Sum.json()['Nation'].keys()).T
dataCovid19SumGender    = pd.DataFrame(responseDataCovid19Sum.json()['Gender'].values(),responseDataCovid19Sum.json()['Gender'].keys()).T
