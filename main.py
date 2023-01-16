from collections import UserDict
from Class import *

ab = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Sorry, try again"
        except ValueError:
            print("incorrect phone number")
        except KeyError:
            print("incorrect Name")
    return wrapper


def greetings(*args):
    print("How can I help you?")


@input_error
def add(*argv):
    ab.add_record(Record(Name(argv[0][0]), Phone(argv[0][1])))


@input_error
def add_phon(*argv):
    ab[argv[0][0]].add_phone(Phone(argv[0][1]))


@input_error
def change(*argv):
    if len(argv[0]) == 3:
        ab[argv[0][0].title()].add_phone(Phone(argv[0][2]))
        ab[argv[0][0].title()].delete_phone(Phone(argv[0][1]))
    else:
        print("To change the number, enter the name of the contact, the number to change, the new phone number")


@input_error
def del_phone(*argv):
    ab[argv[0][0].title()].delete_phone(Phone(argv[0][1]))


@input_error
def show_all(*argv):
    print(ab)


@input_error
def output_phone(name):
    print(ab[name[0].title()])


COMMANDS = {
    greetings: "hello",
    add: "add",
    add_phon: 'append',
    change: "change",
    output_phone: "phone",
    show_all: "show",
    del_phone: "del"

}


def command_parser(u_input: str):
    for comand, key_words in COMMANDS.items():
        if u_input.startswith(key_words):
            return comand, u_input.replace(key_words, "").strip().split(" ")
    return None, None


def main():
    while True:
        u_input = input(">>>")
        u_input = u_input.lower()
        if u_input in [".", "good bye", "close", "exit", "/"]:
            print("Good bye!")
            break
        comand, data = command_parser(u_input)
        if not comand:
            print("Enter command")
        else:
            comand(data)


if __name__ == "__main__":
    main()
