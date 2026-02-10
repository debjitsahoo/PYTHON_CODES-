n = int(input("Enter range for Cumulative Sum:"))
prev_num = 0

for i in range(n+1):          # Range is taken from 0 to n {by doing n+1}
    sum = prev_num + i
    print(f"Current number {i} Previous number {prev_num} Sum:{sum}")

    prev_num = i              # Update previous number value