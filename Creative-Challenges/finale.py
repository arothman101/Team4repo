import random, datetime, os, time, pygame

pygame.font.init()

WIDTH = 1500
HEIGHT = 700
FONT = pygame.font.SysFont("Courier", 25)
largefont = pygame.font.SysFont("Courier", 60)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Search")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def getDistances(distances, weights, vectors, word, x_index, y_index, grid):
    for index, vector in enumerate(vectors):
        weight = 0
        distance = 0
        current_coordinate = x_index, y_index
        for x in range(len(word)):
            if ((current_coordinate[0] < 0 or current_coordinate[0] > 9) \
              or (current_coordinate[1] < 0 or current_coordinate[1] > 9)) or distance > len(word):
                break
            try:
                if grid[current_coordinate[1]][current_coordinate[0]] == word[distance]:
                    if vector in [(1,1), (-1,1), (-1,-1), (1,1)]:
                        weight += 10
                    else:
                        weight += 5
                elif grid[current_coordinate[1]][current_coordinate[0]] == "-":
                    if vector in [(1,1), (-1,1), (-1,-1), (1,1)]:
                        weight += 2
                    else:
                        weight += 1
                else:
                    weight = -1
                    break
            except IndexError:
                weight = -1
                break

            current_coordinate = [current_coordinate[0] + vector[0], current_coordinate[1] + vector[1]]
            distance += 1
        if len(word) > distance:
            distance = -1
        distances[index] = distance
        weights[index] = weight
    return distances, weights

def getBestVector(grid, word, x_index, y_index):
    best_vector = []
    distances = [0] * 8
    weights = [0] * 8
    vectors = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1, 1)]
    distances, weights = getDistances(distances, weights, vectors, word, x_index, y_index, grid)
    max_dist = max(weights)
    if max_dist == -1:
        return (0, 0), distances
    for index in range(len(weights)):
        if weights[index] == max_dist and len(word) <= distances[index]:
            best_vector.append(vectors[index])
    if len(best_vector) > 0:
        return random.choice(best_vector), distances
    else:
        return (0, 0), distances

def getaStart(points, grid, word, coords_checked):
    options = []
    for y_index in range(len(grid)):
        for x_index in range(len(grid[y_index])):
            if (x_index, y_index) in coords_checked:
                continue
            if points[y_index][x_index] >= len(word) and (grid[y_index][x_index] == "-" or grid[y_index][x_index] == word[0]):
                options.append((x_index, y_index))
    start = random.choice(options)
    vector, distances = getBestVector(grid, word, start[0], start[1])
    coords_checked.append((start[0], start[1]))
    if vector == (0, 0) or distances == [-1] * 8:
        vector, coords_checked, x_index, y_index = getaStart(points, grid, word, coords_checked)
        return vector, coords_checked, x_index, y_index
    return vector, coords_checked, start[0], start[1]
            
    
def create_word_search():
    try:
        os.path.isfile("words.txt")
    except:
        print("File words.txt cannot be found, ending the game")
        exit()
    grid = [["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"],
            ["-","-","-","-","-","-","-","-","-","-"]]
    points = [[10,10,10,10,10,10,10,10,10,10],
              [10,9,9,9,9,9,9,9,9,10],
              [10,9,8,8,8,8,8,8,9,10],
              [10,9,8,7,7,7,7,8,9,10],
              [10,9,8,7,6,6,7,8,9,10],
              [10,9,8,7,6,6,7,8,9,10],
              [10,9,8,7,7,7,7,8,9,10],
              [10,9,8,8,8,8,8,8,9,10],
              [10,9,9,9,9,9,9,9,9,10],
              [10,10,10,10,10,10,10,10,10,10]]
    chosen_words = []
    candidates = []
    words = []
    answers = []
    with open("words.txt", mode = "r", encoding = "utf-8") as myFile:
        for word in myFile:
            if len(word.strip("\n")) <= 10:
                words.append(word.strip("\n").lower())
    myFile.close()
    for x in range(10):
        chosen_word = random.choice(words)
