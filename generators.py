import hashlib


def generator_md5(file):
    """
    Принимает путь до файла
    Возвращает md5 хэш строки из файла
    """
    with open(file, 'r') as file:
        for f in file.readlines():
            hash_str = hashlib.md5(f.strip().encode()).hexdigest()
            yield hash_str


if __name__ == '__main__':
    for md5_hash in generator_md5('links.txt'):
        print(md5_hash)
