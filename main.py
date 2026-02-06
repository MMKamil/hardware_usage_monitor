import time
import psutil
from database import init_db, save_session, save_usage_log
from datetime import datetime


def run_monitor():
    init_db()

    cpu_samples = []
    ram_samples = []

    start_ts = time.time()
    start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Monitorowanie CPU / RAM")
    print("Log co sekundę | Ctrl+C aby zakończyć\n")

    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            save_usage_log(ts, cpu, ram)

            cpu_samples.append(cpu)
            ram_samples.append(ram)

            elapsed = int(time.time() - start_ts)
            print(f"{ts}: {elapsed:>4}s | CPU: {cpu:>5.1f}% | RAM: {ram:5.1f}%")

    except KeyboardInterrupt:
        end_ts = time.time()
        end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        duration = end_ts - start_ts

        avg_cpu = sum(cpu_samples) / len(cpu_samples)
        avg_ram = sum(ram_samples) / len(ram_samples)

        save_session(
            start_str,
            end_str,
            duration,
            avg_cpu,
            avg_ram
        )

        print("\nZatrzymano monitorowanie.")
        print(f"Czas trwania: {int(duration)} s")
        print(f"Średnie CPU:  {avg_cpu:.1f}%")
        print(f"Średnie RAM:  {avg_ram:.1f}%")
        print("Zapisano dane do SQLite.")

if __name__ == "__main__":
    run_monitor()
