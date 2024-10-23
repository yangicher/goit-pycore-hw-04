from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                salary = float(line.strip().split(',')[1])
                total += salary
                count += 1
        
        average = total / count if count > 0 else 0
        return (total, average)
    
    except FileNotFoundError:
        print(f"Error: File {path} not found")
        return (0, 0)
    except Exception as e:
        print(f"Error processing file: {e}")
        return (0, 0)
    
total, average = total_salary("/Users/siangicher/Documents/Projects/homework/goit-pycore-hw-04/goit-pycore-hw-04/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")