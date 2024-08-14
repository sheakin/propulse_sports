
Propulse Sports
Propulse Sports is an eCommerce website built with Python and Django, designed for purchasing sports items online. The platform offers a seamless shopping experience with features like product listing, add to cart, remove from cart, and dynamic product management through an admin interface.

Features
Product Listing: Browse through a wide range of sports items available for purchase.
Add to Cart: Easily add desired products to your cart for checkout.
Remove from Cart: Remove unwanted items from your cart before purchase.
Admin Panel:
Add new products.
Set product priority to influence the order of display.
Manage the product catalog efficiently.
Featured Products: Highlight specific products as featured based on admin settings.
Latest Products: Automatically display the latest additions to the store.
Technology Stack
Backend: Python, Django
Database: SQLite
Frontend: HTML, CSS, JavaScript, Bootstrap
Version Control: Git
Installation
Clone the Repository:
bash
Copy code
git clone git@github.com:sheakin/propulse_sports.git
Navigate to the Project Directory:
bash
Copy code
cd propulse_sports
Create and Activate Virtual Environment:
bash
Copy code
python -m venv env
source env/bin/activate
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Apply Migrations:
bash
Copy code
python manage.py migrate
Run the Development Server:
bash
Copy code
python manage.py runserver
Usage
Visit the homepage to browse products.
Add items to the cart and proceed to checkout.
Admin users can log in to the admin panel to manage products, set priorities, and mark featured or latest products.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
