files = ['_global_', 'Group', 'Group#now', 'nowjs', 'User', 'User#now',
'User#user']
head = '<!-- ============================== class title ============================ -->'
foot = '<!-- ============================== footer ================================= -->'
src = '../symbols/src/now_lib_'
git = 'https://github.com/Flotype/now/blob/master/lib/'
def del_html(st):
    try:
        i = st.index('.html')
    except ValueError:
        return st
    while True:
        st = st[:i] + st[(i+5):]
        try: 
            i = st.index('.html')
        except ValueError:
            return st


def crop(st):
    i = st.index(head)
    st = st[i:]
    i = st.index(foot)
    return st[:i]

    

def convert(filename):
    f = open(filename + '.html', 'r')
    content = f.read()
    output = filename + '.ejs'

    
    content = crop(content)
    content = del_html(content)
    content = content.replace(src, git)

    f = open(output, 'w')
    f.write(content)

for doc in files:
    convert(doc)
