#6-1：人
people = {'first_name':'xinyu', 'last_name': 'zhu', 'age': '23', 'city':'Leeds'}
print (people ['first_name'])
print (people ['last_name'])
print (people ['age'])
print (people ['city'])

#6-2：喜欢的数
numbers = {'xinyu':'2',
    'yu':'3',
    'ivy':'4',
    'dage':'5',
    'jjj':'6',
    }
for a, b in numbers.items():
    print (f"{a}'s favorite number is {b}")


#6-3：词汇表
coding_lexicon = {'max ()': 'the maximal value',
    'min()': 'the minimal value',
    'sum()': 'the added value',
    'list()':'making up a list',
    '.append()':'to add something',
    }
for v, i in coding_lexicon.items():
    print (f"For {v}, means {i}.")






