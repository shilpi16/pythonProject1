 rem chrome
 
 pytest -s -v -m "sanity" --html=Reports\report_chrome.html testCases --browser chrome
 REM pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases --browser chrome
 REM pytest -s -v -m "sanity or regression" --html=Reports\report.html testCases --browser chrome
 REM pytest -s -v -m "regression" --html=Reports\report.html testCases --browser chrome
 
 rem firefox
 
 pytest -s -v -m "sanity" --html=Reports\report_firefox.html testCases --browser firefox
 REM pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases --browser firefox
 REM pytest -s -v -m "sanity or regression" --html=Reports\report.html testCases --browser firefox
 REM pytest -s -v -m "regression" --html=Reports\report.html testCases --browser firefox