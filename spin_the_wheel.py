import random
import time
import pyttsx3
import pygame

# Initialize speech engine
engine = pyttsx3.init()

# List of prizes
prizes = [
    "R100 Fuel Voucher",
    "5% Off Next Fill-up",
    "Branded Cap",
    "Try Again",
    "Free Coffee",
    "Free Snacks",
    "Global Oil Keyholder",
    "Better Luck Next Time"
]

# Keywords considered a losing result
losing_keywords = ["Try Again", "Better Luck Next Time"]

# Initialize pygame mixer (only once)
pygame.mixer.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_sound(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing sound: {e}")

def spin_wheel():
    print("\n🎡 Welcome to Global Oil - Spin the Wheel Monthly Competition!")
    input("Press Enter to spin the wheel...")

    print("Spinning", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print("\n🎉 The wheel stopped!")
    prize = random.choice(prizes)

    print(f"🎁 You won: \033[92m{prize}\033[0m")

    # Play appropriate sound and speak
    if prize in losing_keywords:
        play_sound('sounds/aah.mp3')
        speak("Sorry, try again next month!")
    else:
        play_sound('sounds/clap.mp3')
        speak(f"Congratulations! You won {prize}")

if __name__ == "__main__":
    spin_wheel()