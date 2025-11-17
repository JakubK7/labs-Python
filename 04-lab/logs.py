import sys

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

def filter_logs(generator, level):
    for line in generator:
        if level in line:
            yield line

def count_statistics(generator):
    stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in generator:
        if "INFO" in line:
            stats["INFO"] += 1
        if "WARNING" in line:
            stats["WARNING"] += 1
        if "ERROR" in line:
            stats["ERROR"] += 1
    
    yield stats

def main():
    if len(sys.argv) != 3:
        print("Usage: python logs.py <file_name> <log_level>")
        print("Example: python logs.py log.txt ERROR")
        sys.exit(1)
    file_name = sys.argv[1]
    log_level = sys.argv[2].upper()

    print(f"Lines containing the level {log_level} :\n")
    lines_gen = read_lines(file_name)
    filtered_gen = filter_logs(lines_gen, log_level)
    for line in filtered_gen:
        print(line)
    

    print("\nLog statistics:\n")
    all_lines_gen = read_lines(file_name)
    stats_generator = count_statistics(all_lines_gen)
    statistics = next(stats_generator)
    for level, count in statistics.items():
        print(f"{level}: {count}")

    # Memory usage comparison
    print("\nMemory usage comparison:")

    # Load everything into a list
    full_list = [line.strip() for line in open(file_name, encoding='utf-8')]
    print(f"List in memory :  {sys.getsizeof(full_list):,} bytes")
    print(f"  + size of all strings indside!")

    gen = read_lines(file_name)
    # Generator lazy
    print(f"Generator object : {sys.getsizeof(gen):,} bytes")  
    print("\nConclusion: The generator reads only one line at a time")
    print(" so even a 1GB log file uses just a few hundred bytes of RAM")

if __name__ == "__main__":      
    main()