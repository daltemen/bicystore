# bicystore API REST docs

This api will allow you to have a bicycle the one you want

EndPoints for Bicycle Parts

* Create Brakes : `POST /bicystore/api/v1/brakes`
* List Brakes : `GET /bicystore/api/v1/brakes`

* Create Forks : `POST /bicystore/api/v1/forks`
* List Forks : `GET /bicystore/api/v1/forks`

* Create Chains : `POST /bicystore/api/v1/chains`
* List Chains : `GET /bicystore/api/v1/chains`

* Create Frames : `POST /bicystore/api/v1/frames`
* List Frames : `GET /bicystore/api/v1/frames`

* Create Saddles : `POST /bicystore/api/v1/saddles`
* List Saddles : `GET /bicystore/api/v1/saddles`

* Create Wheels : `POST /bicystore/api/v1/wheels`
* List Wheels : `GET /bicystore/api/v1/wheels`

* Create Wheels : `POST /bicystore/api/v1/wheels`
* List Wheels : `GET /bicystore/api/v1/wheels`

For Get and Create bicycles:

* [Bicycles](bicycles_docs.md)

For Create Parts the body of request is the same :D !

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide name of Part to be created.

**Data example** All fields must be sent.

```json
{
    "name": "Wheel or Brakes or whatever"
}
```

**Response** Brakes Example

```json
{
    "brake": {
        "id": 5629499534213120,
        "name": "Shimano Brakes"
    }
}
```
