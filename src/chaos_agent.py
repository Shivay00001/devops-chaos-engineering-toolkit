import time
import timeit
import multiprocessing
import os
import psutil

class ChaosAgent:
    def __init__(self):
        pass

    def _cpu_load(self, duration: int):
        """Generates CPU load."""
        end_time = time.time() + duration
        while time.time() < end_time:
            _ = [x * x for x in range(1000)]

    def stress_cpu(self, duration: int, cores: int = 1):
        """Spawns processes to stress CPU."""
        print(f"🔥 Injecting CPU Stress on {cores} cores for {duration}s...")
        processes = []
        for _ in range(cores):
            p = multiprocessing.Process(target=self._cpu_load, args=(duration,))
            p.start()
            processes.append(p)
        
        for p in processes:
            p.join()
        print("✅ CPU Stress Completed.")

    def consume_memory(self, duration: int, size_mb: int = 500):
        """Allocates memory to stress RAM."""
        print(f"🧠 Consuming {size_mb}MB Memory for {duration}s...")
        dummy_buffer = []
        try:
            # Approx 1MB strings
            chunk = "A" * 1024 * 1024
            for _ in range(size_mb):
                dummy_buffer.append(chunk)
            
            time.sleep(duration)
        except MemoryError:
            print("❌ OOM - System ran out of memory!")
        finally:
            del dummy_buffer
            print("✅ Memory Released.")

    def simulate_latency(self, duration: int, lag_ms: int = 200):
        """
        Simulates network latency by sleeping. 
        (Real network lag requires sudo tc commands, mock for safety/portability)
        """
        print(f"🌐 Simulating Network Latency ({lag_ms}ms) for {duration}s...")
        end_time = time.time() + duration
        while time.time() < end_time:
            time.sleep(lag_ms / 1000.0)
            # This just blocks the thread, representing a laggy service call
        print("✅ Latency Simulation Ended.")

    def fill_disk(self, duration: int, size_mb: int = 100):
        """Writes mock files to disk."""
        filename = "chaos_temp_file.dat"
        print(f"💾 Warning: Writing {size_mb}MB to disk...")
        try:
            with open(filename, "wb") as f:
                f.write(os.urandom(size_mb * 1024 * 1024))
            
            time.sleep(duration)
        finally:
            if os.path.exists(filename):
                os.remove(filename)
            print("✅ Disk Cleaned.")
