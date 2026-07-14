import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_time_input():
    print("=" * 40)
    print("       COUNTDOWN TIMER (CLI)")
    print("=" * 40)
    while True:
        try:
            mins = int(input("  Enter Minutes : "))
            secs = int(input("  Enter Seconds : "))
            if mins < 0 or secs < 0 or secs > 59:
                print("  Invalid input. Seconds must be 0-59.\n")
                continue
            total = mins * 60 + secs
            if total == 0:
                print("  Time must be greater than 0.\n")
                continue
            return total
        except ValueError:
            print("  Please enter valid numbers.\n")

def countdown(total_seconds):
    clear_screen()
    remaining = total_seconds
    try:
        while remaining >= 0:
            mins, secs = divmod(remaining, 60)
            hrs, mins = divmod(mins, 60)

            if hrs > 0:
                timer_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"
            else:
                timer_str = f"{mins:02d}:{secs:02d}"

            clear_screen()
            print("=" * 40)
            print("       COUNTDOWN TIMER (CLI)")
            print("=" * 40)
            print()
            print(f"         {timer_str}")
            print()
            print("-" * 40)
            print("  Press Ctrl+C to stop")
            print("=" * 40)

            if remaining == 0:
                break

            time.sleep(1)
            remaining -= 1

        print()
        print("  *** TIME'S UP! ***")
        print()

    except KeyboardInterrupt:
        print()
        print("  Timer stopped.")
        print()

def main():
    total = get_time_input()
    countdown(total)

if __name__ == "__main__":
    main()
