from multiprocessing import Process
from gui.landing_page.gui import LandingPage
from gui.client_page.gui import ClientPage
from gui.advisor_page.gui import AdvisorPage
from gui.advisor_analysis.gui import AdvisorAnalysis
from serverside import manager_script
from clientside import client_script
from clientside.client_google_drive import upload_google_drive
from serverside.manager_google_drive import retrieve_google_drive
import os
import threading
from serverside.chatgpt_call import Analysis
from datetime import datetime, timedelta
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.landing_page = LandingPage(self.to_client_page, self.to_advisor_page)
        self.client_page = ClientPage(self.start_stt_client, self.stop_stt_client, self.to_landing_page)
        self.advisor_page = AdvisorPage(self.start_stt_advisor, self.stop_stt_advisor, self.to_advisor_analysis, self.to_landing_page)
        self.advisor_analysis = AdvisorAnalysis(self.to_advisor_page)
        self.current_page = self.landing_page
        self.previous_page = None
        self.manager_process = None
        self.client_process = None


    def to_landing_page(self):
        self.previous_page = self.current_page
        try:
            self.current_page.terminate()
        except:
            pass
        self.current_page = self.landing_page
        self.current_page.run()


    def to_client_page(self):
        self.previous_page = self.current_page
        self.current_page.terminate()
        self.current_page = self.client_page
        self.current_page.run()

    def to_advisor_page(self):
        self.previous_page = self.current_page
        self.current_page.terminate()
        self.current_page = self.advisor_page
        self.current_page.run()

    def to_advisor_analysis(self):
        self.previous_page = self.current_page
        self.current_page.terminate()
        self.current_page = self.advisor_analysis
        self.current_page.run()

    def start_stt_advisor(self):
        if __name__ == "__main__":
            if self.manager_process == None:
                self.manager_process = Process(target=manager_script.run)
                self.manager_process.start()
            else:
                file_path = os.getcwd() + r"\serverside\manager_captions.txt"
                os.chmod(file_path, 0o644)
                file_path = os.getcwd() + r"\serverside\manager_script_file.txt"
                os.chmod(file_path, 0o644)

    def start_stt_client(self):
        if __name__ == "__main__":
            if self.client_process == None:
                self.client_process = Process(target=client_script.run)
                self.client_process.start()
            else:
                file_path = os.getcwd() + r"\clientside\client_captions.txt"
                os.chmod(file_path, 0o644)
                file_path = os.getcwd() + r"\clientside\client_script_file.txt"
                os.chmod(file_path, 0o644)

    def retrieve(self):
        def check_time():
            start_time = datetime.now()
            while True:
                if start_time + timedelta(seconds=15) <= datetime.now():
                    retrieve_google_drive()
                    messagebox.showinfo("Success", "Successfully retrieved client analysis!")
                    break
        threading.Thread(target=check_time).start()

    def stop_stt_advisor(self):
        file_path = os.getcwd() + r"\serverside\manager_captions.txt"
        os.chmod(file_path, 0o000)
        file_path = os.getcwd() + r"\serverside\manager_script_file.txt"
        os.chmod(file_path, 0o000)
        self.retrieve()
        threading.Thread(target=Analysis).start()

            
    def stop_stt_client(self):
        file_path = os.getcwd() + r"\clientside\client_captions.txt"
        os.chmod(file_path, 0o000)
        file_path = os.getcwd() + r"\clientside\client_script_file.txt"
        os.chmod(file_path, 0o000)
        upload_google_drive()

    def run(self):
        self.to_landing_page()
    
if __name__ == "__main__":
    gui = GUI()
    gui.run()