
# import matplotlib.pyplot as plt
# import seaborn as sns

# def plot_histogram(list1, list2, title="Histogram", xlabel="Value", ylabel="Frequency"):
#     plt.rcParams['figure.figsize'] = (10, 10)
#     plt.hist(list1, bins=100, label="Item Outlet Sales")
#     plt.hist(list2, alpha=0.3, bins=150, label="Item MRP")
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.legend()
#     plt.show()

# def plot_scatter(data):
#     plt.rcParams['figure.figsize'] = (8, 6)
#     plt.scatter(data["Item_Outlet_Sales"], data["Item_MRP"])
#     plt.title("Item Outlet Sales vs. Item MRP")
#     plt.xlabel("Item Outlet Sales")
#     plt.ylabel("Item MRP")
#     plt.show()

# def plot_bar(data, column):
#     plt.figure(figsize=(10, 6))
#     sns.countplot(data[column])
#     plt.title(f"Count of {column}")
#     plt.xlabel(column)
#     plt.ylabel("Count")
#     plt.xticks(rotation=45)
#     plt.show()

# def plot_box(data, column):
#     plt.figure(figsize=(8, 6))
#     sns.boxplot(x=data[column], y=data["Item_Outlet_Sales"])
#     plt.title(f"Boxplot of Item Outlet Sales by {column}")
#     plt.xlabel(column)
#     plt.ylabel("Item Outlet Sales")
#     plt.xticks(rotation=45)
#     plt.show()

# import matplotlib.pyplot as plt

# def plot_pie_for_each_item(data):
#     item_sales = data.groupby("Item_Type")["Item_Outlet_Sales"].sum()

#     plt.figure(figsize=(10, 8))
#     labels = []
#     sizes = []
#     for item_type, sales_sum in item_sales.items():
#         labels.append(item_type)
#         sizes.append(sales_sum)

#     plt.pie(sizes, labels=labels, autopct='%1.1f%%')
#     plt.title("Sales Distribution for Each Item Type")
#     plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     plt.legend(labels, loc="upper right")
#     plt.show()

# # Assuming `data` is you

# def plot_graphs(data):
#     plot_histogram(data["Item_Outlet_Sales"], data["Item_MRP"])
#     plot_scatter(data)
#     plot_pie_for_each_item(data)
#     plot_box(data, "Outlet_Type")


