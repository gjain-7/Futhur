# Futhur : A career counselling project 
### Cognizance Salesforce Codathon

## About
### Problem statement :
**To solve the multifaceted issue of career choice and the associated harms of an unplanned career**

### Project idea :
A web based application that ranks a set of careers based on the personality of individual and filters them with IQ scores.

### Description of project :
The application is built entirely on python with flask as the host. HTML is used to design the interface of the web-application. A multi-layered _untrained_ neural network (not a neural netowork) is built that takes user input in the form of a MCQ quiz. This quiz's inputs are feeded into the network that is calliberated with predetermined weights that enable the program to give the output in the form of a list. This list contains the professions that are most suitable to the personality of the user. This list is passed through the IQ filter that trims the output list to display only those professions that the user is capable of.

### Built With
- Flask

### Challenges Faced :
The whole project was a great learning experience for the both of us. Some challenges we faced were that we had no idea how to create a gui for our program. We chose flask so that we could deploy it on a browser. We had to use a slight amount of html in the code. For that we managed to learn the barebones of the html syntax. Moreover there we lots of bugs/file handling issue that we encounterd throughout our program. The time crunch was probably the biggest challenge we faced. We have been working non-stop with only nutrition breaks for the last 24 hours. The goal we had set was momentous and we are quite proud of what we could achieve in this short timeframe.


## Getting Started
### Prerequisites
* Python
* Numpy - A Python library
* Flask
***NOTE*** : You might need to change path of the `questions.json` file 

### Installation
- Clone the repo and save it locally
- Run the `main.py` file
- A link `http://localhost:3000` will be generated in the terminal. Open it in any browser

## Usage
 A Screenshot of the Interface :
 ![image](https://user-images.githubusercontent.com/78679552/115129130-be6a1700-a000-11eb-8df7-bd05a651c10c.png)

## License
Distributed under the `GPL -3.0 License`.
