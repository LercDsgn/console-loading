def x():
     for i in range(100):
             print(f"%{i} {'|' * (i//5)}", end="\r")
             import random
             time.sleep(random.random() / 2 if random.random() > 0.2 else 0.8)
