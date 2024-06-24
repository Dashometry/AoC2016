file = open('inputDay10.txt', 'r')
f = file.readlines()
test = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""".split('\n')

bot_items = {}
bot_instructions = {}
output = {}
target = [17, 61]


def get_instruction(string_list, index):
    value = int(string_list[index])
    if string_list[index - 1] == 'output':
        value *= -1
    return value


def add_bot_items(bot, item):
    if bot in bot_items:
        bot_items[bot].append(item)
    else:
        item_list = [item]
        bot_items[bot] = item_list


def pass_items(bot):
    bot_items[bot].sort()
    if target == bot_items[bot]:
        print(bot)
        print("Michael Skyba")
        exit()
    for i in range(2):
        if bot_instructions[bot][i] < 0:
            output[bot_instructions[bot][i]] = bot_items[bot][i]
        else:
            new_bot = bot_instructions[bot][i]
            add_bot_items(new_bot, bot_items[bot][i])
            if len(bot_items[new_bot]) == 2:
                pass_items(new_bot)


def balance_bots():
    for bot in bot_items:
        if len(bot_items[bot]) == 2:
            pass_items(bot)
            return


for line in f:
    line_contents = line.split(' ')
    if line_contents[0] == 'value':
        bot_num = int(line_contents[5])
        add_bot_items(bot_num, int(line_contents[1]))
    elif line_contents[0] == 'bot':
        bot_instructions[int(line_contents[1])] = (get_instruction(line_contents, 6), get_instruction(line_contents, 11))

#for key in bot_instructions:
#    print(str(key) + ", " + str(bot_instructions[key]))

balance_bots()

print(len(output))
for key in output:
    print(str(key) + ", " + str(output[key]))
