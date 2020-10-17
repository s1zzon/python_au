# preparing

old = open(r"C:\Users\User\Desktop\python\source_leetcode_data.txt")
new = open(r"C:\Users\User\Desktop\python\linked-list.md", "a")
head = old.readline()
head = head.replace('\n', '')
link = old.readline()
link = link.replace('\n', '')
index_problems = link.find('problems')
pointer = link[index_problems + 9:-1]
full_text = old.read()
index_def = full_text.find('def')
body = full_text[index_def-1:]

# writing

new.write('\n# Linked List\n\n')
new.write('+[' + head + ']' + '(#' + pointer + ')\n\n')
new.write('# Linked List\n\n')
if split_head[2] != '':
    new.write('+[' + head + ']' + '(#' + split_head[0] + '-' + split_head[1] + '-' + split_head[2] + ')\n\n')
else:
    new.write('+[' + head + ']' + '(#' + split_head[0] + '-' + split_head[1] + ')\n\n')
new.write('##' + head + '\n\n')
new.write(link + '\n\n')
new.write('```python\n' + body + '\n' + '```')

# closing

old.close()
new.close()
