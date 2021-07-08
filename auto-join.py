import time
import schedule
import webbrowser

def join_session(link):
    webbrowser.open(link)

def join_tutorial_a():
    print("joining tutorial")
    join_session("ZOOM_LINK")

def join_lab_b():
    print("joining lab")
    join_session("ZOOM_LINK")

def join_lec_b():
    print("joining lecture")
    join_session("ZOOM_LINK")

def join_lab_251():
    print("joining lab")
    join_session("ZOOM_LINK")

def main():
    schedule.every().tuesday.at("00:00").do(join_lec_b)
    schedule.every().tuesday.at("00:00").do(join_lab_b)
    schedule.every().thursday.at("00:00").do(join_lec_b)
    schedule.every().thursday.at("00:00").do(join_lab_b)
    schedule.every().saturday.at("00:00").do(join_tutorial_a)
    schedule.every().saturday.at("00:00").do(join_lab_a)

    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
