# API Checklist - GET /posts/1

## Positive checks

* Status code = 200
* Content-Type = application/json
* Response body is not empty
* Field userId exists
* Field id exists
* Field title exists
* Field body exists
* userId data type = integer
* id data type = integer

## Negative checks

* Request with non-existing id
* Request with special characters instead of id
* Request with incorrect HTTP method
* Request with unsupported Accept header

## Non-functional checks

* Response time validation
* Caching behavior validation
