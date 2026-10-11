from ext_requests import test_requests
from ext_colorama import test_colorama
from ext_pandas import test_pandas
from ext_numpy import test_numpy
from ext_bs4 import test_bs4
from ext_pillow import test_pillow
from ext_matplotlib import test_matplotlib
from ext_sympy import test_sympy
from ext_jinja2 import test_jinja2
from ext_tqdm import test_tqdm

from std_math import test_math
from std_random import test_random
from std_datetime import test_datetime
from std_json import test_json
from std_os import test_os


def main():
    print("=== ПОЧАТОК ВИКОНАННЯ ЛАБОРАТОРНОЇ РОБОТИ №4 ===\n")

    print("[Сторонні бібліотеки]")
    test_requests()
    test_colorama()
    test_pandas()
    test_numpy()
    test_bs4()
    test_pillow()
    test_matplotlib()
    test_sympy()
    test_jinja2()
    test_tqdm()

    print("\n[Вбудовані бібліотеки]")
    test_math()
    test_random()
    test_datetime()
    test_json()
    test_os()

    print("\n=== ВСІ ФУНКЦІЇ УСПІШНО ВИКОНАНО ===")


if __name__ == "__main__":
    main()