##        while len(chosen_word) > 6 and max_length == 3:
##            chosen_word = random.choice(words)
        while chosen_word in candidates:## or len(chosen_word) < 3 or len(chosen_word) > 10:
            chosen_word = random.choice(words)
##        if len(chosen_word) > 6:
##            max_length +=1
        candidates.append(chosen_word)
    candidates.sort(key = len, reverse = True)
    for word in candidates:
        chosen_words.append([word, False, 0])
    duplicate_grid = grid
    for word in candidates:
        coords_checked = []
        vector, coords_checked, x_index, y_index = getaStart(points, duplicate_grid, word, coords_checked)
        start = (x_index, y_index)
        duplicate_grid[y_index][x_index] = word[0]
        for index in range(len(word)):
            if index == 0:
                continue
            x_index += vector[0]
            y_index += vector[1]
            duplicate_grid[y_index][x_index] = word[index]
        end = (x_index, y_index)
        answers.append([word, start, end])
        grid = duplicate_grid
    for y_index in range(len(grid)):
        for x_index in range(len(grid[y_index])):
            if grid[y_index][x_index] == "-":
                grid[y_index][x_index] = random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "a", "e", "i", "o", "u"])
    return grid, words, chosen_words, answers

def display_input(guesses, grid, chosen_words, answers, index):
    if index == 0:
        colours = (RED, WHITE)
    else:
        colours = (WHITE, RED)
    surf = FONT.render("Enter the start coordinate: " + guesses[0], True, colours[0])
    rect = surf.get_rect()
    rect.center = (1100, 200)
    win.blit(surf, rect)
    surf = FONT.render("Enter the end coordinate: " + guesses[1], True, colours[1])
    rect = surf.get_rect()
    rect.center = (1100, 400)
    win.blit(surf, rect)
    detectKeywords(guesses[0], grid, chosen_words, answers)
    detectKeywords(guesses[1], grid, chosen_words, answers)
    if index == 2:
        start_coordinate = (int(guesses[0].split(" ")[0]), int(guesses[0].split(" ")[1]))
        end_coordinate = (int(guesses[1].split(" ")[0]), int(guesses[1].split(" ")[1]))
        x_difference = int(end_coordinate[0]) - int(start_coordinate[0])
        y_difference = int(end_coordinate[1]) - int(start_coordinate[1])
        if (abs(x_difference) != abs(y_difference) and not (x_difference == 0 and y_difference) and not (y_difference == 0 and x_difference)) \
              or int(start_coordinate[0]) > 9 or int(start_coordinate[0]) < 0 or int(start_coordinate[1]) > 9 or int(start_coordinate[1]) < 0 \
              or int(end_coordinate[0]) > 9 or int(end_coordinate[0]) < 0 or int(end_coordinate[1]) > 9 or int(end_coordinate[1]) < 0:
            return False
    return True

def check_answer(grid, words, chosen_words, answers, guesses):
    print("")
    start_coordinate = (int(guesses[0].split(" ")[0]), int(guesses[0].split(" ")[1]))
    end_coordinate = (int(guesses[1].split(" ")[0]), int(guesses[1].split(" ")[1]))
    x_difference = int(end_coordinate[0]) - int(start_coordinate[0])
    y_difference = int(end_coordinate[1]) - int(start_coordinate[1])
    x_coord_increment = y_coord_increment = 0
    if y_difference > 0:
        y_coord_increment = 1
    elif y_difference < 0:
        y_coord_increment = -1
    if x_difference > 0:
        x_coord_increment = 1
    elif x_difference < 0:
        x_coord_increment = -1
    characters = ""
    current_coordinate = start_coordinate
    while (current_coordinate[0], current_coordinate[1]) != (end_coordinate[0], end_coordinate[1]):
        characters += grid[current_coordinate[1]][current_coordinate[0]]
        current_coordinate = [current_coordinate[0] + x_coord_increment, current_coordinate[1] + y_coord_increment]
    characters += grid[end_coordinate[1]][end_coordinate[0]]
    found = False
    for index in range(len(chosen_words)):
        if characters in chosen_words[index]:
            if not chosen_words[index][1]:
                chosen_words[index][1] = True
                chosen_words[index][2] = datetime.datetime.now() - start_time
                print("Well done you have found a new word")
                found = True
                break
            else:
                print("You have already found this word")
                break
            
    if characters.lower() in words:
        if not found:
            print("This word is not what I am looking for but it does exist in the dictionary")
    else:
        print("This word does not exist in the dictionary")
    return chosen_words, answers

