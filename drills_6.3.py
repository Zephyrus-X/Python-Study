#6-4：词汇表2
coding_lexicon = {'max ()': 'the maximal value',
    'min()': 'the minimal value',
    'sum()': 'the added value',
    'list()':'making up a list',
    '.append()':'to add something',
    }
for v, i in coding_lexicon.items():
    print (f"For {v}, means {i}.")
coding_lexicon ['.values()'] = 'go through values in dictionary'
coding_lexicon ['.keys()'] = 'go through keys in dictionary'
coding_lexicon ['.item()'] = 'go through keys and values in dictionary'
print (coding_lexicon)
for v, i in coding_lexicon.items():
    print (f"For {v}, means {i}.")

#6-5：河流
maps = {}
maps ['nile'] = 'Egupt'
maps ['Yellow_river'] = 'China'
maps ['Eyer'] = 'UK'
maps ['missisipy'] = 'USA'
for river, country in maps.items():
    print(f"The {river} runs through {country}.")
for river in maps.keys():
    print (river)
for country in maps.values():
    print (country)

#6-6：调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
person = ['phil', 'edward', 'jen', 'sarah', 'sjdw', 'djisao']
for name in person:
    if name in favorite_languages.keys():
        print (f"Hi {name}, thank you for taking the poll.")
    else:
        print (f"Hello {name}, why not come and take my polls?")

