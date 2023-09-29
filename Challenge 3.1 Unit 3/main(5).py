def linearSearchProduct(productList, targetProduct):
    indices = []
    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    return indices

# Example usage:
products = ["Red", "White","Red","Purple","Green","Red"]
target = "Red"
target2 = 'shoes'
result = linearSearchProduct(products, target)
print(result)