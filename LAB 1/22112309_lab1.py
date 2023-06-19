
def open_dataset():
    file = open('/content/bank.csv', 'r')
    data = file.readlines()
    return data

def headers(data):
    headers = data[0].strip().split(';')
    print("Headers in the file:")
    for header in headers:
        print(header)

headers(dataset)

def count_of_customers_by_marital_category(data):
    marital_counts = {}
    for line in data[1:]:
        customer = line.strip().split(';')
        marital = customer[2]
        if marital in marital_counts:
            marital_counts[marital] += 1
        else:
            marital_counts[marital] = 1
    print("Count of each marital category:")
    for marital, count in marital_counts.items():
        print(f"{marital}: {count}")

marital_category(dataset)

def age_histogram(data):
    ages = []
    for line in data[1:]:
        customer = line.strip().split(';')
        age = int(customer[0])
        ages.append(age)

    age_classes = {}
    for age in ages:
        age_class = age // 10 * 10
        if age_class in age_classes:
            age_classes[age_class] += 1
        else:
            age_classes[age_class] = 1

    print("Histogram for age:")
    for age_class, count in age_classes.items():
        print(f"{age_class}-{age_class + 9}: {'|' * count}")

age_histogram(dataset)