import csv
import os

# Set the paths
input_file_path = r"N:\Dataset\all.txt"
output_file_path = r"N:\Dataset\output_file.csv"

# Check if the file exists
if os.path.exists(input_file_path):
    print("File found!")
else:
    print("File not found:", input_file_path)

# Open the output CSV file for writing
with open(output_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['productId', 'title', 'price', 'userId', 'profileName', 'helpfulness', 'score', 'time', 'summary', 'text']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Initialize variables to hold product information
    current_product = {}
    review = {}

    # Open the input text file and process line by line
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if ": " in line:
                key, value = line.split(": ", 1)

                if key == "product/productId":
                    # Write the current product and review to the CSV if a product exists
                    if current_product and review:
                        writer.writerow({
                            'productId': current_product.get('productId', ''),
                            'title': current_product.get('title', ''),
                            'price': current_product.get('price', ''),
                            'userId': review.get('userId', ''),
                            'profileName': review.get('profileName', ''),
                            'helpfulness': review.get('helpfulness', ''),
                            'score': review.get('score', ''),
                            'time': review.get('time', ''),
                            'summary': review.get('summary', ''),
                            'text': review.get('text', '')
                        })
                    # Reset for a new product
                    current_product = {'productId': value}
                    review = {}

                elif key == "product/title":
                    current_product['title'] = value

                elif key == "product/price":
                    current_product['price'] = value

                elif key == "review/userId":
                    review['userId'] = value

                elif key == "review/profileName":
                    review['profileName'] = value

                elif key == "review/helpfulness":
                    review['helpfulness'] = value

                elif key == "review/score":
                    review['score'] = float(value)

                elif key == "review/time":
                    review['time'] = int(value)

                elif key == "review/summary":
                    review['summary'] = value

                elif key == "review/text":
                    review['text'] = value

        # Write the last product after finishing the loop
        if current_product and review:
            writer.writerow({
                'productId': current_product.get('productId', ''),
                'title': current_product.get('title', ''),
                'price': current_product.get('price', ''),
                'userId': review.get('userId', ''),
                'profileName': review.get('profileName', ''),
                'helpfulness': review.get('helpfulness', ''),
                'score': review.get('score', ''),
                'time': review.get('time', ''),
                'summary': review.get('summary', ''),
                'text': review.get('text', '')
            })

print("Data has been grouped and saved to output_file.csv")
