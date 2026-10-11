import time
from tqdm import tqdm

def test_tqdm():
    print("tqdm: Прогрес-бар:")
    for _ in tqdm(range(5), desc="Процес"):
        time.sleep(0.1)