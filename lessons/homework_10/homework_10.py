# ЗАДАНИЕ 1: Распаковка списка и слияние
statuses = ["queued", "running", "testing", "deploy", "done"]

# 1
first, *middle, last = statuses
print(first, middle, last)

# 2
new_list = [*middle, "failed", "skipped"]
print(new_list)

# 3
print(first)
print(last)
print(new_list)

# ЗАДАНИЕ 2: Словарь, слияние и вызов функции

browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}


def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


# 1
config = {**browser, **options}

# 2
result = start_session(**config)

# 3
print(config)
print(result)
