# from email import message
# import logging

# logging.basicConfig(filename='test.log', level=logging.INFO, format='%(message)s')
# logging.info("test")
# logging.shutdown()

with open("test.log") as fp:
    for line in fp:
        time, id = str(line).replace("\n","").split("|")
    print(time, "-", id)