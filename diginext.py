smootiesData = {
    "classic":["strawberry", "banana", "pineapple", "mango", "peach", "honey", "ice", "yogurt"],
    "corest berry":["strawberry", "raspberry", "blueberry", "honey", "ice", "yogurt"],
    "freezie":["blackberry", "blueberry", "black currant","grape juice", "frozen yogurt"],
    "greenie":["green apple", "kiwi", "lime", "avocado", "spinach", "ice","apple juice"],
    "vegan delite":["strawberry", "passion fruit", "pineapple", "mango", "peach", "ice", "soy milk"],
    "just desserts":["banana", "ice cream", "chocolate", "peanut", "cherry"],
}

# def print_output(recipes):
    # print(', '.join(recipes))

# def main():
input_smoothie = input().lower().split(",")
key = input_smoothie.pop(0)
if key in smootiesData:
    
    recipes = smootiesData[key]
    if len(input_smoothie)>=1:
        for data in input_smoothie:
            if '+' in data : 
                recipes.append(data[1:])
            if '-' in data : 
                recipes.remove(data[1:])
    # print_output(recipes)
    print(','.join(recipes))
        


# main()