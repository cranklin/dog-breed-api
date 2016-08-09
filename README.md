Sample Flask Application - Dog Breed API
========================================

To install:
-----------
`
(set up a virtual environment)
> virtualenv venv
> . venv/bin/activate
(install dependencies)
> pip install -r requirements.txt
(run unit tests with coverage)
> nosetests --with-coverage --cover-package=dogbreed
(start flask server)
> ./run.py
`




A successful test run should yield:
-----------------------------------
`
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
`
