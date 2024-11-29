
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

    def count(file_contents):
        count = len(file_contents.split())
        return count
    count = count(file_contents)

    def freq(file):
        my_dict = {}
        lowered_file = file.lower()
        for word in lowered_file:
            if word in my_dict:
                my_dict[word]+=1
            else:
                my_dict[word] = 1
        return my_dict
    frequency = freq(file_contents)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print (f"{count} words found in the document")
    for item,value in sorted_frequency:
        print(f"'{item}' character was found {value} times")
    print("--- End report ---")

    

main()