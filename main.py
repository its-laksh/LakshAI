import threading
from wake_word import listen_for_wake_word
from speech_recognition import recognize_speech
from llm_engine import generate_response
from gui import AssistantGUI

class OfflineAssistant:
    def __init__(self):
        self.gui = AssistantGUI(self.process_query)

    def process_query(self, text):
        response = generate_response(text)
        self.gui.display_response(response)

    def start(self):
        print("Assistant started. Say 'Laksh' to activate.")
        
        while True:
            if listen_for_wake_word():
                print("Wake word detected!")
                user_input = recognize_speech()
                if user_input:
                    self.process_query(user_input)

if __name__ == "__main__":
    assistant = OfflineAssistant()
    
    # Run assistant in separate thread
    assistant_thread = threading.Thread(target=assistant.start)
    assistant_thread.daemon = True
    assistant_thread.start()
    
    assistant.gui.run()
