def sort_files(names: list[str]):
    sorted_files = []
    to_close = []
    for name in names:
        file = open(name, encoding="UTF-8")
        sorted_files.append((name, file.readlines()))
        to_close.append(file)
    sorted_files.sort(key=lambda x: len(x[1]))
    for file in to_close:
        file.close()
    return sorted_files


def write_files_to_file(path: str, files: list):
    result = open(path, "a")

    for file in files:
        result.write(file[0] + "\n")
        result.write(str(len(file[1])) + "\n")
        result.writelines(file[1])

    result.close()


if __name__ == "__main__":
    names = [(str(i + 1) + ".txt") for i in range(3)]
    write_files_to_file("result.txt", sort_files(names))
