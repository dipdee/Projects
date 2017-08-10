selection = raw_input("Please type easy/ medium/ hard :").lower()

game_settings = {
    'max_question_number': 5,
    'question_number': 1,
    'answer_number': 0,
    'remain_try': 5,
    'no_more_trys': 0
}
data = {
    'easy': {
        'phrase': '''Hello ___1___!'  In ___2___ this is particularly easy;
                    all you have to do is type in: ___3____ "Hello ___1___!"
                    Of course, that isn't a very useful thing to do. However,
                    it is an example of how to output to the user using the
                    ___3___ command, and produces a program which does
                    something, so it is useful in that capacity.It may seem a
                    bit odd to do something in a Turing complete language that
                    can be done even more easily with an ___4___ file in a
                    browser, but it's a step in learning ___2___ syntax, and
                    that's really its purpose.''',
        'answers': ['world', 'Python', 'print', 'HTML'],
    },
    'medium': {
        'phrase': '''___1___ Inc. is an American multinational technology
                    company headquartered in Cupertino, California that
                    designs, develops, and sells consumer electronics,
                    computer software, and online services.
                    The company's hardware products include the iPhone
                    smartphone, the iPad tablet computer, the ___2___ personal
                    computer, the iPod portable media player, the ___1___ Watch
                    smartwatch, and the ___1___ TV digital media player.___1___
                    's consumer software includes the macOS and iOS operating
                    systems, the ___3___ media player, the ___4___ web browser,
                    and the iLife and iWork creativity and productivity suites.
                    Its online services include the ___3___ Store, the iOS App
                    Store and ___2___ App Store, ___1___ Music, and iCloud.''',
        'answers': ['Apple', 'Mac', 'iTunes', 'Safari'],
    },
    'hard': {
        'phrase': '''+++Hard+++Hypertext Markup Language (HTML) is the standard
                    markup language for creating ___1___ pages and ___1___
                    applications.With Cascading Style Sheets (CSS) and ___2___
                    it forms a triad of cornerstone ___3___ for the
                    World Wide Web.[1] Web browsers receive HTML documents from
                    a webserver or from local storage and render them into
                    ___4___ ___1___ pages. HTML describes
                    the structure of a ___1___ page semantically and originally
                    included cues for the appearance of the document.''',
        'answers': ['web', 'JavaScript', 'technologies', 'multimedia']
    },
    'to_be_changed': ['___1___', '___2___', '___3___', '___4___']
}


def find_word(word):
    """
    Behavior: Compare each word to the word in list data['to_be_changed']
    Input: Words from the string
    Output: If the word is in the list, return result and delete the word
    from the list.
    """
    for i in data['to_be_changed']:
        if i in word:
            result = i
            data['to_be_changed'].remove(i)
            return result
    return None


def show_string(string):
    """
    This function shows the string in readable form
    """
    string = " ".join(string)
    print string


def check_replacement(string, user_input):
    """
    Behavior: Compare the word in string matched with the
    word in to_be_changed if so function replaces this word with the user
    input and return the string
    Input: Choosen phrase and user input
    Output: Return phrase with changes
    """
    for word in string:
        replacement = find_word(word)
        if replacement is not None:
            string = [word.replace(replacement, user_input) for word in string]
            # https://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list
            show_string(string)
            return string


def play_game(answers, string):
    """
    Behavior: In this function we make a counter while ,
    get the user_input, if user_input matches with the answer in the list
    we call function check_replacement() and increase counter.
    If the answer is wrong we count the remain tries. When remain tries == 0 ,
    game is ower.
    Input: Choosen string and answers
    Output: Count trys and return result of function check_replacement()
    """
    string = string.split()
    show_string(string)
    while game_settings['question_number'] < game_settings['max_question_number']:
        user_input = raw_input("Please type your answer for ___" + str(game_settings['question_number']) + "___ question: ")
        if user_input == answers[game_settings['answer_number']]:
            string = check_replacement(string, user_input)
            game_settings['question_number'] += 1
            game_settings['answer_number'] += 1
        else:
            print ("Wrong answer, you have " + str(game_settings['remain_try'] - 1) + " more trys")
            game_settings['remain_try'] -= 1
            if game_settings['remain_try'] == game_settings['no_more_trys']:
                print "Game over"
                return


def select_difficulty():
    """
    Behavior: Function asks user to select the difficulty level
    from (easy/medium/hard)
    if user types incorrect, function will throw an error
    Output: Return result of selection
    """
    print "Please select a difficulty level from easy/ medium/ hard "
    if selection == "easy":
        print "easy is choosen"
    elif selection == "medium":
        print "medium is choosen"
    elif selection == "hard":
        print "hard is choosen"
    else:
        raise ValueError('input error')
    return selection


def first_blank(selection):
    """
    Behavior: Calls the function play game with the choosen level difficulty

    """
    if selection == "easy":
        play_game(data['easy']['answers'], data['easy']['phrase'])
    elif selection == "medium":
        play_game(data['medium']['answers'], data['medium']['phrase'])
    else:
        play_game(data['hard']['answers'], data['hard']['phrase'])
    return


select_difficulty()
first_blank(selection)
