{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "130d9a98",
   "metadata": {},
   "source": [
    "1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:\n",
    "\n",
    "    a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.\n",
    "   \n",
    "    b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.\n",
    "    \n",
    "    c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.\n",
    "\n",
    "Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "83de7606",
   "metadata": {},
   "outputs": [],
   "source": [
    "# b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "37dc9c6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from function_exercises import calculate_tip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1418e6f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The amount you should tip is: 5.25.'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calculate_tip(.15, 35)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "71d0120f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from function_exercises import get_letter_grade as glg"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7ae4468",
   "metadata": {},
   "source": [
    "2. Read about and use the itertools module from the python standard library to help you solve the following problems:\n",
    "\n",
    "- How many different ways can you combine the letters from \"abc\" with the numbers 1, 2, and 3?\n",
    "- How many different combinations are there of 2 letters from \"abcd\"?\n",
    "- How many different permutations are there of 2 letters from \"abcd\"?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "578a492a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from itertools import product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3c9c409a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('a', '1'), ('a', '2'), ('a', '3'), ('b', '1'), ('b', '2'), ('b', '3'), ('c', '1'), ('c', '2'), ('c', '3')]\n",
      "There are 9 possible combinations.\n"
     ]
    }
   ],
   "source": [
    "prod = list(product(\"abc\", \"123\"))\n",
    "x = len(prod)\n",
    "print(prod)\n",
    "print(f'There are {x} different possible combinations.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d0dac4da",
   "metadata": {},
   "outputs": [],
   "source": [
    "from itertools import combinations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b82c51f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]\n",
      "There are 6 different combinations of of 2 letters from abcd.\n"
     ]
    }
   ],
   "source": [
    "combs = list(combinations('abcd', 2))\n",
    "length = len(combs)\n",
    "print(combs)\n",
    "print(f'There are {length} different combinations of of 2 letters from abcd.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "64b87202",
   "metadata": {},
   "outputs": [],
   "source": [
    "from itertools import permutations as p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f5ffc253",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]\n",
      "There are 12 different permutations of 2 letters from abcd.\n"
     ]
    }
   ],
   "source": [
    "combs = list(p('abcd', 2))\n",
    "length = len(combs)\n",
    "print(combs)\n",
    "print(f'There are {length} different permutations of 2 letters from abcd.')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a7a92a6",
   "metadata": {},
   "source": [
    "3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).\n",
    "\n",
    "Use the load function from the json module to open this file.\n",
    "\n",
    "    import json\n",
    "\n",
    "    json.load(open('profiles.json'))\n",
    "\n",
    "Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:\n",
    "\n",
    "- Total number of users\n",
    "- Number of active users\n",
    "- Number of inactive users\n",
    "- Grand total of balances for all users\n",
    "- Average balance per user\n",
    "- User with the lowest balance\n",
    "- User with the highest balance\n",
    "- Most common favorite fruit\n",
    "- Least most common favorite fruit\n",
    "- Total number of unread messages for all users\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9ef44741",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "37f49bf0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'_id': '54e23c3e46ab53a440b580e8',\n",
       "  'index': 0,\n",
       "  'guid': '9962b468-ef3e-4993-b677-617469bc3008',\n",
       "  'isActive': False,\n",
       "  'balance': '$2,097.02',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 39,\n",
       "  'eyeColor': 'blue',\n",
       "  'name': 'Hebert Estes',\n",
       "  'gender': 'male',\n",
       "  'company': 'ANDRYX',\n",
       "  'email': 'hebertestes@andryx.com',\n",
       "  'phone': '+1 (866) 456-2268',\n",
       "  'address': '121 Emmons Avenue, Klondike, Kentucky, 5975',\n",
       "  'about': 'Sit cillum deserunt irure laboris tempor fugiat laboris. Amet commodo amet est incididunt. Dolore qui fugiat cillum pariatur dolore excepteur elit ipsum.\\r\\n',\n",
       "  'registered': '2014-11-10T01:44:03 +06:00',\n",
       "  'latitude': -80.157843,\n",
       "  'longitude': 161.93016,\n",
       "  'tags': ['sit', 'occaecat', 'non', 'ea', 'sit', 'laboris', 'exercitation'],\n",
       "  'friends': [{'id': 0, 'name': 'Tanisha Leonard'},\n",
       "   {'id': 1, 'name': 'Dennis Wilson'},\n",
       "   {'id': 2, 'name': 'Lupe Howe'}],\n",
       "  'greeting': 'Hello, Hebert Estes! You have 4 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3ef5cc0d250968c212',\n",
       "  'index': 1,\n",
       "  'guid': '905f849d-49bf-4a57-b4f3-5d6e4bf1b04c',\n",
       "  'isActive': False,\n",
       "  'balance': '$3,654.02',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 30,\n",
       "  'eyeColor': 'green',\n",
       "  'name': 'Allison Wynn',\n",
       "  'gender': 'male',\n",
       "  'company': 'PHARMACON',\n",
       "  'email': 'allisonwynn@pharmacon.com',\n",
       "  'phone': '+1 (926) 525-3131',\n",
       "  'address': '724 Brevoort Place, Lodoga, Indiana, 3880',\n",
       "  'about': 'Esse quis cillum sunt occaecat ad et eu incididunt aliquip dolor. Adipisicing labore magna anim cillum nisi. Elit mollit consequat velit nulla cillum excepteur elit ullamco deserunt. Anim aliquip Lorem excepteur ad veniam et labore in qui ullamco. Occaecat sit do incididunt voluptate id magna ea amet.\\r\\n',\n",
       "  'registered': '2014-06-10T13:41:26 +05:00',\n",
       "  'latitude': 55.737207,\n",
       "  'longitude': -167.177561,\n",
       "  'tags': ['enim',\n",
       "   'officia',\n",
       "   'laboris',\n",
       "   'irure',\n",
       "   'veniam',\n",
       "   'occaecat',\n",
       "   'pariatur'],\n",
       "  'friends': [{'id': 0, 'name': 'Curry Cox'},\n",
       "   {'id': 1, 'name': 'Alma Dale'},\n",
       "   {'id': 2, 'name': 'Barbara Mayo'}],\n",
       "  'greeting': 'Hello, Allison Wynn! You have 19 unread messages.',\n",
       "  'favoriteFruit': 'apple'},\n",
       " {'_id': '54e23c3e09cc6875638cd36b',\n",
       "  'index': 2,\n",
       "  'guid': '1b042d48-9cfa-4db5-8b60-4104165591c3',\n",
       "  'isActive': True,\n",
       "  'balance': '$1,536.02',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 31,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Jacobs Floyd',\n",
       "  'gender': 'male',\n",
       "  'company': 'QUONK',\n",
       "  'email': 'jacobsfloyd@quonk.com',\n",
       "  'phone': '+1 (853) 537-3315',\n",
       "  'address': '941 Cox Place, Bluffview, Georgia, 5882',\n",
       "  'about': 'Deserunt adipisicing proident exercitation cillum anim consectetur labore exercitation. Commodo reprehenderit laborum enim exercitation. Ullamco nulla culpa aliqua nisi fugiat consectetur deserunt nostrud in eu.\\r\\n',\n",
       "  'registered': '2014-07-30T03:17:32 +05:00',\n",
       "  'latitude': 30.215667,\n",
       "  'longitude': 68.831905,\n",
       "  'tags': ['est', 'aute', 'laborum', 'sint', 'anim', 'sit', 'consectetur'],\n",
       "  'friends': [{'id': 0, 'name': 'Robles Chan'},\n",
       "   {'id': 1, 'name': 'Whitfield Strickland'},\n",
       "   {'id': 2, 'name': 'Lina Melton'}],\n",
       "  'greeting': 'Hello, Jacobs Floyd! You have 5 unread messages.',\n",
       "  'favoriteFruit': 'banana'},\n",
       " {'_id': '54e23c3e54e4094147a3b1da',\n",
       "  'index': 3,\n",
       "  'guid': '69eb3454-8acc-46f1-a636-c6df00dfb542',\n",
       "  'isActive': False,\n",
       "  'balance': '$3,919.64',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 20,\n",
       "  'eyeColor': 'green',\n",
       "  'name': 'Fay Hammond',\n",
       "  'gender': 'female',\n",
       "  'company': 'INRT',\n",
       "  'email': 'fayhammond@inrt.com',\n",
       "  'phone': '+1 (922) 429-2592',\n",
       "  'address': '518 Randolph Street, Whitestone, Arizona, 8189',\n",
       "  'about': 'Aliqua sunt exercitation quis cupidatat fugiat nulla laboris occaecat ut reprehenderit qui incididunt. Amet excepteur qui amet mollit sint enim velit est dolor eu. Velit labore ea aute ipsum consequat culpa cupidatat excepteur aliqua. Sit commodo id est deserunt commodo. Labore sit deserunt enim in dolore incididunt. Officia qui est veniam cillum consequat minim duis Lorem esse magna culpa cupidatat cupidatat enim. Amet eiusmod elit qui reprehenderit commodo quis.\\r\\n',\n",
       "  'registered': '2015-01-30T08:05:38 +06:00',\n",
       "  'latitude': 33.825844,\n",
       "  'longitude': -65.969538,\n",
       "  'tags': ['aliqua', 'esse', 'sint', 'pariatur', 'commodo', 'do', 'anim'],\n",
       "  'friends': [{'id': 0, 'name': 'Dudley Booker'},\n",
       "   {'id': 1, 'name': 'Esmeralda Tyler'},\n",
       "   {'id': 2, 'name': 'Rosa Hampton'}],\n",
       "  'greeting': 'Hello, Fay Hammond! You have 10 unread messages.',\n",
       "  'favoriteFruit': 'banana'},\n",
       " {'_id': '54e23c3e177caf5567ba87ac',\n",
       "  'index': 4,\n",
       "  'guid': '97962c85-7700-4ffa-a01e-2fcbc147fd81',\n",
       "  'isActive': False,\n",
       "  'balance': '$3,681.39',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 39,\n",
       "  'eyeColor': 'green',\n",
       "  'name': 'Chasity Marsh',\n",
       "  'gender': 'female',\n",
       "  'company': 'WAZZU',\n",
       "  'email': 'chasitymarsh@wazzu.com',\n",
       "  'phone': '+1 (976) 425-2362',\n",
       "  'address': '604 Just Court, Eastvale, Federated States Of Micronesia, 8644',\n",
       "  'about': 'Irure excepteur consequat esse qui tempor deserunt nulla fugiat. Ut excepteur do veniam dolore dolor proident sunt voluptate ad ipsum nisi. Lorem proident deserunt Lorem cupidatat dolor nulla qui id aliqua. Et nulla laborum deserunt tempor ad culpa. Ullamco occaecat adipisicing dolore laborum laborum duis aliqua nisi irure ex. Incididunt tempor Lorem quis dolore.\\r\\n',\n",
       "  'registered': '2014-07-31T06:03:19 +05:00',\n",
       "  'latitude': -31.660978,\n",
       "  'longitude': 37.559095,\n",
       "  'tags': ['aliquip', 'duis', 'irure', 'amet', 'aliquip', 'dolore', 'esse'],\n",
       "  'friends': [{'id': 0, 'name': 'Kristina Glover'},\n",
       "   {'id': 1, 'name': 'Ora Christian'},\n",
       "   {'id': 2, 'name': 'Jacklyn Joseph'}],\n",
       "  'greeting': 'Hello, Chasity Marsh! You have 9 unread messages.',\n",
       "  'favoriteFruit': 'apple'},\n",
       " {'_id': '54e23c3eaffbb506aa15ec1c',\n",
       "  'index': 5,\n",
       "  'guid': 'fc3e04d1-44c2-449e-891a-d4f8053d14a4',\n",
       "  'isActive': True,\n",
       "  'balance': '$1,694.42',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 30,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Camacho Cortez',\n",
       "  'gender': 'male',\n",
       "  'company': 'EARTHWAX',\n",
       "  'email': 'camachocortez@earthwax.com',\n",
       "  'phone': '+1 (869) 528-2019',\n",
       "  'address': '101 Haring Street, Nicut, Louisiana, 1473',\n",
       "  'about': 'Qui ad commodo elit voluptate cupidatat exercitation amet ea laborum sunt aliquip nisi irure. Veniam voluptate eiusmod sint aliquip ea. Voluptate voluptate Lorem nulla laborum eiusmod occaecat et nostrud sint in cillum reprehenderit magna nulla. Lorem id fugiat laborum qui mollit amet. Culpa officia ipsum nisi culpa in. Fugiat quis eu cupidatat non culpa in ea velit pariatur non in excepteur.\\r\\n',\n",
       "  'registered': '2014-03-17T12:04:00 +05:00',\n",
       "  'latitude': 74.434627,\n",
       "  'longitude': 69.527088,\n",
       "  'tags': ['et', 'sit', 'in', 'id', 'ullamco', 'elit', 'laborum'],\n",
       "  'friends': [{'id': 0, 'name': 'Sexton Tillman'},\n",
       "   {'id': 1, 'name': 'Boone Steele'},\n",
       "   {'id': 2, 'name': 'Elvia Ward'}],\n",
       "  'greeting': 'Hello, Camacho Cortez! You have 19 unread messages.',\n",
       "  'favoriteFruit': 'apple'},\n",
       " {'_id': '54e23c3e0fd8074c2ca52667',\n",
       "  'index': 6,\n",
       "  'guid': 'af8d9a03-fde9-4039-b20c-c4708d4cfc3c',\n",
       "  'isActive': False,\n",
       "  'balance': '$1,214.10',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 35,\n",
       "  'eyeColor': 'green',\n",
       "  'name': 'Avery Flynn',\n",
       "  'gender': 'male',\n",
       "  'company': 'TERSANKI',\n",
       "  'email': 'averyflynn@tersanki.com',\n",
       "  'phone': '+1 (966) 404-2471',\n",
       "  'address': '569 Oakland Place, Beyerville, Puerto Rico, 2395',\n",
       "  'about': 'Minim consequat anim ad et tempor et pariatur cillum ut. Ea Lorem consectetur sunt aliquip ea minim minim id dolore incididunt qui magna. Magna velit labore dolore voluptate ut aliquip esse qui est ipsum cupidatat duis enim. Sunt esse eiusmod cupidatat duis quis sunt anim dolore adipisicing enim dolore aliqua mollit. Commodo sit ad eiusmod reprehenderit.\\r\\n',\n",
       "  'registered': '2014-04-13T10:25:03 +05:00',\n",
       "  'latitude': -89.879409,\n",
       "  'longitude': 143.441709,\n",
       "  'tags': ['quis',\n",
       "   'esse',\n",
       "   'Lorem',\n",
       "   'minim',\n",
       "   'nostrud',\n",
       "   'voluptate',\n",
       "   'laborum'],\n",
       "  'friends': [{'id': 0, 'name': 'Ball Henson'},\n",
       "   {'id': 1, 'name': 'Dalton Mccoy'},\n",
       "   {'id': 2, 'name': 'Carolina Sharp'}],\n",
       "  'greeting': 'Hello, Avery Flynn! You have 13 unread messages.',\n",
       "  'favoriteFruit': 'banana'},\n",
       " {'_id': '54e23c3eb112d96e4204914d',\n",
       "  'index': 7,\n",
       "  'guid': '95f1c020-f9eb-4a29-b236-e766759d89d0',\n",
       "  'isActive': False,\n",
       "  'balance': '$2,930.31',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 23,\n",
       "  'eyeColor': 'blue',\n",
       "  'name': 'Michael Cash',\n",
       "  'gender': 'male',\n",
       "  'company': 'ORBIXTAR',\n",
       "  'email': 'michaelcash@orbixtar.com',\n",
       "  'phone': '+1 (996) 439-3660',\n",
       "  'address': '808 Duryea Court, Downsville, Northern Mariana Islands, 2154',\n",
       "  'about': 'Minim proident minim consectetur nostrud dolor reprehenderit. Ea est proident non do cillum eu est dolor Lorem id. Tempor enim incididunt consequat voluptate nulla ipsum voluptate id. Incididunt enim laboris nostrud in exercitation est culpa nulla velit.\\r\\n',\n",
       "  'registered': '2014-05-24T17:56:54 +05:00',\n",
       "  'latitude': -86.621367,\n",
       "  'longitude': -4.06197,\n",
       "  'tags': ['eu', 'sit', 'dolore', 'culpa', 'Lorem', 'in', 'esse'],\n",
       "  'friends': [{'id': 0, 'name': 'Rodgers Nolan'},\n",
       "   {'id': 1, 'name': 'Jewel Marks'},\n",
       "   {'id': 2, 'name': 'Sue Mejia'}],\n",
       "  'greeting': 'Hello, Michael Cash! You have 17 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3ef30f14d0e5afddf3',\n",
       "  'index': 8,\n",
       "  'guid': 'bde2d56f-2488-40d0-a7d2-21019ee8a18b',\n",
       "  'isActive': False,\n",
       "  'balance': '$1,944.15',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 25,\n",
       "  'eyeColor': 'green',\n",
       "  'name': 'Madeleine Bray',\n",
       "  'gender': 'female',\n",
       "  'company': 'KIDSTOCK',\n",
       "  'email': 'madeleinebray@kidstock.com',\n",
       "  'phone': '+1 (820) 541-2969',\n",
       "  'address': '684 Stratford Road, Rosine, District Of Columbia, 7177',\n",
       "  'about': 'Ullamco ea esse ullamco commodo quis amet ut ad. Sint eiusmod ullamco minim nostrud amet in ex adipisicing velit cillum Lorem enim nostrud. Deserunt esse incididunt eiusmod commodo ullamco id pariatur tempor duis laboris Lorem. Laboris magna Lorem quis laborum ullamco. Dolor minim magna ut occaecat in consequat consequat in commodo pariatur voluptate pariatur dolore. Quis exercitation cillum labore cillum laborum. Dolore est reprehenderit anim reprehenderit consectetur sit quis ea ut veniam.\\r\\n',\n",
       "  'registered': '2014-08-11T08:54:06 +05:00',\n",
       "  'latitude': 45.118798,\n",
       "  'longitude': -7.698707,\n",
       "  'tags': ['id',\n",
       "   'magna',\n",
       "   'excepteur',\n",
       "   'excepteur',\n",
       "   'excepteur',\n",
       "   'duis',\n",
       "   'excepteur'],\n",
       "  'friends': [{'id': 0, 'name': 'Herrera Doyle'},\n",
       "   {'id': 1, 'name': 'Berger Fisher'},\n",
       "   {'id': 2, 'name': 'Chang Coffey'}],\n",
       "  'greeting': 'Hello, Madeleine Bray! You have 2 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3ebd80e9c26b057fa3',\n",
       "  'index': 9,\n",
       "  'guid': '75991ca5-05ed-499e-bbb5-f057f86d05d7',\n",
       "  'isActive': True,\n",
       "  'balance': '$2,839.22',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 37,\n",
       "  'eyeColor': 'blue',\n",
       "  'name': 'Corine French',\n",
       "  'gender': 'female',\n",
       "  'company': 'INTRAWEAR',\n",
       "  'email': 'corinefrench@intrawear.com',\n",
       "  'phone': '+1 (987) 573-3164',\n",
       "  'address': '964 Clara Street, Snyderville, Oklahoma, 3627',\n",
       "  'about': 'Sint cillum laborum labore duis fugiat voluptate adipisicing. Ad culpa et et ea incididunt nulla excepteur officia. Cillum veniam amet ipsum reprehenderit do eiusmod aliqua aute nisi Lorem consectetur esse in incididunt.\\r\\n',\n",
       "  'registered': '2014-06-25T20:17:13 +05:00',\n",
       "  'latitude': -37.637422,\n",
       "  'longitude': 154.195523,\n",
       "  'tags': ['laboris',\n",
       "   'in',\n",
       "   'dolore',\n",
       "   'mollit',\n",
       "   'velit',\n",
       "   'laboris',\n",
       "   'excepteur'],\n",
       "  'friends': [{'id': 0, 'name': 'Greta Hill'},\n",
       "   {'id': 1, 'name': 'Cline Curry'},\n",
       "   {'id': 2, 'name': 'Branch Sawyer'}],\n",
       "  'greeting': 'Hello, Corine French! You have 18 unread messages.',\n",
       "  'favoriteFruit': 'banana'},\n",
       " {'_id': '54e23c3e6d89c09f5507e7dd',\n",
       "  'index': 10,\n",
       "  'guid': '87cffc18-3acf-40c5-8708-1bb93f1b68de',\n",
       "  'isActive': True,\n",
       "  'balance': '$2,467.31',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 29,\n",
       "  'eyeColor': 'blue',\n",
       "  'name': 'Trudy Cummings',\n",
       "  'gender': 'female',\n",
       "  'company': 'SPLINX',\n",
       "  'email': 'trudycummings@splinx.com',\n",
       "  'phone': '+1 (925) 403-2797',\n",
       "  'address': '558 Charles Place, Tedrow, California, 9832',\n",
       "  'about': 'Non id adipisicing deserunt non magna ex adipisicing sint esse sint. Laborum ea nostrud Lorem voluptate quis proident eu nisi exercitation in. Consequat occaecat proident officia anim.\\r\\n',\n",
       "  'registered': '2014-03-13T17:54:31 +05:00',\n",
       "  'latitude': -36.185131,\n",
       "  'longitude': -37.774906,\n",
       "  'tags': ['aute', 'occaecat', 'ea', 'pariatur', 'consectetur', 'magna', 'ea'],\n",
       "  'friends': [{'id': 0, 'name': 'Amber Gates'},\n",
       "   {'id': 1, 'name': 'Barron Walsh'},\n",
       "   {'id': 2, 'name': 'Nell Bolton'}],\n",
       "  'greeting': 'Hello, Trudy Cummings! You have 2 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3e4192cf53edd67c99',\n",
       "  'index': 11,\n",
       "  'guid': '5a5496f1-a027-4c21-85da-c399234cd9a5',\n",
       "  'isActive': True,\n",
       "  'balance': '$3,304.99',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 21,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Peggy Mayer',\n",
       "  'gender': 'female',\n",
       "  'company': 'ACCUPRINT',\n",
       "  'email': 'peggymayer@accuprint.com',\n",
       "  'phone': '+1 (854) 428-2585',\n",
       "  'address': '830 Willmohr Street, Crenshaw, Missouri, 6032',\n",
       "  'about': 'Aliqua sit enim cillum aliquip ad proident excepteur in consectetur eiusmod. Ipsum sint cillum veniam eiusmod aute sunt et do est tempor. Lorem elit dolor dolore incididunt cillum. Enim occaecat minim sunt cillum est velit cillum deserunt tempor eu.\\r\\n',\n",
       "  'registered': '2014-09-14T07:06:49 +05:00',\n",
       "  'latitude': 48.323912,\n",
       "  'longitude': 22.184821,\n",
       "  'tags': ['commodo', 'esse', 'ad', 'ullamco', 'ea', 'sint', 'ipsum'],\n",
       "  'friends': [{'id': 0, 'name': 'Hopkins Mccall'},\n",
       "   {'id': 1, 'name': 'Nielsen Weeks'},\n",
       "   {'id': 2, 'name': 'Dale Knowles'}],\n",
       "  'greeting': 'Hello, Peggy Mayer! You have 13 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3eedcc65f0ec3a5496',\n",
       "  'index': 12,\n",
       "  'guid': '759a21c4-5f9c-4189-9c50-c9d8a9f31037',\n",
       "  'isActive': False,\n",
       "  'balance': '$3,844.42',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 40,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Chan Hurley',\n",
       "  'gender': 'male',\n",
       "  'company': 'ZEAM',\n",
       "  'email': 'chanhurley@zeam.com',\n",
       "  'phone': '+1 (917) 475-3705',\n",
       "  'address': '915 Channel Avenue, Clinton, North Dakota, 6244',\n",
       "  'about': 'Voluptate exercitation ut anim ex adipisicing ut do officia incididunt fugiat cupidatat aliqua. Cillum ullamco irure dolore est consectetur non consequat. Nulla ullamco eu irure qui dolor magna ipsum id in enim voluptate aute. Officia aliqua dolore ut reprehenderit Lorem cillum. Cillum reprehenderit eu cillum aliqua sint eiusmod cupidatat culpa elit in. Fugiat voluptate reprehenderit amet anim qui nisi velit aliqua proident anim.\\r\\n',\n",
       "  'registered': '2014-03-01T14:51:23 +06:00',\n",
       "  'latitude': 85.901051,\n",
       "  'longitude': -74.986179,\n",
       "  'tags': ['minim', 'veniam', 'sit', 'aute', 'irure', 'non', 'eiusmod'],\n",
       "  'friends': [{'id': 0, 'name': 'Reese Grant'},\n",
       "   {'id': 1, 'name': 'Jenna Kinney'},\n",
       "   {'id': 2, 'name': 'Rhea May'}],\n",
       "  'greeting': 'Hello, Chan Hurley! You have 7 unread messages.',\n",
       "  'favoriteFruit': 'apple'},\n",
       " {'_id': '54e23c3eb813e66c6d33aa82',\n",
       "  'index': 13,\n",
       "  'guid': '6fd14a8e-3158-48eb-a7e1-93fe57b74746',\n",
       "  'isActive': True,\n",
       "  'balance': '$3,594.99',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 40,\n",
       "  'eyeColor': 'blue',\n",
       "  'name': 'Diaz Pena',\n",
       "  'gender': 'male',\n",
       "  'company': 'SUREPLEX',\n",
       "  'email': 'diazpena@sureplex.com',\n",
       "  'phone': '+1 (986) 511-3050',\n",
       "  'address': '184 Kingsway Place, Grantville, Michigan, 2421',\n",
       "  'about': 'Enim elit amet officia consectetur do Lorem reprehenderit cupidatat exercitation velit. Ex tempor esse consectetur dolore aute et. Cupidatat duis nulla in incididunt nulla ullamco non magna officia commodo anim. Labore quis ullamco est deserunt excepteur duis nostrud deserunt cillum proident. Non eiusmod consectetur pariatur deserunt irure quis exercitation ex incididunt quis dolore pariatur sunt irure. Eu do fugiat laboris tempor culpa.\\r\\n',\n",
       "  'registered': '2014-04-19T20:43:12 +05:00',\n",
       "  'latitude': 6.606991,\n",
       "  'longitude': 81.593748,\n",
       "  'tags': ['excepteur',\n",
       "   'elit',\n",
       "   'ullamco',\n",
       "   'excepteur',\n",
       "   'ad',\n",
       "   'quis',\n",
       "   'dolore'],\n",
       "  'friends': [{'id': 0, 'name': 'Mcmillan Knox'},\n",
       "   {'id': 1, 'name': 'Flossie Dixon'},\n",
       "   {'id': 2, 'name': 'Sears Carson'}],\n",
       "  'greeting': 'Hello, Diaz Pena! You have 13 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3e502a2f526b689c3e',\n",
       "  'index': 14,\n",
       "  'guid': '459cc82d-7878-42cb-b9c6-073506380036',\n",
       "  'isActive': True,\n",
       "  'balance': '$2,940.24',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 40,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Heath Castaneda',\n",
       "  'gender': 'male',\n",
       "  'company': 'NETPLODE',\n",
       "  'email': 'heathcastaneda@netplode.com',\n",
       "  'phone': '+1 (944) 478-3741',\n",
       "  'address': '278 Village Road, Sunnyside, Massachusetts, 7496',\n",
       "  'about': 'Consectetur mollit cupidatat ex consectetur eiusmod ut. Cupidatat anim cupidatat cupidatat minim ipsum et quis amet proident pariatur. Do consectetur fugiat quis nisi non. Ut eu consequat consequat in ullamco eiusmod quis cillum sunt dolore anim. Non irure aliqua aliqua enim elit labore consequat.\\r\\n',\n",
       "  'registered': '2014-07-30T21:38:43 +05:00',\n",
       "  'latitude': 69.928876,\n",
       "  'longitude': 33.649878,\n",
       "  'tags': ['elit', 'commodo', 'ut', 'ullamco', 'ullamco', 'velit', 'ullamco'],\n",
       "  'friends': [{'id': 0, 'name': 'Dora Mack'},\n",
       "   {'id': 1, 'name': 'Christensen Camacho'},\n",
       "   {'id': 2, 'name': 'Castro Kelly'}],\n",
       "  'greeting': 'Hello, Heath Castaneda! You have 12 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3e69d22e49c7fe62de',\n",
       "  'index': 15,\n",
       "  'guid': '33d2bbe5-d6f7-4844-88fc-b9f6af63b373',\n",
       "  'isActive': False,\n",
       "  'balance': '$3,062.41',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 38,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Greer Blankenship',\n",
       "  'gender': 'male',\n",
       "  'company': 'QUALITERN',\n",
       "  'email': 'greerblankenship@qualitern.com',\n",
       "  'phone': '+1 (957) 482-3874',\n",
       "  'address': '557 Ingraham Street, Brambleton, South Dakota, 8482',\n",
       "  'about': 'Non in excepteur nostrud consectetur. Qui non consectetur officia incididunt elit laboris exercitation exercitation est minim veniam ullamco dolore. Eu sit aute culpa ex sunt amet. Ut et amet Lorem sunt anim pariatur.\\r\\n',\n",
       "  'registered': '2014-03-30T21:39:41 +05:00',\n",
       "  'latitude': -71.093388,\n",
       "  'longitude': 65.740255,\n",
       "  'tags': ['enim',\n",
       "   'eiusmod',\n",
       "   'Lorem',\n",
       "   'reprehenderit',\n",
       "   'nisi',\n",
       "   'anim',\n",
       "   'sunt'],\n",
       "  'friends': [{'id': 0, 'name': 'Woods Norman'},\n",
       "   {'id': 1, 'name': 'Marilyn Haney'},\n",
       "   {'id': 2, 'name': 'Webster Nielsen'}],\n",
       "  'greeting': 'Hello, Greer Blankenship! You have 7 unread messages.',\n",
       "  'favoriteFruit': 'banana'},\n",
       " {'_id': '54e23c3e42676228c442a669',\n",
       "  'index': 16,\n",
       "  'guid': 'e44604f0-c7a8-4b89-bda3-0f4710ebe28a',\n",
       "  'isActive': False,\n",
       "  'balance': '$3,067.82',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 32,\n",
       "  'eyeColor': 'green',\n",
       "  'name': 'Coffey Hayes',\n",
       "  'gender': 'male',\n",
       "  'company': 'INQUALA',\n",
       "  'email': 'coffeyhayes@inquala.com',\n",
       "  'phone': '+1 (880) 451-3490',\n",
       "  'address': '490 Durland Place, Craig, Tennessee, 5034',\n",
       "  'about': 'Est esse irure Lorem ullamco veniam fugiat laborum veniam excepteur. Ad enim pariatur nostrud excepteur et nostrud velit dolore ex enim cillum in aliquip fugiat. Nulla laborum exercitation irure magna elit laborum magna ad excepteur. Cillum pariatur Lorem eiusmod ad dolore eiusmod veniam do minim laborum in dolor. Reprehenderit elit ad id voluptate Lorem Lorem dolor cupidatat excepteur. Proident minim ea aute nulla.\\r\\n',\n",
       "  'registered': '2014-04-01T23:04:39 +05:00',\n",
       "  'latitude': -30.662644,\n",
       "  'longitude': 59.806684,\n",
       "  'tags': ['duis', 'est', 'in', 'officia', 'nostrud', 'occaecat', 'mollit'],\n",
       "  'friends': [{'id': 0, 'name': 'Suarez Perry'},\n",
       "   {'id': 1, 'name': 'Marlene Sheppard'},\n",
       "   {'id': 2, 'name': 'Cohen Yates'}],\n",
       "  'greeting': 'Hello, Coffey Hayes! You have 19 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'},\n",
       " {'_id': '54e23c3e4ac5969958013235',\n",
       "  'index': 17,\n",
       "  'guid': 'fa7e26df-d239-41e8-9aa9-be5e808b6f89',\n",
       "  'isActive': True,\n",
       "  'balance': '$2,646.76',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 24,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Leanne Hurst',\n",
       "  'gender': 'female',\n",
       "  'company': 'ACCIDENCY',\n",
       "  'email': 'leannehurst@accidency.com',\n",
       "  'phone': '+1 (820) 420-3317',\n",
       "  'address': '196 Columbus Place, Carbonville, New Jersey, 7513',\n",
       "  'about': 'Dolor occaecat dolore ut tempor. Veniam elit anim duis do pariatur. Qui excepteur nisi eiusmod mollit laboris fugiat commodo ipsum reprehenderit labore cillum. Aliquip laborum commodo nisi cupidatat labore nostrud exercitation adipisicing mollit eu magna proident ex Lorem. Nostrud magna sint sint consequat consectetur et sint.\\r\\n',\n",
       "  'registered': '2014-11-10T01:25:55 +06:00',\n",
       "  'latitude': 16.671695,\n",
       "  'longitude': 139.707959,\n",
       "  'tags': ['culpa',\n",
       "   'deserunt',\n",
       "   'tempor',\n",
       "   'quis',\n",
       "   'reprehenderit',\n",
       "   'incididunt',\n",
       "   'est'],\n",
       "  'friends': [{'id': 0, 'name': 'Farley Frank'},\n",
       "   {'id': 1, 'name': 'Pruitt Frye'},\n",
       "   {'id': 2, 'name': 'Simpson Cardenas'}],\n",
       "  'greeting': 'Hello, Leanne Hurst! You have 5 unread messages.',\n",
       "  'favoriteFruit': 'banana'},\n",
       " {'_id': '54e23c3ed945981ba2580614',\n",
       "  'index': 18,\n",
       "  'guid': 'e608dc5c-fee4-4086-971b-3ebd37bfa137',\n",
       "  'isActive': True,\n",
       "  'balance': '$2,227.79',\n",
       "  'picture': 'http://placehold.it/32x32',\n",
       "  'age': 22,\n",
       "  'eyeColor': 'brown',\n",
       "  'name': 'Ewing Larson',\n",
       "  'gender': 'male',\n",
       "  'company': 'ESCENTA',\n",
       "  'email': 'ewinglarson@escenta.com',\n",
       "  'phone': '+1 (943) 439-3760',\n",
       "  'address': '136 Beard Street, Wattsville, New Hampshire, 2803',\n",
       "  'about': 'Veniam eiusmod exercitation culpa mollit reprehenderit ullamco voluptate voluptate irure qui duis anim et. Laborum dolor quis do voluptate. In pariatur dolor id mollit et enim. Qui ex qui in cillum irure enim non reprehenderit irure et excepteur aliquip eu eu.\\r\\n',\n",
       "  'registered': '2014-07-21T19:17:41 +05:00',\n",
       "  'latitude': 15.903555,\n",
       "  'longitude': -159.721203,\n",
       "  'tags': ['Lorem',\n",
       "   'magna',\n",
       "   'dolor',\n",
       "   'aliquip',\n",
       "   'reprehenderit',\n",
       "   'eu',\n",
       "   'voluptate'],\n",
       "  'friends': [{'id': 0, 'name': 'Suzette Huffman'},\n",
       "   {'id': 1, 'name': 'Paige Santiago'},\n",
       "   {'id': 2, 'name': 'Dollie Fernandez'}],\n",
       "  'greeting': 'Hello, Ewing Larson! You have 16 unread messages.',\n",
       "  'favoriteFruit': 'strawberry'}]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "json.load(open('profiles.json'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f52bc184",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"profiles.json\") as file:\n",
    "    profiles_dict = json.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0c3b81e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n"
     ]
    }
   ],
   "source": [
    "# number of users\n",
    "users = len([profile for profile in profiles_dict])\n",
    "print(users)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "ed8d78c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "# number of active users\n",
    "active_users = len([profile for profile in profiles_dict if profile['isActive'] == False])\n",
    "print(active_users)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "84fcd9b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "# number of inactive users\n",
    "inactive_users = len([profile for profile in profiles_dict if profile['isActive'] == False])\n",
    "print(inactive_users)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "65303a2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "52667.02\n"
     ]
    }
   ],
   "source": [
    "# Grand total of balances for all users\n",
    "user_balances = sum([float(profile['balance'].strip('$').replace(',','')) for profile in profiles_dict])\n",
    "print(user_balances)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "f8904fc2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2771.95\n"
     ]
    }
   ],
   "source": [
    "# Average balance per user\n",
    "avg_bal = user_balances / users\n",
    "# print(avg_bal) # need to round \n",
    "print(round(avg_bal,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "39cf0593",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$1,214.10\n"
     ]
    }
   ],
   "source": [
    "# User with the lowest balance\n",
    "lowest_bal = min([profile[\"balance\"] for profile in profiles_dict])\n",
    "print(lowest_bal)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "59259863",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'_id': '54e23c3e0fd8074c2ca52667', 'index': 6, 'guid': 'af8d9a03-fde9-4039-b20c-c4708d4cfc3c', 'isActive': False, 'balance': '$1,214.10', 'picture': 'http://placehold.it/32x32', 'age': 35, 'eyeColor': 'green', 'name': 'Avery Flynn', 'gender': 'male', 'company': 'TERSANKI', 'email': 'averyflynn@tersanki.com', 'phone': '+1 (966) 404-2471', 'address': '569 Oakland Place, Beyerville, Puerto Rico, 2395', 'about': 'Minim consequat anim ad et tempor et pariatur cillum ut. Ea Lorem consectetur sunt aliquip ea minim minim id dolore incididunt qui magna. Magna velit labore dolore voluptate ut aliquip esse qui est ipsum cupidatat duis enim. Sunt esse eiusmod cupidatat duis quis sunt anim dolore adipisicing enim dolore aliqua mollit. Commodo sit ad eiusmod reprehenderit.\\r\\n', 'registered': '2014-04-13T10:25:03 +05:00', 'latitude': -89.879409, 'longitude': 143.441709, 'tags': ['quis', 'esse', 'Lorem', 'minim', 'nostrud', 'voluptate', 'laborum'], 'friends': [{'id': 0, 'name': 'Ball Henson'}, {'id': 1, 'name': 'Dalton Mccoy'}, {'id': 2, 'name': 'Carolina Sharp'}], 'greeting': 'Hello, Avery Flynn! You have 13 unread messages.', 'favoriteFruit': 'banana'}]\n"
     ]
    }
   ],
   "source": [
    "lowest_u_bal = [profile for profile in profiles_dict if profile[\"balance\"] == lowest_bal]\n",
    "print(lowest_u_bal)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "246d1717",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$3,919.64\n"
     ]
    }
   ],
   "source": [
    "# User with the highest balance\n",
    "max_bal = max([profile[\"balance\"] for profile in profiles_dict])\n",
    "print(max_bal)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "ea362d72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'_id': '54e23c3e54e4094147a3b1da', 'index': 3, 'guid': '69eb3454-8acc-46f1-a636-c6df00dfb542', 'isActive': False, 'balance': '$3,919.64', 'picture': 'http://placehold.it/32x32', 'age': 20, 'eyeColor': 'green', 'name': 'Fay Hammond', 'gender': 'female', 'company': 'INRT', 'email': 'fayhammond@inrt.com', 'phone': '+1 (922) 429-2592', 'address': '518 Randolph Street, Whitestone, Arizona, 8189', 'about': 'Aliqua sunt exercitation quis cupidatat fugiat nulla laboris occaecat ut reprehenderit qui incididunt. Amet excepteur qui amet mollit sint enim velit est dolor eu. Velit labore ea aute ipsum consequat culpa cupidatat excepteur aliqua. Sit commodo id est deserunt commodo. Labore sit deserunt enim in dolore incididunt. Officia qui est veniam cillum consequat minim duis Lorem esse magna culpa cupidatat cupidatat enim. Amet eiusmod elit qui reprehenderit commodo quis.\\r\\n', 'registered': '2015-01-30T08:05:38 +06:00', 'latitude': 33.825844, 'longitude': -65.969538, 'tags': ['aliqua', 'esse', 'sint', 'pariatur', 'commodo', 'do', 'anim'], 'friends': [{'id': 0, 'name': 'Dudley Booker'}, {'id': 1, 'name': 'Esmeralda Tyler'}, {'id': 2, 'name': 'Rosa Hampton'}], 'greeting': 'Hello, Fay Hammond! You have 10 unread messages.', 'favoriteFruit': 'banana'}]\n"
     ]
    }
   ],
   "source": [
    "max_u_bal = [profile for profile in profiles_dict if profile[\"balance\"] == max_bal]\n",
    "print(max_u_bal)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "82709d89",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Most common favorite fruit\n",
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "d4c001c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({'strawberry': 9, 'apple': 4, 'banana': 6})"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Counter([profile['favoriteFruit'] for profile in profiles_dict])\n",
    "# favorite = strawberry (9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "00bef95f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({'strawberry': 9, 'apple': 4, 'banana': 6})"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Least most common favorite fruit\n",
    "Counter([profile['favoriteFruit'] for profile in profiles_dict])\n",
    "# least most common favorite = apple (4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "21db3ea5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Hello, Hebert Estes! You have 4 unread messages.', 'Hello, Allison Wynn! You have 19 unread messages.', 'Hello, Jacobs Floyd! You have 5 unread messages.', 'Hello, Fay Hammond! You have 10 unread messages.', 'Hello, Chasity Marsh! You have 9 unread messages.', 'Hello, Camacho Cortez! You have 19 unread messages.', 'Hello, Avery Flynn! You have 13 unread messages.', 'Hello, Michael Cash! You have 17 unread messages.', 'Hello, Madeleine Bray! You have 2 unread messages.', 'Hello, Corine French! You have 18 unread messages.', 'Hello, Trudy Cummings! You have 2 unread messages.', 'Hello, Peggy Mayer! You have 13 unread messages.', 'Hello, Chan Hurley! You have 7 unread messages.', 'Hello, Diaz Pena! You have 13 unread messages.', 'Hello, Heath Castaneda! You have 12 unread messages.', 'Hello, Greer Blankenship! You have 7 unread messages.', 'Hello, Coffey Hayes! You have 19 unread messages.', 'Hello, Leanne Hurst! You have 5 unread messages.', 'Hello, Ewing Larson! You have 16 unread messages.']\n"
     ]
    }
   ],
   "source": [
    "# Total number of unread messages for all users\n",
    "unread_messages = [profile['greeting'] for profile in profiles_dict]\n",
    "print(unread_messages)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "c7c34fe8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "210\n"
     ]
    }
   ],
   "source": [
    "\n",
    "t_unread_messages = []\n",
    "for greeting in unread_messages: \n",
    "    split = greeting.split()\n",
    "    for i in split:\n",
    "        if i.isdigit():\n",
    "            t_unread_messages.append(int(i))\n",
    "print(sum(t_unread_messages))\n",
    "# 210 unread messages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3f41431",
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
