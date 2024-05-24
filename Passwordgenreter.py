import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def main():
    length = int(input("Enter the desired length of the pass word "))
    password = generate_password(length)
    print("Generate password: ",password)

if __name__ == "__main__":
    main()