# Getting working with Python
This is our introduction to Python, and in some ways some of this has been setup a bit strangely. I understand if it takes you a bit of getting used to. But once it does, you will have:
* Automatic tests that check whether or not your code works
* The ability to put in the values yourself
* Easy access for Mr Matheson to see your progress (and help out!)

## The work you need to do
In each of the exercises, you are writing functions. Each function needs to return a value, based on the parameters it is given. Follow the description in the ***TODO:*** comments to work out what you 
need to do, then write the code to make that happen. 

## Try it yourself, then let pytest try it for you
Each file has code inside to let you provide your own test data, to see how you have gone with the functions. Just hit the play button in VS Code, or go to the terminal and type

    python ex1_number_exercises.py

for example. Once you think you've got it right, check against my tests by going back to the terminal and typing:

    pytest test_ex1_number_exercises.py

This will run pytest against your file to see if you have passed the tests. Each time you commit your changes to github the pytests will all get checked against your code.
Don't worry when it tells you the code has failed before you are done - it checks all of the files. To run pytest on all the files in the folder, you can type:

    pytest
