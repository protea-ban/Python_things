from tqdm import tqdm
import random
import time

for i in tqdm(range(10)):
    print('\n', i)
    time.sleep(random.uniform(1, 4))