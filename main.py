import re
print("TASK_1")

def run():
    a, b = input('enter_1:'), input('enter_2: ')
    try:
        a = int(a)
        b = int(b)
        print(a + b)
    except:
        a = str(a)
        b = str(b)
        print(a + b)
        print("you bastard! enter NUMBERS!")
        run()
if __name__ == "__main__":
    run()

print("TASK_2")
sample = 'Exercises number 1, 12, 13 and 345 are important 456'
print(re.findall(r"\d{3}", sample))


print("TASK_3")
food = ["chocolate", 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []
new_list = []
try:
    for x in food:
        fifth.append(x[4])
    print(fifth)
except IndexError:
    print("Not all words contain 5 letters :( But below is the list of 5th letters of those words that contain 5 or more letters: ")
    food_sorted = list(filter(lambda n: len(n) > 5, food))
    new_list = [x[4] for x in food_sorted]
    print(new_list)


print("TASK_4")
colors = '#ABCDFC, BMN, @DFGRTS, #ABGDF'
a = re.findall(r'#[A-Fa-f]{6}', colors)
print(a)



print("TASk_5")
print("Sorry I didnt find a way to solve the task")
text_time = "24:45 or maybe 78:70 or 11:52 and what if 23:59"
data = re.findall(r'^\d[0-2]\d[0-3](:)\d[0-5]\d$', text_time)
print(data)