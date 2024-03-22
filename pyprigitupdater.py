import subprocess
import schedule
import time

def run_batch_file_silently(batch_file_path):
    # Run the batch file invisibly
    subprocess.call(["cmd", "/c", batch_file_path], shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

def main():
    # Path to the first batch file
    batch_file_path1 = r"C:\pyDash1\pushOlenPrimary.bat"
    # Path to the second batch file
    batch_file_path2 = r"C:\pyPri\pushOlenPrimary.bat"
    
    # Schedule running the first batch file every 60 seconds
    schedule.every(60).seconds.do(run_batch_file_silently, batch_file_path1)
    # Schedule running the second batch file every 60 seconds
    schedule.every(60).seconds.do(run_batch_file_silently, batch_file_path2)
    
    # Run scheduled tasks indefinitely
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
