# Lets define a function so that it can be a little convienant for me.
# This will be a logical based programming, just data isn't a priority right now.

def user_input(): # Why should I use the input function when I can just make my own instead?
    choice = int(input("Choose number: ")) 
    return choice

# Lets move on to other definitions, which will become useful over time.

def show_menu():
    print("╔══════════════════════╗")
    print("║ AdviceTUI 0.1.0 DEMO ║")
    print("╚══════════════════════╝")
    print("     ")
    print("『 OPTIONS 』")
    print("1) Show SubMenu | 2) FAQ | 3) Exit Program")

def show_faq():
    print("╔════════════════════════════╗")
    print("║ Frequently Asked Questions ║")
    print("╚════════════════════════════╝")
    print("     ")
    print("『 Technical Writer Speaking! 』")
    print("     ")
    print("Question, by Nobody asked! lol... Said: Why are there grammatical issues?")
    print("Answered by Technical Writer: Because in order to make sure that it wasn't written by a clanker, we use our own grammatical mistakes to assure that intentionally.")
    print("     ")
    print("════════════════════════════")
    print("     ")

def show_submenu():
    print("╔═══════════════════════════════╗")
    print("║ Advice, Tips, Recommendations ║")
    print("╚═══════════════════════════════╝")
    print("     ")
    print("『 Your all in one place bafei 』")
    print("     ")
    print("1. How do I start programming?")
    print("2. Is privacy a spectrum?")
    print("3. Why should I care about privacy? (Minors and adults editions)")
    print("4. Why should I care about digital hygine? (Operations Edition)")
    print("5. Why should I as a developer care about FOSS/FLOSS?")
    print("6. How do I spot AI in videos, images, and text?")
    print("7. Why can't I achieve privacy on proprietary systems?")
    print("8. How do I start being productive (No fluff)")
    print("9. Why should I care about Linux? Why and what.")
    print("")
    print("════════════════════════════")

# This is where the real, true actuall program begins actually

while True:
    show_submenu()
    prompt = user_input()

    if prompt == "1":
        print("Advice Revision 1")
        print("════════════════════════════")
        print("     ")
        print("In order to start programming, you need one or two things:")
        print("One you can start by picking a programming language,")
        print("In beginners land, you can start learning Python first.")
        print("In also beginners land, but not so simple, is C programming language.")
        print("But I recommend Python as your first language for now, until you have a solid,")
        print("grasp of the programming language itself, that is by mastering it.")
        print("     ")
        print("However, if you want to challenge yourself, start with C.")
        print("Why Python? Because its the first beginners choice.")
        print("Why C? Because you will also learn other languages like Rust, Go, etc.")
        print("     ")
        print("Or two, start by studying or learning Computer science and Data Structure & Algerithms.")
        print("Why? Because you will later understand and get a solid grasp of computers and later algerithms.")
        print("1. You will understand a little bit about computers, and later with C you will learn a lot about computers.")
        print("2. By making an algerithm, you make a personalized feed for yourself and anybody else around, that is the typicallization of what it seems like.")
        print("     ")
        print("Final Verdict: Learn Python first as your choice, then later down the line learn computer science and algerithms, and especially data structure as well.")
        print("     ")
        print("════════════════════════════")
        print("     ")
        break