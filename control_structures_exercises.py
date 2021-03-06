{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "46084e92",
   "metadata": {},
   "source": [
    "Conditional Basics\n",
    "\n",
    "    a. prompt the user for a day of the week, print out whether the day is Monday or not\n",
    "\n",
    "    b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend\n",
    "\n",
    "    c. create variables and make up values for\n",
    "\n",
    "        - the number of hours worked in one week\n",
    "        - the hourly rate\n",
    "        - how much the week's paycheck will be\n",
    "    write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e244453a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter ther day of the week:Wednesday\n",
      "Monday is not the day of the week.\n"
     ]
    }
   ],
   "source": [
    "# a. \n",
    "day = input('Please enter ther day of the week:')\n",
    "if day == 'Monday': \n",
    "    print('Monday is the day of the week.')        \n",
    "else: \n",
    "    print('Monday is not the day of the week.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "769c607d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter ther day of the week:Saturday\n",
      "It is the weekend.\n"
     ]
    }
   ],
   "source": [
    "#b. \n",
    "day = input('Please enter ther day of the week:')\n",
    "    \n",
    "if day in ('Saturday', 'Sunday'): \n",
    "    print('It is the weekend.')\n",
    "else: \n",
    "    print('It is a weekday.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5e30d50f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2700.0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#c. \n",
    "weekly_hours = 60\n",
    "hourly_rate = 30\n",
    "\n",
    "paycheck = weekly_hours * hourly_rate\n",
    "paycheck\n",
    "# 1200 with 40 hours a week\n",
    "if weekly_hours <= 40:\n",
    "    pass # could also have done else statement with \n",
    "         # paycheck = weekly_hours * hourly_rate\n",
    "else: \n",
    "    paycheck = weekly_hours * (hourly_rate*1.5)\n",
    "paycheck\n",
    "#2700.0 with 60 hours a week"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc3ccfdd",
   "metadata": {},
   "source": [
    "2. Loop Basics\n",
    "\n",
    "\n",
    "    \n",
    "        \n",
    "       \n",
    "   \n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "319764ed",
   "metadata": {},
   "source": [
    "a. Create an integer variable i with a value of 5.\n",
    "Create a while loop that runs so long as i is less than or equal to 15\n",
    "Each loop iteration, output the current value of i, then increment i by one. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "de3b3456",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "i = 5\n",
    "while i <= 15:\n",
    "    print(i)\n",
    "    i +=1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "49b8e446",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "# b. Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.\n",
    "i = 0\n",
    "while i <= 100: \n",
    "    print(i)\n",
    "    i += 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8d690810",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n",
      "0\n",
      "-5\n",
      "-10\n"
     ]
    }
   ],
   "source": [
    "# Alter your loop to count backwards by 5's from 100 to -10.\n",
    "i = 100\n",
    "while i >=-10: \n",
    "    print(i)\n",
    "    i -= 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5915a555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "16\n",
      "256\n",
      "65536\n"
     ]
    }
   ],
   "source": [
    "# Create a while loop that starts at 2, and displays the \n",
    "# number squared on each line while the number is less than 1,000,000. \n",
    "# Output should equal:\n",
    "i = 2\n",
    "while i < 1000000:\n",
    "    print(i)\n",
    "    i**= 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f7b73266",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "95\n",
      "90\n",
      "85\n",
      "80\n",
      "75\n",
      "70\n",
      "65\n",
      "60\n",
      "55\n",
      "50\n",
      "45\n",
      "40\n",
      "35\n",
      "30\n",
      "25\n",
      "20\n",
      "15\n",
      "10\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# Write a loop that uses print to create the output shown below. (100-5 by 5s)\n",
    "i = 100 \n",
    "while i >= 5: \n",
    "    print(i) \n",
    "    i -= 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8a6f77d1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number here:9\n",
      "9 x 1 = 9\n",
      "9 x 2 = 18\n",
      "9 x 3 = 27\n",
      "9 x 4 = 36\n",
      "9 x 5 = 45\n",
      "9 x 6 = 54\n",
      "9 x 7 = 63\n",
      "9 x 8 = 72\n",
      "9 x 9 = 81\n",
      "9 x 10 = 90\n"
     ]
    }
   ],
   "source": [
    "# b. For Loops\n",
    "# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.\n",
    "\n",
    "num = input('Please enter a number here:')\n",
    "i = 1 \n",
    "\n",
    "while i <= 10:\n",
    "    print(num, 'x', i, '=', int(num) * i)\n",
    "    i += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b034f75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n",
      "666666\n",
      "7777777\n",
      "88888888\n",
      "999999999\n"
     ]
    }
   ],
   "source": [
    "# ii. Create a for loop that uses print to create the output shown below. 1-9 xs the number it is\n",
    "for i in range (1,10):\n",
    "    print(str(i)*i)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c733c21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter an odd number between 1 and 50\n",
      "7\n",
      "Please enter an odd number between 1 and 50\n",
      "Please enter an odd number between 1 and 50\n",
      "9\n",
      "Please enter an odd number between 1 and 50\n",
      "Please enter an odd number between 1 and 50\n"
     ]
    }
   ],
   "source": [
    "# c. break and continue\n",
    "\n",
    "# Prompt the user for an odd number between 1 and 50. \n",
    "# Use a loop and a break statement to continue prompting the user if they enter invalid input. \n",
    "# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, \n",
    "# except for the number the user entered.\n",
    " \n",
    "while True:\n",
    "    print('Please enter an odd number between 1 and 50')\n",
    "    odd = input()\n",
    "    if odd.isdigit() == False:\n",
    "        print('Please enter an odd number between 1 and 50')\n",
    "        continue\n",
    "    if odd not in range(1,51):\n",
    "        print('Please enter an odd number between 1 and 50')\n",
    "        continue\n",
    "    if odd % 2 != 1:\n",
    "        print('Please enter an odd number between 1 and 50')\n",
    "        continue\n",
    "    if (odd.isdigit() and int(odd) in range(1,51) and int(odd) % 2 == 1):\n",
    "        break\n",
    "        \n",
    "odd = int(odd)\n",
    "\n",
    "i = 1\n",
    "while i <50:\n",
    "    if i != odd:\n",
    "        print('Here is an odd number:', i)\n",
    "        i +=2\n",
    "    elif i == odd:\n",
    "        print('Yikes! Skipping number', odd)\n",
    "        i += 2\n",
    "            \n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d52f7127",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a positive number:2\n",
      "0\n",
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "# d. The input function can be used to prompt for input and use that input in your python code.\n",
    "# Prompt the user to enter a positive number and write a loop that counts from 0 to that number.\n",
    "# (Hints: first make sure that the value the user entered is a valid number, also note that the \n",
    "# input function returns a string, so you'll need to convert this to a numeric type.)\n",
    "\n",
    "pos_num = input('Please enter a positive number:')\n",
    "i = 0 \n",
    "num = int(pos_num)\n",
    "\n",
    "if num > 0: \n",
    "    while i <= num: \n",
    "        print(i)\n",
    "        i +=1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8cdb056f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a positive number:7\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# e. Write a program that prompts the user for a positive integer. \n",
    "# Next write a loop that prints out the numbers from the number the user entered down to 1.\n",
    "\n",
    "pos_num = input('Please enter a positive number:')\n",
    "num = int(pos_num)\n",
    "\n",
    "while num >= 1:\n",
    "    print(num)\n",
    "    num -= 1\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c03f7b9",
   "metadata": {},
   "source": [
    "3. Fizzbuzz\n",
    "\n",
    "One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.\n",
    "\n",
    "Write a program that prints the numbers from 1 to 100.\n",
    "For multiples of three print \"Fizz\" instead of the number\n",
    "For the multiples of five print \"Buzz\".\n",
    "For numbers which are multiples of both three and five print \"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a54a0ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "aea9a0e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 101):\n",
    "    if i % 3 == 0 and i % 5 == 0: \n",
    "        print('FizzBuzz')\n",
    "    elif i % 3 == 0: \n",
    "        print('Fizz')\n",
    "    elif i % 5 == 0: \n",
    "        print('Buzz')\n",
    "    else: print(i)\n",
    "# success, order matters"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53d00e7d",
   "metadata": {},
   "source": [
    "4. Display a table of powers.\n",
    "\n",
    "Prompt the user to enter an integer.\n",
    "Display a table of squares and cubes from 1 to the value entered.\n",
    "Ask if the user wants to continue.\n",
    "Assume that the user will enter valid data.\n",
    "Only continue if the user agrees to.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dae4d7a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What number would you like to go up to?\n",
      "3\n",
      "Here is your table!\n",
      "number | squared | cubed\n",
      "------ | ------- | -----\n",
      "1      | 1       | 1     \n",
      "2      | 4       | 8     \n",
      "3      | 9       | 27     \n",
      "To continue enter yes:yes\n"
     ]
    },
    {
     "ename": "SyntaxError",
     "evalue": "'break' outside loop (<ipython-input-4-aaa6de631388>, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-aaa6de631388>\"\u001b[0;36m, line \u001b[0;32m10\u001b[0m\n\u001b[0;31m    break\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m 'break' outside loop\n"
     ]
    }
   ],
   "source": [
    "print('What number would you like to go up to?')\n",
    "user_int = input()\n",
    "n = int(user_int)\n",
    "print ('Here is your table!')\n",
    "print('number | squared | cubed\\n------ | ------- | -----')\n",
    "for i in range(1, n + 1):\n",
    "    print(i,'     |',i ** 2,'      |',i**3,'    ')\n",
    "i = input('To continue enter yes:')\n",
    "if i != 'yes':\n",
    "    break"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c91daf3",
   "metadata": {},
   "source": [
    "5. Convert given number grades into letter grades.\n",
    "\n",
    "Prompt the user for a numerical grade from 0 to 100.\n",
    "Display the corresponding letter grade.\n",
    "Prompt the user to continue.\n",
    "Assume that the user will enter valid integers for the grades.\n",
    "The application should only continue if the user agrees to.\n",
    "Grade Ranges:\n",
    "\n",
    "A : 100 - 88\n",
    "B : 87 - 80\n",
    "C : 79 - 67\n",
    "D : 66 - 60\n",
    "F : 59 - 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dce7727d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your grade: 90\n",
      "A\n",
      "Would you like to continue (yes or no)?:\"yes\n",
      "Enter your grade: 50\n",
      "F\n",
      "Would you like to continue (yes or no)?:\"no\n"
     ]
    }
   ],
   "source": [
    "con = 'yes'\n",
    "while con == 'yes':\n",
    "    num = input('Enter your grade: ')\n",
    "    num = int(num)\n",
    "    if num in range(88,101):\n",
    "        print('A')\n",
    "    elif num in range(87,81):\n",
    "        print('B')\n",
    "    elif num in range(67, 80):\n",
    "        print('C')\n",
    "    elif num in range(60,67):\n",
    "        print('D')\n",
    "    else:\n",
    "        print('F')\n",
    "    con = input('Would you like to continue (yes or no)?:\"')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74ef5bb4",
   "metadata": {},
   "source": [
    "6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.\n",
    "\n",
    "Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b179fc8f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'title': 'title1', 'author': 'author1', 'genre': 'genre1'}\n",
      "{'title': 'title2', 'author': 'author2', 'genre': 'genre2'}\n",
      "{'title': 'title3', 'author': 'author3', 'genre': 'genre3'}\n"
     ]
    }
   ],
   "source": [
    "books = [\n",
    "    {\n",
    "        'title':'title1',\n",
    "        'author': 'author1',\n",
    "        'genre': 'genre1'\n",
    "    },\n",
    "    {\n",
    "        'title':'title2',\n",
    "        'author': 'author2',\n",
    "        'genre': 'genre2'},\n",
    "    {\n",
    "        'title':'title3',\n",
    "        'author': 'author3',\n",
    "        'genre': 'genre3'}\n",
    "]\n",
    "i = 0\n",
    "for book in books:\n",
    "    while i < len(books):\n",
    "        print(books[i])\n",
    "        i += 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1c85d2b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Request a genre:genre2\n",
      "{user_input}: {title}\n"
     ]
    }
   ],
   "source": [
    "user_input = input('Request a genre:')\n",
    "for i in books:\n",
    "    title =i['title']\n",
    "    if i['genre'] == user_input:\n",
    "        print ('{user_input}: {title}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "518aa14b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
