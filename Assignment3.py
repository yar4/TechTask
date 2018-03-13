import operator
Person = [
("Tom", "19", "167", "54"),
("Jony", "24", "180", "69"),
("Json", "21", "185", "75"),
("John", "27", "190", "87"),
("Jony", "24", "191", "98"),
    ]

print(sorted(Person, key=operator.itemgetter(0,1,2,3)))
