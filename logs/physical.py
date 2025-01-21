#file read and write and foler create function 
import logging
import time
import sys
import os
from datetime import datetime




def log_action(action=None, process_name=None, process_type=None, log_type='console'):
    handlers = []
    if log_type in ['file', 'both']:
        file_handler = logging.FileHandler('ophelia_log.txt')
        handlers.append(file_handler)
    if log_type in ['console', 'both']:
        console_handler = logging.StreamHandler()
        handlers.append(console_handler)

    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    if action:
        logging.info(action)
    if process_name and process_type:
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{start_time}: {process_name} : {process_type}")




#NOte down function 
def note_down_emily():
    log_action("Note taking function start")
    notes = []
    print("Start noting down. Type 'end' when finished.")
    
    while True:
      line = input("> ")
      if line.lower() == 'end':
        break
      notes.append(line)

    if notes:
      filename = input("Enter filename to save the note (e.g., ophelia_notes.txt): ")
      with open(filename, 'a') as f:
        for note in notes:
          f.write(note + '\n')
      print(f"Notes saved to {filename}")
      log_action("Note save into {filename}", "Log file save", "True")
    else:
      print("No notes were taken.")
      log_action("Log file not save!")
      
      
def loading(duration=6):
    loading_chars = ['|', '/', '-', '\\']
    loading_message = "Loading.."
    
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for char in loading_chars:
            sys.stdout.write(f"\r{loading_message} {char}")
            sys.stdout.flush()
            time.sleep(0.2)  
    sys.stdout.write(f"\r{loading_message} - Done!            \n")
    sys.stdout.flush()
  

def type_animation(message, duration=3):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    print()
    time.sleep(duration)
    sys.stdout.write("\r" + " " * len(message) + "\r")
    sys.stdout.flush()

def type_text():
    message = """Welcome to the Assistant bot!
Type 'exit' to end the bot 
If you want to know the usage, you can type 'help'"""
    
    type_animation(message, duration=3)
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    
