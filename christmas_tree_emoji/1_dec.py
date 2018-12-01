# read input
def read_file_as_int(filename):
    url = "../input/"+filename
    return [int(i) for i in open(url, "r")]

# DAY ONE
# 1
def dec_1_1():
    lines = read_file_as_int("input_1.txt");
    number = 0;

    for freq in lines:
        number += freq;
    return number;

def dec_1_2():
    lines = read_file_as_int("input_1.txt");
    number = 0;
    prev_numbers=set([0]);

    while True:
        for freq in lines:
            number+=freq
            if number in prev_numbers:
                return number;
            prev_numbers.add(number);
    return "didn't work out";



print dec_1_1();
print dec_1_2();
