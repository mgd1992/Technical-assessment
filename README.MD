**AMENITIZ**

*Technical assessment*

# **Cash Register App** 🛒

## **Overview**
This project is a simple **cash register** system that allows adding products to a cart, calculating the total price, and applying special discount rules based on the product type.

## **Features**

✅ Adds products to the cart.

✅ Calculates the total price dynamically.

✅ Applies discounts or special rules based on the product.


## **Products and Pricing**

| Product Code | Name         | Price  |
|-------------|-------------|--------|
| GR1         | Green Tea   | €3.11  |
| SR1         | Strawberries | €5.00  |
| CF1         | Coffee      | €11.23 |

### **Special Pricing Rules**
- **Buy-One-Get-One-Free (Green Tea - GR1)**: If you buy **2 or more**, you only pay for half of them.
- **Bulk Discount (Strawberries - SR1)**: If you buy **3 or more**, the price drops to **€4.50** per unit.
- **Volume Discount (Coffee - CF1)**: If you buy **3 or more**, the price of each unit drops to **2/3 of the original price**.

## **Defining the Solution**
We built a `Cart` class that can:

✔ Add products to the cart.

✔ Calculate the total price while applying discount rules.

Basic Structure:

- A Cart class with methods to add products and calculate the total.
- A dictionary of products with their prices for easy reference.
- Rules for each special product (Green Tea, Strawberries, Coffee).

## **Installation & Usage**

### **Requirements**
- Python 3 installed

### **Run the Program**
Clone this repository and navigate to the project folder:

```bash
git clone https://github.com/mgd1992/Technical-assessment.git
```

```bash
cd Technical-assessment
```
To run the backend:

```bash
python3 main.py
```
To run the frontend navigate up to cart-test-app:

```bash
cd Technical-assessment/front/cart-test-app
npm run dev
```

## **Future Improvements**

🚀 Implement tests.
