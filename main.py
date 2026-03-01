#!/usr/bin/env python3
import subprocess
import time
from colorama import Fore, Style

def user_interface():
    print("\n<--------------------------------->")
    print(f"{Fore.CYAN}Wi-Fi Monitor{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1. Start Monitoring{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. Stop Monitoring{Style.RESET_ALL}")
    print("<--------------------------------->")
    print(f"{Fore.YELLOW}3. Start Scan{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}4. Targeted Scan{Style.RESET_ALL}\n")
    print(f"{Fore.RED}5. Exit{Style.RESET_ALL}\n")
    return input(f"{Fore.CYAN}Select an option: {Style.RESET_ALL}")

def start_monitoring():
    interface = input(f"{Fore.GREEN}Enter the Wi-Fi interface name (e.g., wlan0): {Style.RESET_ALL}")
    print(f"\n{Fore.GREEN}Starting monitoring on interface {interface}{Style.RESET_ALL}")
    
    try:
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
        print(f"\n{Fore.GREEN}Monitoring started successfully.{Style.RESET_ALL}")
        
    except subprocess.CalledProcessError:
        print(f"\n{Fore.RED}Failed to start monitoring.{Style.RESET_ALL}")

def stop_monitoring():
    interface = input(f"{Fore.GREEN}Enter the Wi-Fi interface name (e.g., wlan0): {Style.RESET_ALL}")
    print(f"{Fore.RED}Stopping monitoring on interface {interface}{Style.RESET_ALL}")
    
    try:
        subprocess.run(["sudo", "airmon-ng", "stop", interface], check=True)
        print(f"{Fore.GREEN}Monitoring stopped successfully.{Style.RESET_ALL}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Failed to stop monitoring.{Style.RESET_ALL}")

def start_scan():
    interface = input(f"{Fore.GREEN}Enter the Wi-Fi interface name (e.g., wlan0): {Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Starting scan on interface {interface}{Style.RESET_ALL}")
    
    try:
        subprocess.run(["sudo", "airodump-ng", interface], check=True)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Scan stopped. Returning to menu...{Style.RESET_ALL}")
        main()
        
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Failed to start scan.{Style.RESET_ALL}")

def target_scan():
    interface = input(f"{Fore.GREEN}Enter the Wi-Fi interface name (e.g., wlan0): {Style.RESET_ALL}")
    
    target_bssid = input(f"{Fore.YELLOW}Enter the target BSSID: {Style.RESET_ALL}")
    target_channel = input(f"{Fore.YELLOW}Enter the target channel: {Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}Starting targeted scan for BSSID {target_bssid} on channel {target_channel}{Style.RESET_ALL}")
    
    try:
        subprocess.run(["sudo", "airodump-ng", "-c", target_channel, "--bssid", target_bssid, interface], check=True)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Targeted scan stopped. Returning to menu...{Style.RESET_ALL}")
        main()
        
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Failed to start targeted scan.{Style.RESET_ALL}")

def main():
    while True:
        choice = user_interface()
        
        if choice == '1':
            start_monitoring()
            
        elif choice == '2':
            stop_monitoring()
            
        elif choice == '3':
            start_scan()
            
        elif choice == '4':
            target_scan()
        
        elif choice == '5':
            print(f"{Fore.RED}Exiting Wi-Fi Monitor.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid option. Please try again.{Style.RESET_ALL}")
            
        time.sleep(1)
        
if __name__ == "__main__":
        main()
        
        
        