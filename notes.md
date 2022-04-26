# AdaptID

## Init

- `python run.py`
- `POST http://127.0.0.1:5000/skills/reverse-skill-title`
- `BODY : {"skill_title": "abc"}`
- `r = requests.post(url, json= {'skill_title': 'abc'})`

- 1

```JSON
{
    "OCC 11-1011" : {
        "name" : "Transport ...",
        "emp" : [150, 40, 0]
    },

    "OCC 53-5511" : {
        "name" : "building ...",
        "emp" : {
            "MSA 1 4546" : "452",
            "MSA 2 123" : "777",
        }
    }
}
```

- response

```JSON
{
    "response" : [
        {
            "job" : "WOrk",
            "emp_cnt" : 123
        },
        {

        }
    ]
}
```

- response 1

```JSON
{
    "city 1" : [
        {
            "job" : "WOrk",
            "emp_cnt" : 123
        },
        {
            "job" : "WOrk1",
            "emp_cnt" : 123
        }
    ],
    "city 2" : [
        {
            "job" : "WOrk",
            "emp_cnt" : 123
        }
    ]

}
```

- error response

```JSON
{
    "ERROR" : "error"
}
```