def detectKeywords(userinput, grid, chosen_words, answers):
    if userinput.upper() == "FINISH":
        finish(chosen_words, False, datetime.datetime.now() - start_time)
    elif userinput.upper() == "ANSWERS":
        answer(grid, chosen_words, answers)
    elif userinput.upper() == "AGAIN":
        again()

def answer(grid, chosen_words, answers):
    run = True
    clock = pygame.time.Clock()
    pygame.time.set_timer(1, 5000)
    index = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                run = False
            if event.type == 1:
                index += 1
        win.fill(BLACK)
        answersurf = FONT.render("You have decided to see the answers", True, WHITE)
        answerrect = answersurf.get_rect()
        answerrect.center = (WIDTH//2, 50)
        win.blit(answersurf, answerrect)
        msgsurf = FONT.render(str(chosen_words[index][0].capitalize() + " is from the start coordinate: {} to the end coordinate: {}").format(answers[index][1], answers[index][2]), True, WHITE)
        msgrect = msgsurf.get_rect()
        msgrect.center = (WIDTH//2, 100)
        win.blit(msgsurf, msgrect)
        x_coord_increment = y_coord_increment = 0
        if answers[index][2][1] > answers[index][1][1]:
            y_coord_increment = 1
        elif answers[index][2][1] < answers[index][1][1]:
            y_coord_increment = -1
        if answers[index][2][0] > answers[index][1][0]:
            x_coord_increment = 1
        elif answers[index][2][0] < answers[index][1][0]:
            x_coord_increment = -1
        current_coordinate = [answers[index][1][0], answers[index][1][1]]
        path = []
        while current_coordinate != [answers[index][2][0], answers[index][2][1]]:
            path.append(current_coordinate)
            current_coordinate = [current_coordinate[0] + x_coord_increment, current_coordinate[1] + y_coord_increment]

        path.append(answers[index][2])
        
        index_identifier = "  "
        for num in range(10):
            index_identifier += str(num) + " "
        index_identifier += " "
        surf = FONT.render(index_identifier, True, WHITE)
        rect = surf.get_rect()
        rect.center = (WIDTH//2, 150)
        win.blit(surf, rect)
        value = 0
        for y_index, row in enumerate(grid):
            display_row = str(value) + " "
            for x_index, letter in enumerate(row):
                if [x_index, y_index] in path:
                    display_row += str(grid[y_index][x_index]).upper() + " "
                else:
                    display_row += "- "
            display_row += " "
            surf = FONT.render(display_row, True, WHITE)
            rect = surf.get_rect()
            rect.center = (WIDTH//2, 200 + (value * 50))
            win.blit(surf, rect)
            value += 1
        pygame.display.update()
        clock.tick()
    pygame.quit()
    exit()

def again():
    print("You have decided to play again")
    main()

def finish(chosen_words, done, finish_time):
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        clock.tick(60)
        win.fill(BLACK)
        if not done:
            endsurf = FONT.render("You have decided to end the game", True, WHITE)
        else:
            if finish_time.total_seconds() < 300:
                endsurf = FONT.render("You have finished this game", True, WHITE)
            else:
                endsurf = FONT.render("You ran out of time", True, WHITE)
        endrect = endsurf.get_rect()
        endrect.center = (WIDTH//2, 50)
        win.blit(endsurf, endrect)
        wordsurf = FONT.render("Here are the words you found", True, WHITE)
        wordrect = wordsurf.get_rect()
        wordrect.center = (WIDTH//2, 100)
        win.blit(wordsurf, wordrect)
        points = 0
        y = 150
        for word in chosen_words:
            if word[1]:
                wordsurf = FONT.render(word[0], True, WHITE)
                wordrect = wordsurf.get_rect()
                wordrect.center = (WIDTH//2, y)
                win.blit(wordsurf, wordrect)
                y += 50
                if word[2].total_seconds() < 300:
                    points += len(word[0])
        if points != 0:
            msgsurf = FONT.render("Well done you got " + str(points) + " points after " + str(datetime.timedelta(seconds=round(finish_time.total_seconds(), 0))), True, WHITE)
            msgrect = msgsurf.get_rect()
            msgrect.center = (WIDTH//2, y)
            win.blit(msgsurf, msgrect)
        else:
            msgsurf = FONT.render("Oh dear you got " + str(points) + " points after " + str(datetime.timedelta(seconds=round(finish_time.total_seconds(), 0))) + " please try again", True, WHITE)
            msgrect = msgsurf.get_rect()
            msgrect.center = (WIDTH//2, y)
            win.blit(msgsurf, msgrect)
        pygame.display.update()
    exit()

def display(grid, chosen_words):
    index_identifier = "  "
    for num in range(10):
        index_identifier += str(num) + " "
    index_identifier += " "
    surf = FONT.render(index_identifier, True, WHITE)
    rect = surf.get_rect()
    rect.center = (200, 100)
    win.blit(surf, rect)
    value = 0
    for row in grid:
        display_row = str(value) + " "
        for letter in row:
            display_row += str(letter.upper()) + " "
        display_row += " "
        surf = FONT.render(display_row, True, WHITE)
        rect = surf.get_rect()
        rect.center = (200, 150 + (value * 50))
        win.blit(surf, rect)
        value += 1
    surf = FONT.render("Words to be found", True, WHITE)
    rect = surf.get_rect()
    rect.center = (650, 100)
    win.blit(surf, rect)
    y = 150
    for chosen_word in chosen_words:
        if chosen_word[1]:
            surf = FONT.render("-" * len(chosen_word[0]), True, WHITE)
            rect = surf.get_rect()
            rect.center = (650, y)
            win.blit(surf, rect)
        else:
            surf = FONT.render((chosen_word[0]), True, WHITE)
            rect = surf.get_rect()
            rect.center = (650, y)
            win.blit(surf, rect)
        y += 50

def checkIfFinished(chosen_words):
    done = False
    words_found = 0
    for chosen_word in chosen_words:
        if chosen_word[1]:
            words_found += 1
    if words_found == 10 or (datetime.datetime.now() - start_time).total_seconds() > 300:
        done = True
    return done

def drawTime():
    timesurf = FONT.render("Time: " + str(datetime.timedelta(seconds=round((datetime.datetime.now() - start_time).total_seconds(), 0))), True, WHITE)
    timerect = timesurf.get_rect()
    timerect.center = (WIDTH//2, 20)
    win.blit(timesurf, timerect)

def menu():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill(BLACK)
        welcomesurf = largefont.render("Click to Play!", True, WHITE)
        welcomerect = welcomesurf.get_rect()
        welcomerect.center = (WIDTH//2, HEIGHT//2)
        win.blit(welcomesurf, welcomerect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

def main():
    try:
        clock = pygame.time.Clock()
        global start_time
        grid, words, chosen_words, answers = create_word_search()
        done = False
        index = 0
        start_time = datetime.datetime.now()
        guesses = ["", ""]
        while not done:
            pygame.display.update()
            win.fill(BLACK)
            condition = display_input(guesses, grid, chosen_words, answers, index)
            if not condition:
                index = 0
                guesses = ["", ""]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        index += 1
                        if index == 2:
                            chosen_words, answers = check_answer(grid, words, chosen_words, answers, guesses)
                            guesses = ["", ""]
                            index = 0
                    elif event.unicode.isnumeric() or event.unicode.isalpha() or event.key == pygame.K_SPACE:
                        guesses[index] += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        guesses[index] = guesses[index][:-1]
            drawTime()
            display(grid, chosen_words)
            done = checkIfFinished(chosen_words)
            clock.tick()
        finish(chosen_words, True, datetime.datetime.now() - start_time)
    except IndexError:
        main()

menu()
                
          
