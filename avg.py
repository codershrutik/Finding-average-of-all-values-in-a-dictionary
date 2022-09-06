test_dict = {"This": 42, "is": 37, "the": 58, "time": 86, "of": 19, "our": 5, "lives":7}
print("The original dictionary is : " + str(test_dict))

# values extracted using values()
res = sum(test_dict.values()) / len(test_dict)

print("The computed mean : " + str(res))
