capitals = {
    "Nigeria": "FCT",
    "France": "Berlin"

 }

# [] = list, {} = caliberaces(dictionary)

#Nested list in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijan"],
    "Germany": ["Stuttgart", "Berlin"],

}
#print(travel_log["France"][1])
# #To print an item in a list, Lille
# for list in travel_log:
#     print(travel_log["France"][2])
#
#
# Nested_list = ["A", "B", ["C", "D"]]
# #for list in Nested_list:
# print(Nested_list[2][0])

#List nested in a dictionary
travel_log = {
    "France": {
        "number_times_visited": 10,
        "number_of_cities_visited": ["Paris", "Lille", "Dijan"],#list nested in a dictionary
    },
    "Germany": {
        "cities_visited": [ "Berlin", "Hamburg", "Stuttgart",],
        "times_visited": 5
    }
}
#to access Stuttgart in the nested list
print(travel_log["Germany"]["cities_visited"][2])
