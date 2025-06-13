quiz = [
    {
        "question": "What is the Linux kernel?",
        "options": ["a) A desktop environment", "b) A graphical user interface", "c) The core of the operating system", "d) A software application"],
        "answer": "c"
    },
    {
        "question": "Who created Linux?",
        "options": ["a) Richard Stallman", "b) Linus Torvalds", "c) Dennis Ritchie", "d) Bill Gates"],
        "answer": "b"
    },
    {
        "question": "Which of the following is NOT a Linux distribution?",
        "options": ["a) Ubuntu", "b) Fedora", "c) MacOS", "d) Debian"],
        "answer": "c"
    },
    {
        "question": "What does 'open source' mean in the context of Linux?",
        "options": ["a) The software is free to use", "b) The software's source code is available for anyone to view, modify, and distribute", "c) It only runs on specific hardware", "d) It is closed and proprietary"],
        "answer": "b"
    },
    {
        "question": "Which command is used to list files and directories in Linux?",
        "options": ["a) pwd", "b) ls", "c) cd", "d) cat"],
        "answer": "b"
    },
    {
        "question": "What is the role of a package manager in Linux?",
        "options": ["a) To manage hardware drivers", "b) To download, install, update, and remove software packages", "c) To monitor system performance", "d) To create bootable drives"],
        "answer": "b"
    },
    {
        "question": "What does the 'chmod' command do?",
        "options": ["a) Changes file permissions", "b) Modifies file content", "c) Deletes files", "d) Compresses files"],
        "answer": "a"
    },
    {
        "question": "What is the default shell for most Linux distributions?",
        "options": ["a) Bash", "b) Zsh", "c) Fish", "d) PowerShell"],
        "answer": "a"
    },
    {
        "question": "Which of the following is a popular Linux text editor?",
        "options": ["a) Notepad", "b) Nano", "c) Sublime", "d) MS Word"],
        "answer": "b"
    },
    {
        "question": "What does the command 'sudo' do in Linux?",
        "options": ["a) Lists directory contents", "b) Executes commands with superuser privileges", "c) Opens a text editor", "d) Reboots the system"],
        "answer": "b"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Linux Quiz!\n")
    print("Press Enter without typing anything to quit the quiz at any time.\n")

    for i, q in enumerate(quiz):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("\nYour answer (a/b/c/d): ").strip().lower()

        # Check if the user pressed Enter without typing anything
        if answer == "":
            print("\nYou chose to exit the quiz.")
            break  # Exit the loop

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # Display the score when the user exits or finishes the quiz
    print(f"Your score: {score}/{len(quiz)}")
    print("Thanks for playing!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
