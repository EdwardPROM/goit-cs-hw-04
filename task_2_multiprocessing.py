from multiprocessing import Pool, Manager
import time


def search_keywords_in_file(args):
    file_path, keywords, result_dict = args

    matches = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    matches[keyword] = True
                else:
                    matches[keyword] = False
        result_dict[file_path] = matches
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")


def main_multiprocessing(files, keywords):
    start_time = time.perf_counter()

    with Manager() as manager:
        result_dict = manager.dict()

        args = [(file_path, keywords, result_dict) for file_path in files]

        with Pool(processes=None) as pool:
            pool.map(search_keywords_in_file, args)

        print(
            f"Час виконання за допомогою багатопроцесорного програмування: {time.perf_counter() - start_time: .5f} сек."
        )
        return dict(result_dict)


if __name__ == "__main__":
    files = ["./book_1.txt", "./book_2.txt", "./book_3.txt"]
    keywords = ["Holmes", "Paris", "love"]
    results = main_multiprocessing(files, keywords)
    for result in results:
        print(result, results[result])
