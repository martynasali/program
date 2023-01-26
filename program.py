import os
import configparser


def main():
    settings = get_settings()
    text = read_file(settings)
    result = count(text)
    sort_and_save(result, settings)


def get_settings():
    settings = configparser.ConfigParser()
    settings.read('./settings.ini')
    settings_variables = {
        "sort_by": settings.get('SORT', 'SORT_BY'),
        "input": settings.get('FILE_LOCATION', 'INPUT'),
        "output": settings.get('FILE_LOCATION', 'OUTPUT')
    }
    return settings_variables


def read_file(settings):
    data = []
    if os.path.isfile(settings["input"]):
        text_file = open(settings["input"], "r")
        data = text_file.read()
        text_file.close()
        return data


def count(text):
    result = {}
    for letter in text:
        if letter not in result:
            if not letter.isalpha():
                continue
            result[letter.lower()] = 1
        else:
            result[letter.lower()] += 1
    return result


def sort_and_save(result, settings):
    sorted_result = {}
    if settings["sort_by"] == 'letter':
        # sort by letter
        sorted_result = dict(sorted(result.items()))
    elif settings["sort_by"] == 'count':
        # sort by letter count
        sorted_result = dict(reversed(sorted(result.items(), key=lambda item: item[1])))
    with open(settings["output"], 'w') as f:
        for key, value in sorted_result.items():
            f.write('%s:%s\n' % (key, value))
        f.close()


if __name__ == '__main__':
    main()
