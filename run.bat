behave -f allure_behave.formatter:AllureFormatter -o report/allure_results
allure generate report/allure_results -o report/allure_report --clean
cd report
allure serve
