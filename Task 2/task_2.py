2.
# Given the product name ' OnePlus Nord-CE 3 ', write code to clean it 
# by removing extra spaces, converting all letters to uppercase, and 
# replacing the dash with a colon.<br><br><em><strong>Hint:</strong> Use strip()
# , upper(), and replace() methods in sequence.</em>

product = " OnePlus Nord-CE 3 "
result = " ".join(product.split())
print(product)  
print(result)  
print(result.upper())
result_2 = result.replace("-",":")
print(result_2)