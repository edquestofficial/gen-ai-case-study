<!-- THis is test commit from ED-19-test branch. -->
Step 1: Sample Sum Function
In Directory sample_unit_tese/sum.py is main file for sum

Step 2: Write Unit Test for the Sum Function
Create another file named test_sum.py, this is sum.py unit test case file

Step 3: Run the Unit Test
To run the unit test, execute the following command in your terminal:

    python -m unittest test_sum.py

You should see an output similar to:

....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK


Step 4: Install coverage for Coverage Report
Install the coverage module using pip:

    pip install coverage

Step 5: Generate Coverage Report
Run the following commands to check the test coverage:

Run the tests with coverage:

    coverage run -m unittest test_sum_function.py

Generate the coverage report:

    coverage report

To create an HTML coverage report:

    coverage html

The HTML report will be available in the htmlcov directory. Open htmlcov/index.html in your browser to see a detailed report.

Output Examples
Coverage Report in Terminal:


Name                   Stmts   Miss  Cover
------------------------------------------
sum.py            2      0   100%
test_sum.py      17      0   100%
------------------------------------------
TOTAL                     19      0   100%
