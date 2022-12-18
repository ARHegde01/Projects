Project Title: CDN Simulator

Description:
This project was developed as a way to fine tune my understanding of C++11 and its uses. More so, the CDN Simulator was developed to take the concept of a content delivery network - often seen in websites and online platforms - and create a small scale version that would help users organize and monitor files on their personal device.

A CDN is a delivery system built on the user side of a network that helps keep the server from being over whelmed with requests. For example, the CDN stores the most recent version of a piece of content, so if 10 clients request the same file, all clients would receive a copy from the CDN, with the server only getting 1 request. 

The way this tool works is when content is requested by a client, we (the user) can ask the server for that data and store it within our cache. 
This cache remains active for a set period of time, called freshness, that the user sets. For example, 1 minute. 
For any further requests for that file within a minute, the cache sends the client a copy of that file. If a request comes prior to that minute, we ask the server for an updated version of the content and reset the freshness. 

This project utilised two different files:

1. the Library:
- Establishes the Cache class which holds:
    - private members such as structs to hold data pulled from files
    - private member such as variables to be used inside these structs and within the header file
    - public members such as declared methods

2. the Header:
- Defines a Cache class constructor
- Defines a destroyer to remove files from Cache class

- First method - getText
    Parameter; 1; string filepath
    Return: string; fresh/updated copy of text file
    Description: Can pull data from filepath by reading text in it as linkedlist

- Second method - getBinary
    Parameter; 1; string filepath
    Return: char; fresh/updated copy of binary file
    Description: Essentially same as getText, however, all content inside given file is in binary char instead of text

- Third method - isCached
    Parameter; 1; string filepath
    Return: bool; 
    Description: Returns bool True if the file you received matches a previously saved file

- Fourth method - getFreshness
    Parameters; 1; string filepath
    Return: unsigned int; remaining requests
    Description: Takes a given file, and returns an unsigned int depicting how many requests are left for the file till freshness is depleted

- Fifth method - markFileFresh
    Parameters; 1; string filepath
    Return: none
    Description: Recieves a file name, if the file is currently stored in cache, reset its freshness to original value

- Sixth method - purgeCache
    Parameters; 0; none
    Return: none
    Description: Deletes all currently stored files in your cache, any calls after this has class read the file from the disk
    
- Seventh method - topFile
    Parameters; 0; none
    Return: none
    Description: method returns the file thats been requested the most (same concept as search engine optimization)

- Eighth method - getStats
    Parameters; 0; none
    Return: string; cache stats report
    Description: method returns a string report of the stats of the cache