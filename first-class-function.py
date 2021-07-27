def html_tag(tag):
    def wrap_text(msg):
        print('{0}><{1}></{0}>'.format(tag, msg))

    return wrap_text


def outer_function(message):
    def in_function():
        print(message)

    return in_function()


outer_function('Coat')


def display():
    print('display function running = executable')


# print_h1 = html_tag('h1')
print_h1 = html_tag('p')
print_h1('Test Headline!')
print_h1('Another Headline!')
