
start = "Param1317"
end = "$ decimal places"
to_append = "HELLO WORLD"

with open('test.txt','r') as handler:
    with open('new_file.txt','w') as write_handler:
        started = False
        for line in handler:
            if line.find(start):
                started = True
            write_handler.write(line)
            if started and line.endswith(end):
                started = False
#write_handler.write(line)
                write_handler.write(to_append)
