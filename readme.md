<div align="center">
    <h1> PaceBot </h1>
    <img src="./readme_src/project-cover.jpg" alt="Project Cover" width="400">
</div>

## Table of Contents

- [Description](#description)

- [How It Works?](#how-it-works)

- [Technologies Used](#technologies-used)

- [Installation](#installation)

- [Configuration](#configuration)

- [Running the bot](#running-the-bot)

- [Editing the Code](#editing-the-code)
 
- [Warnings](#warnings) 


## Description

PaceBot is an experimental trading bot developed for research purposes. Operating on a 4-stage state machine, this bot dynamically transitions between states according to a specific algorithm. It determines its position based on the current state, enabling it to perceive market direction and make accurate predictions. 

PaceBot serves as a tool for users interested in experimenting with automated strategies for entering "LONG" or "SHORT" positions in the cryptocurrency market, particularly in assets like Bitcoin. With advanced algorithms, it aims to analyze market movements, and make accurate predictions.

<div align="center">
    <img src="./readme_src/description.jpg" alt="Project Cover" width="400">
</div>

## How It Works?
During the Computer Architecture and GPU design lesson, I saw a model which is a 2 bit branch prediction counter. 
In short, this model attempts to make accurate predictions by forecasting branching outcomes based on its current state.
<div align="center">
    <img src="./readme_src/strategy1.png" alt="strategy" width="500">
</div>

You can check out this model more by searching "2 bit branch predictor" on Google.<br>
So, I though that the process of predicting the next branch state and the result of the transaction are similar. And tried to adapt this model on this trading bot.

The operational logic of the bot is as follows:
<div align="center">
    <img src="./readme_src/strategy2.png" alt="strategy" width="500">
</div>


## Technologies Used

1. **Python:** The primary programming language driving PaceBot's functionality and logic.

2. **Binance API:** PaceBot connects seamlessly to the Binance cryptocurrency exchange through its API, allowing real-time access to market data and execution of trades.

3. **TA-Lib Library:** Technical Analysis Library provides essential functions for technical analysis of financial markets, aiding PaceBot in evaluating market indicators.

4. **ChatGPT:** ChatGPT, powered by OpenAI, is employed for code assistance, aiding developers in coding tasks and providing guidance on library usage. Additionally, ChatGPT is utilized for crafting informative log messages, enhancing communication and facilitating a smoother understanding of PaceBot's operations.

<div align="center">
    <p> 
        <a href="https://www.python.org/"> <img src="./readme_src/python-logo.png" width="75" alt="python"> </a>
        <a href="https://github.com/sammchardy/python-binance"> <img src="./readme_src/binance-logo.png" width="75" alt="binanceAPI"> </a>
        <a href="https://pypi.org/project/TA-Lib/"> <img src="./readme_src/talib-logo.png" width="75" alt="TA-lib"> </a>
        <a href="https://chat.openai.com/chat" target="_blank"> <img src="./readme_src/chatgpt-logo.png" width="75" alt="python"> </a>
    </p>
</div>

## Installation

To install Project, follow these simple steps:

1.  **Install Python:**  
	- Visit [Python official website](https://www.python.org/downloads/) and download python. 
	- I strongly recommend downloading a version lower than 3.10 and higher than 3 to ensure that you can download it without any issues and run the Talib library smoothly.
2. **Cloning the Project into your local:**
    Go to the directory where you want to download the project using 'cd', and then type the following command 
    ```bash
    $git clone https://github.com/basaryldrm06/PaceBot
    ```
3. **Install Dependencies**
    Enter these commands in sequence.
    ```bash
    $cd PaceBot
    $pip install -r requirements.txt
    ```
Upon successfully completing these steps, proceed to configure your settings and run the program.

In case you encounter any issues, kindly attempt to resolve them before moving forward.

If you are facing difficulties downloading the Talib library, consider trying a manual download from this [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

## Configuration
Rename the file config2.py to config.py.

Open the config.py file to edit the settings, and fill in the empty fields according to your preferences.

<div align="center">
    <img src="./readme_src/config.png" alt="Config File" width="500">
</div>

If you do not have an api key you can obtain one from this [link](https://www.binance.com/en/my/settings/api-management)

You can use the default values for other sections or customize them based on your preferences.

Once you have finished editing your settings, you will be ready to run the program.

## Running the Bot
If you have completed the previous steps, PaceBot is now ready to run. Start it by entering the following command:

 ```bash
$python main.py
```

After running the command, you should see a screen similar to the one below.

<div align="center">
    <img src="./readme_src/running.png" alt="Running Bot" width="800">
</div>

## Editing the Code
Feel free to tailor the project to your specific preferences and requirements. The code has been meticulously documented to provide clear explanations of each component, empowering you to make effortless customizations. Whether you want to tweak parameters, integrate additional features, or adapt the functionality to suit your needs, the codebase is designed to be intuitive and easily adaptable. 

<div align="center">
    <img src="./readme_src/code.png" alt="Code Example" width="800">
</div>


## Warnings
This trading bot is developed solely for experimental purposes, aiming to explore the viability and effectiveness of automating the trading process by a spesific algorithm. It is a completely experimental project shared as open-source to serve as an example for the development of trading bots.

Any profits or losses incurred using this bot are entirely your responsibility. Please refrain from using the program if you are not familiar with its functionalities. Understand that engaging in financial transactions carries inherent risks, and it's crucial to exercise caution and knowledge when utilizing this bot.

<div align="center">
    <img src="./readme_src/high-risk.jpg" alt="Code Example" width="350">
</div>

## Last Words from Developer
I hope you find this project useful and enjoyable.

Feel free to follow my account for more projects like this and stay updated on upcoming releases. Don't forget to star and watch this project to receive notifications about future updates and improvements.

Algorithmic Trading Bots represent a significant advancement in our era, providing a diverse array of applications within the financial landscape. While engaging in this project, my goal was to explore the capabilities of Algorithmic Trading Bots and their effectiveness in financial transactions. For this reason, this project was particularly intriguing and enjoyable for me.

If you have any innovative ideas in mind for trading bots or AI, feel free to reach out to me through the links on my profile. We can collaborate and develop something together.

Thank you for your interest and support! 🚀

<div align="center">
    <p> 
        <a href="mailto:basaryldrm06@gmail.com?subject=Hello%20basaryldrm06"> <img src="./readme_src/gmail.png" width="60" alt="gmail"> </a>
        <a href="https://www.linkedin.com/in/basaryldrm06/"> <img src="./readme_src/linkedin.png" width="60" alt="linkedin"> </a>
        <a href="https://github.com/basaryldrm06" target="_blank"> <img src="./readme_src/github.png" width="60" alt="github"> </a>
    </p>
</div>