def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }

                cats_info.append(cat_dict)
                
        return cats_info
    
    except FileNotFoundError:
        print(f"Error: File {path} not found")
        return []
    except Exception as e:
        print(f"Error processing file: {e}")
        return []
    
cats_info = get_cats_info("/Users/siangicher/Documents/Projects/homework/goit-pycore-hw-04/goit-pycore-hw-04/hw2/cats.txt")
print(cats_info)
