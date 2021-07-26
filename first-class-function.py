def html_tag(tag):

    def wrap_text(msg):
        print('{1}><{1}}><{0}>'.format(tag, msg))
