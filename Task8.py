"""Create a method sayHello/say_hello/SayHello that takes as input a name,
city, and state to welcome a person.
Note that name will be an array consisting of one or
more values that should be joined together with one space between
each, and the length of the name array in test cases will vary."""


def say_hello(name, city, state):
    return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)
