import matplotlib.pyplot as plt

grh = input("Select the type of graph: 1)line 2)bar 3)Pie 4)Scattar 5)Histogram : \n")


if grh == "1":
    x=list(input("Enter number for x axis: "))
    y=list(input("Enter number for y axis: "))
    plt.plot(x,y , color='red', linestyle='dashed', marker='o',markerfacecolor='green')
    plt.xlabel('X axis')
    plt.ylabel('Y Axis')
    plt.title('Graph and Chart plotter - Line chart')
    plt.legend()
    plt.show()

elif grh == "2":
    num_categories = int(input("Enter the number of categories: "))
    categories = []
    values = []
    for i in range(num_categories):
        category = input(f"Enter Category {i + 1}: ")
        value = float(input(f"Enter Value for Category {i + 1}: "))
        categories.append(category)
        values.append(value)
    plt.figure(figsize=(8, 6))  # Adjust the figure size (optional)
    plt.bar(categories, values, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Graph and Chart plotter - Bar graph')

    plt.show()


elif grh == "3":
    
    labels = ['A', 'B', 'C', 'D']
    sizes = [int(input(f"Enter the value of {label}: ")) for label in labels]
    plt.figure(figsize=(8, 8)) 
    colors = ['red', 'blue', 'green', 'yellow']
    explode = (0, 0.1, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Graph and Chart plotter - Pie chart')
    plt.axis('equal') 
    plt.show()

elif grh == "4":
    x_str = input("Enter X-axis values (comma-separated): ")
    x = [int(val) for val in x_str.split(",")]
    y_str = input("Enter Y-axis values (comma-separated): ")
    y = [int(val) for val in y_str.split(",")]
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', marker='o', s=100)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph and Chart plotter - Scatter chart')
    plt.grid(True)
    plt.show()


elif grh =="5":
    data = input("Enter a list of numbers separated by spaces: ")
    data = [int(x) for x in data.split()]
    num_bins = 5
    plt.hist(data, bins=num_bins, color='skyblue', edgecolor='black')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Graph and Chart plotter - Histogram chart')
    plt.show()

else:
    print("Invaild Choice")