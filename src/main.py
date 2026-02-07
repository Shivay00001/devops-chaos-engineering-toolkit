import argparse
from src.chaos_agent import ChaosAgent

def main():
    parser = argparse.ArgumentParser(description="Chaos Engineering Toolkit")
    parser.add_argument("--fault", choices=["cpu", "memory", "latency", "disk"], required=True, help="Type of fault to inject")
    parser.add_argument("--duration", type=int, default=10, help="Duration of fault in seconds")
    parser.add_argument("--param", type=int, default=0, help="Extra parameter (MB size, cores, or ms lag)")
    
    args = parser.parse_args()
    agent = ChaosAgent()
    
    try:
        if args.fault == "cpu":
            cores = args.param if args.param > 0 else 1
            agent.stress_cpu(args.duration, cores)
        elif args.fault == "memory":
            mb = args.param if args.param > 0 else 500
            agent.consume_memory(args.duration, mb)
        elif args.fault == "latency":
            lag = args.param if args.param > 0 else 200
            agent.simulate_latency(args.duration, lag)
        elif args.fault == "disk":
            mb = args.param if args.param > 0 else 100
            agent.fill_disk(args.duration, mb)
            
    except KeyboardInterrupt:
        print("\n🚫 Chaos Aborted by User.")

if __name__ == "__main__":
    main()
