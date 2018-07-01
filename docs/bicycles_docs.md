# bicystore API REST docs

This api will allow you to have a bicycle the one you want

EndPoints for Bicycle Parts

* Create Bicycles : `POST /bicystore/bicycles`
* Get Bicycle : `GET /bicystore/api/v1/bicycles/{id}`
* Update Bicycle : `PUT /bicystore/api/v1/bicycles/{id}`
* Delete Bicycle : `DELETE /bicystore/api/v1/bicycles/{id}`


Create Bicycles
**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide name of Part to be created.

**Data example** All fields must be sent.

```json
{
	"wheels": 5838406743490560,
	"chain": 5311740673785856
}
```

**Response** Brakes Example

```json
{
    "bicycle": {
        "brakes": null,
        "chain": 5311740673785856,
        "fork": null,
        "frame": null,
        "id": 6156165603917824,
        "saddle": null,
        "wheels": 5838406743490560
    }
}
```

Update Bicycles
**Method** : `PUT`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

Provide name of Part to be created.

**Data example**

```json
{
    "chain": 5311740673785856
}
```

**Response** Brakes Example

```json
{
    "bicycle": {
        "brakes": null,
        "chain": "Adri Chain",
        "fork": null,
        "frame": null,
        "id": 5171003185430528,
        "saddle": null,
        "wheels": "Wheel Yamahas"
    }
}
```
