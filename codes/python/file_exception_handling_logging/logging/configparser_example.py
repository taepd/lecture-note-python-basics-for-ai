import configparser

config = configparser.ConfigParser()

config.read("example.cfg")
print(config.sections())

print(config["SectionThree"])
for key in config["SectionOne"]:
    value = config["SectionOne"][key]
    print("{0} : {1}".format(key, value))
