**Massenger Bot**

This repository contains a Messenger Bot that interacts with Messenger chats using automated responses.

### Installation and Setup

1. **Download the Repository**:
   - Download this repository and extract the files to your computer.

2. **Install Python**:
   - Ensure that Python is installed on your computer.
   - Download Python from the [official Python website](https://www.python.org/) if not already installed.

3. **Install Required Packages**:
   - Open your terminal and run the following commands to install the necessary packages:
     ```bash
     pip install pyppeteer
     pip install pyautogui
     ```

4. **Start Chrome in Debugging Mode**:
   - Use the following command in your terminal to start Chrome with remote debugging enabled:
     ```bash
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
     ```
     - Replace `9222` with your desired port if needed.
     - Log in to [Messenger.com](https://www.messenger.com) using Chrome.

5. **Update Program with Target Messenger URL**:
   - Copy the Messenger chat URL from Chrome (e.g., `https://www.messenger.com/t/<chat-id>`).
   - Paste this URL into the program where the target Messenger URL is specified.

6. **Create or Modify `responses.json`**:
   - Create a `responses.json` file in the same directory as the script.
   - Add your desired questions and answers in the following format:
     ```json
     [
       {
         "question": "Hello",
         "answer": "Hey, what's up?"
       },
       {
         "question": "How are you?",
         "answer": "I'm doing great! How about you?"
       }
     ]
     ```

7. **Run the Program**:
   - Once everything is set up, execute the `main.py` file by running the following command:
     ```bash
     python main.py
     ```

### Notes
- Ensure Chrome is running in debugging mode before starting the program.
- Modify `responses.json` to customize the bot's responses.
- For advanced configurations, update the script as necessary.

Enjoy automating your Messenger conversations!
