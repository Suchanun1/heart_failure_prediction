import numpy as np

searchQuery = ""
print("\n\n")
print("You can search for the following terms, and you will get an output of webpages that are returned by the query in order of importance.\n")
print("List of terms - Ash, Butternut, Cherry, Elm, Katsura, Magnolia, Teak, Ginkgo, Fir, Hickory, Pine, Willow, Redwood, Sassafras, Oak, Spruce, Aspen\n")
print("You can enter your query of the form :- ")
print("1) Just 1 term (For eg - Katsura) ")
print("2) Combination of terms (For eg - Hickory and Sassafras and Oak)")
print("3) Make use of the keywords - AND, OR, NOT to output the webpages returned by a combination of terms")
print("4) Make sure you use the same keyword across the combination query. For example - You cannot do Hichory and Pine not Sassafras")

searchQuery = input("Enter your search query here : ")
print("\n")


terms = ["ash", "butternut", "cherry", "elm", "katsura", "magnolia", "teak",  "ginkgo", "fir", "hickory", "pine", "willow", "redwood", "sassafras", 
         "oak", "spruce", "aspen"]


queryVector = np.zeros(len(terms))
listTerms = []
combinationKeyword = ""

safe = True

arr = searchQuery.split()
if len(arr) == 1:
    word = arr[0].lower()
    if word not in terms:
        print("You entered an invalid search term. Please make sure the spellings are correct and you used one of the given terms")
        safe = False

    else:
        queryVector[terms.index(word)] = 1
else:
    if (len(arr) % 2 == 0):
        print("You entered an invalid search term. Please make sure the spellings are correct and you used the right format for a combination query")
        safe = False
    else:  
        combinationKeyword = arr[1].lower()
        for i, s in enumerate(arr):
            arr[i] = s.lower()
            if i % 2 != 0:
                if arr[i] != combinationKeyword:
                    print("You made an error while typing the combination keyword. Make sure you do not use different keywords for the same search query")
                    safe = False
                    break
            else:
                if arr[i] not in terms:
                    print("You entered an invalid search term. Please make sure the spellings are correct and you used one of the given terms")
                    safe = False
                    break
                else:
                    listTerms.append(arr[i])

if safe:
    if combinationKeyword == "and" or combinationKeyword == "or":
        for s in listTerms:
            queryVector[terms.index(s)] = 1
    elif combinationKeyword == "not":
        count = 0
        for s in listTerms:
            if count == 0:
                queryVector[terms.index(s)] = 1
            else:
                queryVector[terms.index(s)] = -1
            count = 1



    T = np.array([
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    ])

    dT = np.dot(queryVector, T)

    webPage = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    webPageInOrder = ["K", "J", "G", "H", "F", "D", "I", "L", "B", "E", "C", "A"]
    tempRes = []
    res = []

    lookFor = 1

    if combinationKeyword == "and":
        lookFor = len(listTerms)
    elif combinationKeyword == "or" or combinationKeyword == "not":
        lookFor = 1

    for i, n in enumerate(dT):
        if n >= lookFor:
            tempRes.append(webPage[i])

    for n in webPageInOrder:
        if n in tempRes:
            res.append(n) 

    output = ', '.join(res)

    if len(tempRes) == 0:
        print("There were no webpages that were returned after your search query")
    else:
        print("Here is the result of Webpages returned by your search query in order of importance : ", output)


print("\n\n")