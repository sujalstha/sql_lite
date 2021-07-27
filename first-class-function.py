def html_tag(tag):
    def wrap_text(msg):
        print('{0}><{1}></{0}>'.format(tag, msg))

    return wrap_text


def outer_function(message):
    def in_function():
        print(message)


def display():
    print('display function running = executable')


x = outer_function(display)

print(x)

# print_h1 = html_tag('h1')
print_h1 = html_tag('p')
print_h1('Test Headline!')
print_h1('Another Headline!')
