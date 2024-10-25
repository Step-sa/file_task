if __name__ == "__main__":
    names = [(str(i + 1) + ".txt") for i in range(3)]
    sorted_files = []
    to_close = []
    for name in names:
        file = open(name, encoding="UTF-8")
        sorted_files.append((name, file.readlines()))
        to_close.append(file)
    sorted_files.sort(key=lambda x: len(x[1]))

    result = open("result.txt", "a")

    for file in sorted_files:
        result.write(file[0] + "\n")
        result.write(str(len(file[1])) + "\n")
        result.writelines(file[1])

    result.close()

    for file in to_close:
        file.close()
