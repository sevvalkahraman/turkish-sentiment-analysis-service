#### Create an environment
```bash
git add .
git commit -m 'init'
git remote add origin https://github.com/sevvalkahraman/turkishSentimentAnalysisService.git
git push origin master
```

#### Create an environment

```bash
python -m venv venv
```

#### Activate the environment
```bash
venv\Scripts\activate.bat 
```

#### Deactivate the environment
```bash
venv\Scripts\deactivate.bat
```

#### Install libraries in Requirements file.
```bash
pip install -r requirements.txt
```

### Run the service
```bash
set FLASK_APP=application.py
flask run
```