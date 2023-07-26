# host checker Bot CODED by TARIUS BLAKE

# echoeyes - telegram @tariusblake1 

# echoeyes - github @  https://github.com/tariusblake1 
import os
import concurrent.futures
import subprocess

# ... (rest of the code remains the same)

def ping_host(url):
    count = f"{cyan}~"
    try:
        result = subprocess.run(["ping", "-c", "1", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "1 packets transmitted, 1 received" in result.stdout:
            print(count, f"{green}[Ping success] {blue}[{url}]{white}")
        else:
            print(count, f"{red}[Ping failed][{url}]{white}")
    except Exception as e:
        print(count, f"{red}[N/A][{url}]{white} - Error: {e}")

# ... (rest of the code remains the same)

intro = f"""{red} 
# ... (rest of the intro remains the same)
"""

with open("hosts.txt", "r") as f:
    list_of = f.readlines()
    hosts = [host.strip() for host in list_of]
    
    print(intro)
    
    choice = input("choose the index of the server: ")
    
    try:
        if choice == "1": 
            print(f"{blue}you selected {green}Cloudflare{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(cloudflare, hosts)
        elif choice == "2":
            print(f"{blue}you selected {green}Cloudfront{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(cloudfront, hosts)
        elif choice == "3":
            print(f"{blue}you selected {green}Apache{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(apache, hosts)
        elif choice == "4":
            print(f"{blue}you selected {green}HAProxy{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(haproxy, hosts)
        elif choice == "5":
            print(f"{blue}you selected {green}Nginx{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(nginx, hosts)
        elif choice == "6":
            print(f"{blue}you selected {green}Ping Test{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(ping_host, hosts)
        else:
            print("invalid input")
            
    except KeyboardInterrupt:
        sys.exit("This could cause an Error, Try CTRL+C...")

        
