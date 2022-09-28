ratings = {}
products = {}
"""
I read the products.txt and ratings.txt file in the program with the open() method. 
I deleted the leading and trailing spaces with the strip() method, 
and split the characters (, and -) that I gave inside with the split() method.
"""
with open("ratings.txt") as f:
    for line in f:
       k ,v =  line.strip().split(',')
       ratings[k] = v


with open("products.txt") as f:
    for line in f:
       k ,v =  line.strip().split('-')
       products[k] = v



#I created a while loop and the program will run until the user type "exit".
while True:
    """
    I created the variable "best_rating" to find the best rating,
    the variable best_rating_company to find the company with the best rating, 
    and the variable company_counter to find how many different companies sold a product.
    """
    best_rating = 0
    best_rating_company = ""
    company_counter = 0

    product_name = input("Please enter the product you want to buy:")
    if product_name == "exit":
        print("Goodbye!")
        break
        """
        I went through all the items with the for loop, so I found the company that matched 
        the product name entered by the user and increased the company_counter variable by 1.
        """
    for key, value in products.items():
        if product_name in value:
            company_counter += 1
            rating = float(ratings[key].split("/")[0])
            """
            I added an if condition to find the largest rating among the companies selling the entered item,
            so I assigned the highest rating and the company with this rating to my variables.
            """
            if rating > best_rating:
                best_rating = rating
                best_rating_company  = key

    #if only one company sells the entered product...
    if company_counter == 1:
        print(f"Only {best_rating_company} sells this product.")

    #if no company sells the entered product...
    if best_rating == 0:
        print("None of the companies sell this product.")
    """
    If more than one company sells the entered product and their rating is not 0, I printed the name of the product, 
    the name of the company with the highest rating, and the rating on the screen.
    """
    if best_rating != 0 and company_counter != 1:
        print(f'We suggest you to buy {product_name} from {best_rating_company} because it has the highest ranking as {best_rating}')





