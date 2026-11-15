"""2026 recovery improvement: reusable list exercise, no import-time output."""

def build_list():
    values = []
    for value in (10, 20, 30, 40):
        values.append(value)
    values.insert(1, 15)
    values.extend([50, 60, 70])
    values.pop()
    values.sort()
    return values

def main():
    values = build_list()
    print('The index of 30 is:', values.index(30))
    print('Final sorted list:', values)
if __name__ == '__main__':
    main()
