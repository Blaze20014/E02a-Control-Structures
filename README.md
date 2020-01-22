
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?

  I expect main01.py to display greetings and then allow me to answer the question what is my favorite color

  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.

    It displayed the text "Greetings!" and asked me what my favorite color was which i was able to answer

  - What do you think the program did with what you typed in answer to the question?

    nothing, there was no variable to store the answer so the answer was lost 

- Open main02.py. Before running it, describe how this is different than main01.py.

    It actually stores your answer into a variable and prints it back

  - What do you think the color = input() will do?

      It will allow me to input an answer and then store that answer into the variable color 

  - Run the program in the terminal and answer the question. Did the program do what you expected?

      Yes it did

- Open main03.py. Before running it, describe how this is different than main02.py.

  There is an if...else statement in play now

  - What is happening on lines 9–12?

    If the value in color is equal to "Red" it will print 'correct' Else it prints 'sorry, try again'.

  - Why are lines 10 and 12 indented?

    because those lines act based on the result of the previous line (the if...else statement)

  - Run the program and answer the question. What happens if you don’t capitalize Red?

    it counts it as not 'Red'

  - What does this tell you about "color"?

    color is case sensitive or currently lowercase

- Open main04.py. Before running it, describe how this is different than main03.py.

  there is an Or operator in the if else statement

  - What problem is this trying to solve?

    the case sensitive problem

  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?

    Another problem will arise because the capitalization doesn't match

- Open main05.py. What do you expect line 9 to do?
  
  convert color's value to the lowercase form then compare it in the if else

  - What problem is it trying to solve?

    the variant capitalization problem

  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?

    It will run the else statement

 - Open main06.py. How is line 9 different than in main05.py?

    convert it to the lowercase form, and then removes the spaces from the sides

   - What would you guess .strip() is doing?

      removing the spaces from the outer sides

   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?

    adding a special character to the end (red!)

 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?

    if the color isnt red, it check if the color is pink, otherwise run the else statement 

   - What is happening on line 12?

    the code is checking if the value of color is pink

   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?

    while the value of color isn't equal to red the indented block of code will continue to execute 

   - Why are lines 10–17 indented?

    they run based on the while loop on line 9

   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?

    the loop could be skipped and the program would end immediately, it also makes an infinite loop

   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?

    it adds one to the current value of the count variable

   - What is the purpose of “count”?

    counts the amount of iterations of the loop 

   - What is happening on line 22?

    on line 21, its printing a statement with the amount of guesses where the brackets are  
    
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
  
  DONE

 - *Extra credit:* open main11.py. What is happening on lines 6-11?

    a function that chooses the color and makes sure the color isn't the same as the last chosen color is created (Even though there isn't a way that last_color changes, it will constantly be ''.)
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
