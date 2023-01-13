Project Title: Most Active Cookies

Description:

This project was developed as a way to improve my skillset in python and file use in the language. It is meant to utilize the concept of file reading, data storage, and return - often seen in cookie caches and data analysis programs - and create a small scale (personal device size) to help users organize and monitor data on specific files in their personal device.

A cookie cache reading system is used to run data analyses on large scale csv files that often store large amounts of loggable data. This data can be interpreted to find different uses of the program/site/etc and how often its being used (as seen in this case). For example, finding out how many times a user logged into a server within the span of 24 hours or at a specific time.

The way this tool works is a user can submit a csv file that holds large quantities of data along with a specific date that they wish to attain the data of. The program can then search the file for any data values that were taken on that date, and return which cookie was the most active for that day. It is able to recognize when multiple cookies have been equally used, or if no cookies were logged for that day.



This project utilizes 1 file:

1. most_active_cookie.py:

- Uses 2 external libraries:
    - sys: used to interact with the interpreter
    - unittest: used in test cases for the most_active_cookies function

- Function: most_active_cookies()
    - Parameters; 2; file name: csvfile, string: date
    - Return; one list with the most active cookie
    - Description: Returns the most active cookie of a specified date within a csv file

- Class: UnitTestMostActiveCookies()
    - Parameters; 1; TestCase

    - Methods; 3
        - most_active_cookies_singular_test()
            - Parameters; 2; file name: csvfile, string: date
            - Return; one list with the most active cookie
            - Description: Tests whether the function can recognize the most active cookie
        
        - most_active_cookies_multitude_test()
            - Parameters; 2; file name: csvfile, string: date
            - Return; one list with the most active cookie
            - Description: Tests whether the function can recognize to return multiple cookies of the same activity level

        - most_active_cookie_none_test()
            - Parameters; 2; file name: csvfile, string: date
            - Return; one list with the most active cookie
            - Description: Tests whether the function can recognize there is no data to return for the specified date

