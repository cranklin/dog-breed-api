Sample Flask Application - Dog Breed API
========================================
This application is used as my demonstration for:
<a href="https://cranklin.wordpress.com/2016/08/09/testing-the-right-way/">Testing The Right Way</a>


Description:
------------
List all of the available dog pictures grouped by breed
List all of the available dog pictures of a particular breed
Vote up and down a dog picture
The details associated with a dog picture
The information the Dog Breed App needs to function is:

A URL to a dog picture
The number of time the picture was favorited
The dog's breed
Any other information required to identify a specific dog
The Dog Breed App expects the response to be sorted by the number of times the picture was favorited. The pictures may be sorted

The API responses must be in JSON.

Additional Voting Requirements

Each client is allowed to vote once for any particular dog picture.


To install:
-----------
```
(set up a virtual environment)
> virtualenv venv
> . venv/bin/activate
(install dependencies)
> pip install -r requirements.txt
(run unit tests with coverage)
> nosetests --with-coverage --cover-package=dogbreed
(start flask server)
> ./run.py
```




A successful test run should yield:
-----------------------------------
```
....................
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
dogbreed.py                  21      0   100%
dogbreed/actions.py          34      0   100%
dogbreed/base.py              0      0   100%
dogbreed/base/models.py      20     11    45%   10-25
dogbreed/exceptions.py       16      0   100%
dogbreed/models.py           51     10    80%   19, 29-31, 34, 49-51, 54, 68
dogbreed/routes.py           30      0   100%
-------------------------------------------------------
TOTAL                       172     21    88%
----------------------------------------------------------------------
Ran 20 tests in 0.998s

OK
```
