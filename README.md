# sportmanager

_CLI tool to improve fitness monitoring_

## Concept

Data will be stored in ElasticSearch in order to make my ES skill a bit less rusty.

## Installation

```bash
$ pip install sportmanager
```


## Data format

```javascript
// A workout
{
    "name": "arbitrary name",
    "date": datetime.datetime,
    "type": "legs | back | push | pull...", // must be consistent
    "exercises": [{}],
    "meta": {}, // arbitrary
}
```
