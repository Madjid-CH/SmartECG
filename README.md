# SmartECG-Project

## initializing the project
### server
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### client
```bash
cd client
npm install
```

## running the project
### server
```bash
uvicorn main:app --reload
```
or 
```bash
python main.py
```
### client
```bash
cd client
npm run
```

## Endpoints
### server
- `/predict` : predict the class of a given time series
- `/plot/{index}` : return the plot of the instance in position index

