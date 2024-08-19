import sys

#import pyparsing #- available if you need it!
#import lark #- available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    if pattern == str('\\d'):
        for character in input_line:
            if character.isdigit():
                return True
    if pattern == str('\\w'):
        for character in input_line:
            if character.isalnum():
                return True
    if pattern[0] == '[' and pattern[len(pattern)-1] == ']':
        characters = pattern[1:len(pattern)-1]
        for c in characters:
            if c in input_line:
                return True
    else:
       return False


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
