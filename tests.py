lessons = ["farsi","english","lesson 3"]
results = []
maxlen = 3
def fill_next_cell(array):
    cloned = array.copy()
    if len(cloned) == maxlen:
        results.append(cloned)
    else:
        cloned.append(None)
        index_to_inject = len(cloned)-1
        for lesson in lessons:
            cloned[index_to_inject] = lesson
           
            fill_next_cell(cloned)

fill_next_cell([])
for i in results:
    print(i)
