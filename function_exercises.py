{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "da6c42e4",
   "metadata": {},
   "source": [
    "# Function Exercises"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6222dd3",
   "metadata": {},
   "source": [
    "1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1acd478a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_two(x):\n",
    "    return x in [2, '2']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "68fb2165",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#is_two(2) == True\n",
    "#is_two(1) == True\n",
    "#is_two('2') == True"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6cfec1b1",
   "metadata": {},
   "source": [
    "2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "89b5a542",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_vowel(string):\n",
    "    return string.lower() in ['a','e','i','o','u']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2855e3a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#is_vowel('a') == True\n",
    "#is_vowel('A') == True\n",
    "#is_vowel('B') == True\n",
    "#is_vowel('a') == True"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "955a9421",
   "metadata": {},
   "source": [
    "3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5186467d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_consonant(x): \n",
    "    return not is_vowel(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "ed18d8e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#is_consonant('b') == True\n",
    "#is_consonant('a') == True"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21cd5b76",
   "metadata": {},
   "source": [
    "4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d86a7d13",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cap_the_con(x):\n",
    "    return x.capitalize() if is_consonant(x[0]) else x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a856ab4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cap_the_con('chloe') == 'Chloe'\n",
    "#cap_the_con('allen') == 'Allen'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96099f78",
   "metadata": {},
   "source": [
    "5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f32542f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_tip(tip, bill):\n",
    "    return f\"The amount you should tip is: {tip * bill}.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "55a878cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The amount you should tip is: 5.25.'"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calculate_tip(.15, 35)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "796c4941",
   "metadata": {},
   "source": [
    "6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0dcd4c5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def apply_discount(price, discount):\n",
    "    return f'The price after the discount is: {price - (discount * price)}.'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "17011b29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The price after the discount is: 120.0.'"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apply_discount(200, .40)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5087564d",
   "metadata": {},
   "source": [
    "7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7c52e49f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def handle_commas(num_str):\n",
    "    return float(num_str.replace(',', ''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "dc3c8ff1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "handle_commas('5,,,,000') == 5000"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73b86f5d",
   "metadata": {},
   "source": [
    "8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "daa8bc65",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_letter_grade(grade):\n",
    "    if grade >= 90:\n",
    "        return('A')\n",
    "    elif grade >= 80:\n",
    "        return('B')\n",
    "    elif grade >= 70:\n",
    "        return('C')\n",
    "    elif grade >= 60:\n",
    "        return('D')\n",
    "    else:\n",
    "        return('F')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "e0c20135",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#get_letter_grade(89) == 'A'\n",
    "#get_letter_grade(61) == 'D'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9b46c80",
   "metadata": {},
   "source": [
    "9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b5954ae2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def remove_vowels(vowels):\n",
    "    for i in vowels:\n",
    "        if i in ['a','e','i','o','u']:\n",
    "            return vowels.replace(i,'')\n",
    "    #won't work for multiple vowels becuase return in looop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f2fbed6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'dg'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "remove_vowels('dog')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1699a7a8",
   "metadata": {},
   "source": [
    "10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:\n",
    "    - anything that is not a valid python identifier should be removed\n",
    "    - leading and trailing whitespace should be removed\n",
    "    - everything should be lowercase\n",
    "    - spaces should be replaced with underscores\n",
    "    - for example:\n",
    "        - Name will become name\n",
    "        - First Name will become first_name\n",
    "        - % Completed will become completed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "6f0019a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def normalize_name(not_python):\n",
    "    return not_python.strip('0123456789!@#$%^&*-()+=:;\"\\'<,>.?/|').lower().replace(' ','_')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "84592b35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'c_at_dog'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "normalize_name('1&C at doG')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63f2f307",
   "metadata": {},
   "source": [
    "11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.\n",
    "    - cumulative_sum([1, 1, 1]) returns [1, 2, 3]\n",
    "    - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "65103507",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cumulative_sum(lst):\n",
    "    for i in range(1, len(lst)):\n",
    "        lst[i] = lst[i-1] + lst[i]\n",
    "    return lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "7864ea10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cumulative_sum([1,1,1]) == [1,2,3]\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "370fda3c",
   "metadata": {},
   "source": [
    "#### Additional Exercise"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f018f14",
   "metadata": {},
   "source": [
    "Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc7087fd",
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
