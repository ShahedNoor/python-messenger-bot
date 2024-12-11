import asyncio
import json
import pyautogui
import time
from pyppeteer import connect

async def get_existing_tab():
    try:
        # Connect to the remote Chrome instance
        browser = await connect(browserURL='http://localhost:9222', defaultViewport=None)
        
        # Get all open tabs (pages)
        pages = await browser.pages()
        print(f"Found {len(pages)} tabs open.")
        
        # Check if any tab has Messenger URL
        # Replace your Massenger url here
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

                # Check the last message and respond if it matches "Hello"
                if messages and messages[-1].strip().lower() == "hello":
                    respond_with_pyautogui("Hey, what's up?")

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