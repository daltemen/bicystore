# bicystore

Example of Flask Api in App engine

Install libraries (It's very important -t parameter)
```
pip install -t lib -r requirements.txt
```

How to set a App Engine project ?
```
gcloud config set project <PROJECT-ID>
```

How to run local server ?
```
dev_appserver.py ./app.yaml
```


Deploy app !
```
gcloud app deploy --project <PROJECT-ID>
```