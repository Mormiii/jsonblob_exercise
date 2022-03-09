Hi!

This is a REST - API test project
The goal is to test create, update and delete methods on JSON Blob API.
I've made this project in PyCharm, using python, pytest, pytest_bdd and requests library.

The content of this project :
    env folder: virtual environment where all the needed modules are installed
    testsuite_jsonblob folder: here are the test related files
        features folder: .feature file, corresonding to the test.py
                     - business logic is presented - bdd style
                     - testdata is stored here ( in long term test data should be handled differently)

        test_jsonblob.py : the logic/scripting for the tests
    pytest-how_to_run_config.png : the configuration is printscreened to support setting it up
    README.txt

There are 3 scenarios, each with different test data, to check unsuccessful cases as well.
Its easy to extend the test cases, adding new examples.


About pytest:
https://docs.pytest.org/en/6.2.x/

About pytest_bdd:
https://pypi.org/project/pytest-bdd/

How to run the testcases(in PyCharm):
In the Run/Debug Configurations, create a new :Pyton tests- pytest:
Target and Working directory should be filled with the location of this project.
(printscreen is attached)

