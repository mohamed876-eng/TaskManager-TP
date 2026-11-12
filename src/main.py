def main():
    print("Bienvenue dans TaskManager")
    task = add_task("Apprendre Git")
    print(task)

def add_task(title):
    return {"title": title, "completed": False}


  
if __name__ == "__main__":
    main()