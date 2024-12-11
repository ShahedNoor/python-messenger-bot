import asyncio
import json
import pyautogui
import time
from pyppeteer import connect

# Load responses from JSON file
def load_responses_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            responses = json.load(file)
        return responses
    except Exception as e:
        print(f"Error loading responses from file: {e}")
        return []

# Get response based on the question
def get_response(question, responses):
    for entry in responses:
        if entry.get("question", "").strip().lower() == question.strip().lower():
            return entry.get("answer", "")
    return ""  # Return an empty string if no match is found

async def get_existing_tab():
    try:
        # Connect to the remote Chrome instance
        browser = await connect(browserURL='http://localhost:9222', defaultViewport=None)

        # Get all open tabs (pages)
        pages = await browser.pages()
        print(f"Found {len(pages)} tabs open.")

        # Check if any tab has Messenger URL
        desired_url = 'https://www.messenger.com/e2ee/t/25492530650394779'
        target_page = None
        for page in pages:
            print(f"Checking tab with URL: {page.url}")
            if page.url == desired_url:
                target_page = page
                break

        if not target_page:
            print(f"Target tab with URL {desired_url} not found. Make sure it's open.")
            return

        print(f"Connected to tab: {target_page.url}")

        # **Load responses from the JSON file**
        responses = load_responses_from_file("responses.json")  # Change the path if needed

        # Periodically fetch messages
        while True:
            try:
                # Extract message texts from `div[dir="auto"]` elements
                messages = await target_page.evaluate('''() => {
                    const messageElements = document.querySelectorAll('div[dir="auto"]');
                    return Array.from(messageElements).map(msg => msg.innerText).filter(text => text.trim() !== "");
                }''')

                # Print all fetched messages
                print("All Messages:")
                print(json.dumps(messages, indent=4))

                # Check the last message and respond
                if messages:
                    last_message = messages[-1].strip()
                    response = get_response(last_message, responses)
                    if response:
                        respond_with_pyautogui(response)

            except Exception as e:
                print(f"Error fetching messages: {e}")

            await asyncio.sleep(3)  # Poll every 3 seconds

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await browser.disconnect()  # Disconnect when done

def respond_with_pyautogui(response_message):
    """
    Uses pyautogui to type a response and press enter.
    """
    print(f"Responding with: {response_message}")
    time.sleep(1)
    pyautogui.typewrite(response_message)  # Type the message
    time.sleep(3)
    pyautogui.press("enter")  # Press Enter to send

# Use asyncio.run() instead of asyncio.get_event_loop()
asyncio.run(get_existing_tab())
