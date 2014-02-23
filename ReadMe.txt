This is the first file to read. You're in the right place. Go on.

This is the cached version of the solution to the application asked in Challenge-1 of the internship interview.
Time taken for the application to run:
On an average this takes around 0.06  to 0.13 seconds depending on "the amount" and "no of items". So, it's almost one tenth of a second.
Time prints have been inserted suitably in the file for your reference.

It has two python files.

1. connect.py - RUN THIS FIRST
This is NOT the actual application file and this need NOT be run everytime a user asks for an amount-items combination.
This is like a BACKGROUND task and can be run like once or twice in a day (or even infrequently depending on how quickly the products at Zappos go outdated and how quickly new products get added.)
This is done for two reasons:
1. So that this file can run in background once or twice in a day (or even infrequently depending on how quickly the products at Zappos go outdated and how quickly new products get added.) and so that the actual user amount-items application runs lightening fast.
b. Because the APIs have a limit of 2,500 per day, so not a good idea to practice hitting the costly and heavy API service everytime.

On an average, this file takes around 50 seconds to run.
Don't worry, this won't run every time. Just once in a day, in background. Doesn't run when user uses the main application which is Display.py and which is super-fast. Time prints have been inserted suitably in the file for your reference.

Way to run this file.
This is a no argument file. Run it like below:
$ python connect.py

It generates a catalog.txt file in the python path automatically. If you're not running it from the python path,  place copy the generated catalog.txt file in the place where Display.py is located. For reference, a Catalog,txt file has been given.

2. Display.py - RUN THIS AFTER RUNNING connect.py

This is the ACTUAL application that displays the combinations of products for an "amount-no of items".
On an average this takes around 0.06  to 0.13 seconds depending on "the amount" and "no of items". So, it's almost one tenth of a second.
Time prints have been inserted suitably in the file for your reference.

Way to run this:
This takes the file-name and 3 arguments.
1. Name of the file: Display.py
2. The amount
3. Number of items
4. Number of possible combinations you would like to see 
So, the usage format is 
$ python Display.py <amount> <no_of_items> <no_of_combinations_to_show>
Example: $ python Display.py 155 4 10 
means, 4 items, which sum tp $155 and 10 such combinations.
Also, make sure that the file saved by connect.py is in the Python path or in the directory where this file is located.