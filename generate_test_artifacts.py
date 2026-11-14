"""
Generate professional Test Cases, Execution Results, and Bug Reports
in Excel (.xlsx) and CSV formats.
"""

import os
import csv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# --- Test Cases Data (44 Test Cases) ---
TEST_CASES = [
    {
        "id": "TC001",
        "module": "User Registration",
        "scenario": "Verify successful user registration with valid data",
        "preconditions": "Application loaded; registration modal open",
        "steps": "1. Click 'Register' in navbar.\n2. Enter valid Name.\n3. Enter unique valid Email.\n4. Enter valid Password (>=6 chars).\n5. Enter matching Confirm Password.\n6. Click 'Create Account'.",
        "data": "Name: Sarah Connor, Email: sarah.c@example.com, Pass: Secret123!, Confirm: Secret123!",
        "expected": "Account created successfully, modal closes, user greeting displayed in navbar, success toast appears.",
        "actual": "Account created successfully, user greeted in navbar as 'Hi, Sarah Connor'.",
        "status": "Pass",
        "remarks": "Positive test case."
    },
    {
        "id": "TC002",
        "module": "User Registration",
        "scenario": "Verify registration with existing/duplicate email address",
        "preconditions": "User 'testuser@example.com' already registered",
        "steps": "1. Open registration modal.\n2. Enter Name.\n3. Enter existing Email 'testuser@example.com'.\n4. Enter Password and Confirm Password.\n5. Click 'Create Account'.",
        "data": "Email: testuser@example.com",
        "expected": "Registration rejected with alert message 'An account with this email already exists.'",
        "actual": "Alert message displayed: 'An account with this email already exists.' Registration prevented.",
        "status": "Pass",
        "remarks": "Negative test case for duplicate prevention."
    },
    {
        "id": "TC003",
        "module": "User Registration",
        "scenario": "Verify registration validation when passwords do not match",
        "preconditions": "Registration modal is open",
        "steps": "1. Fill Name and Email.\n2. Enter Password 'Password123!'.\n3. Enter Confirm Password 'Mismatch456!'.\n4. Click 'Create Account'.",
        "data": "Password: Password123!, Confirm Password: Mismatch456!",
        "expected": "Inline error 'Passwords do not match' displayed under Confirm Password field.",
        "actual": "Inline error 'Passwords do not match' displayed; submission blocked.",
        "status": "Pass",
        "remarks": "Negative validation test case."
    },
    {
        "id": "TC004",
        "module": "User Registration",
        "scenario": "Verify registration password boundary value (less than 6 characters)",
        "preconditions": "Registration modal is open",
        "steps": "1. Fill Name and Email.\n2. Enter 5-character Password '12345'.\n3. Enter Confirm Password '12345'.\n4. Click 'Create Account'.",
        "data": "Password: 12345 (5 characters - boundary test)",
        "expected": "Inline error 'Password must be at least 6 characters' displayed.",
        "actual": "Inline error 'Password must be at least 6 characters' displayed; submission blocked.",
        "status": "Pass",
        "remarks": "Boundary Value Analysis (BVA) negative test."
    },
    {
        "id": "TC005",
        "module": "User Registration",
        "scenario": "Verify registration form submission with all fields empty",
        "preconditions": "Registration modal is open",
        "steps": "1. Leave all fields empty.\n2. Click 'Create Account' button.",
        "data": "Empty inputs",
        "expected": "Validation error messages displayed under all required fields.",
        "actual": "Validation messages 'Full name is required', 'Email address is required', 'Password is required' displayed.",
        "status": "Pass",
        "remarks": "Negative field validation test."
    },
    {
        "id": "TC006",
        "module": "User Authentication",
        "scenario": "Verify login with valid registered credentials",
        "preconditions": "Default test user exists; user is logged out",
        "steps": "1. Click 'Login' in navbar.\n2. Enter registered Email.\n3. Enter correct Password.\n4. Click 'Login' button.",
        "data": "Email: testuser@example.com, Password: Password123!",
        "expected": "User logs in successfully, modal closes, navbar displays 'Hi, Test User' and Logout button.",
        "actual": "User logged in, avatar and greeting 'Hi, Test User' visible in navbar.",
        "status": "Pass",
        "remarks": "Core positive authentication test."
    },
    {
        "id": "TC007",
        "module": "User Authentication",
        "scenario": "Verify login failure with incorrect password",
        "preconditions": "Login modal is open",
        "steps": "1. Enter valid Email.\n2. Enter incorrect Password.\n3. Click 'Login' button.",
        "data": "Email: testuser@example.com, Password: WrongPassword999!",
        "expected": "Login rejected; alert message 'Invalid credentials: Incorrect password.' displayed.",
        "actual": "Alert message 'Invalid credentials: Incorrect password.' displayed.",
        "status": "Pass",
        "remarks": "Negative security test."
    },
    {
        "id": "TC008",
        "module": "User Authentication",
        "scenario": "Verify login failure with unregistered email address",
        "preconditions": "Login modal is open",
        "steps": "1. Enter unregistered Email.\n2. Enter any Password.\n3. Click 'Login' button.",
        "data": "Email: notregistered@example.com, Password: Password123!",
        "expected": "Login rejected; alert message 'Invalid credentials: User does not exist.' displayed.",
        "actual": "Alert message 'Invalid credentials: User does not exist.' displayed.",
        "status": "Pass",
        "remarks": "Negative authentication test."
    },
    {
        "id": "TC009",
        "module": "User Authentication",
        "scenario": "Verify login form validation with empty email and password",
        "preconditions": "Login modal is open",
        "steps": "1. Leave email and password inputs blank.\n2. Click 'Login' button.",
        "data": "Email: '', Password: ''",
        "expected": "Validation errors 'Email address is required' and 'Password is required' displayed.",
        "actual": "Inline error messages displayed under both fields; form not submitted.",
        "status": "Pass",
        "remarks": "Validation test case."
    },
    {
        "id": "TC010",
        "module": "User Authentication",
        "scenario": "Verify user logout functionality and session termination",
        "preconditions": "User is actively logged in",
        "steps": "1. Click 'Logout' button in navbar.\n2. Verify navbar returns to Guest state.",
        "data": "Active session for 'Test User'",
        "expected": "Session cleared, navbar shows 'Login' and 'Register' buttons, toast confirms logout.",
        "actual": "Session cleared, navbar toggled to guest mode, toast notification displayed.",
        "status": "Pass",
        "remarks": "Session management test."
    },
    {
        "id": "TC011",
        "module": "Product Listing",
        "scenario": "Verify product catalog displays all available items on initial page load",
        "preconditions": "Application is loaded",
        "steps": "1. Observe main catalog grid.\n2. Verify total product count indicator.",
        "data": "Default catalog state",
        "expected": "Catalog displays 12 product cards with message 'Showing 12 of 12 products'.",
        "actual": "All 12 product cards rendered cleanly; count message indicates 'Showing 12 of 12 products'.",
        "status": "Pass",
        "remarks": "Catalog display test."
    },
    {
        "id": "TC012",
        "module": "Product Listing",
        "scenario": "Verify all product cards render image, category, title, rating, and price correctly",
        "preconditions": "Catalog is displayed",
        "steps": "1. Inspect each product card in the grid.\n2. Verify presence of image, category badge, title, star rating, reviews count, price, Details and Add to Cart buttons.",
        "data": "Product Card #1 (Quantum Pro)",
        "expected": "All card components are visible and correctly formatted with currency symbol.",
        "actual": "Components rendered as expected with price formatted as '₹4,999.00' and category badge.",
        "status": "Pass",
        "remarks": "UI integrity test."
    },
    {
        "id": "TC013",
        "module": "Product Details",
        "scenario": "Verify opening product details modal by clicking 'Details' button",
        "preconditions": "Catalog is loaded",
        "steps": "1. Locate product #1 (Quantum Pro Wireless Headphones).\n2. Click 'Details' button.",
        "data": "Product ID: 1",
        "expected": "Modal opens displaying high-res product visual, title, price, in-depth description, rating, stock status, and quantity selector.",
        "actual": "Modal displayed with correct product title, price '₹4,999.00', stock '(25 units available)', and description.",
        "status": "Pass",
        "remarks": "Product details view test."
    },
    {
        "id": "TC014",
        "module": "Product Details",
        "scenario": "Verify quantity adjustment inside product details modal",
        "preconditions": "Product details modal is open",
        "steps": "1. Click '+' button to increment quantity to 3.\n2. Click '-' button to decrement to 2.\n3. Verify quantity input updates.",
        "data": "Quantity: 2",
        "expected": "Quantity updates dynamically between 1 and available stock limit.",
        "actual": "Quantity incremented to 3 and decremented to 2 as expected.",
        "status": "Pass",
        "remarks": "Details modal interaction test."
    },
    {
        "id": "TC015",
        "module": "Product Details",
        "scenario": "Verify closing product details modal via close button and backdrop click",
        "preconditions": "Product details modal is open",
        "steps": "1. Click '×' close button on top right of modal.\n2. Reopen modal and click outside modal card on backdrop.",
        "data": "Modal close action",
        "expected": "Modal closes and returns user to the catalog view.",
        "actual": "Modal closes smoothly on both actions.",
        "status": "Pass",
        "remarks": "Modal behavior test."
    },
    {
        "id": "TC016",
        "module": "Product Search",
        "scenario": "Verify searching for an existing product by exact title keyword",
        "preconditions": "Catalog is loaded with 12 items",
        "steps": "1. Enter 'Laptop' into search bar.\n2. Click search icon or press Enter.",
        "data": "Search Query: 'Laptop'",
        "expected": "Grid updates to display only matching laptop products; count indicates 'Showing 1 of 12 products'.",
        "actual": "UltraBook Pro laptop displayed; count shows 'Showing 1 of 12 products'.",
        "status": "Pass",
        "remarks": "Positive search test."
    },
    {
        "id": "TC017",
        "module": "Product Search",
        "scenario": "Verify search is case-insensitive (uppercase and lowercase)",
        "preconditions": "Catalog is loaded",
        "steps": "1. Search for 'HEADPHONES'.\n2. Note results.\n3. Search for 'headphones'.",
        "data": "Queries: 'HEADPHONES' vs 'headphones'",
        "expected": "Both queries return identical result: 'Quantum Pro Wireless Headphones'.",
        "actual": "Both searches returned the exact same product card.",
        "status": "Pass",
        "remarks": "Search usability test."
    },
    {
        "id": "TC018",
        "module": "Product Search",
        "scenario": "Verify searching for a non-existing product displays empty state message",
        "preconditions": "Catalog is loaded",
        "steps": "1. Enter non-existent keyword 'Spaceship'.\n2. Click search button.",
        "data": "Search Query: 'Spaceship'",
        "expected": "Grid displays empty state message 'No matching products found' with 'Clear Filters' button.",
        "actual": "Empty state with message 'No matching products found' displayed.",
        "status": "Pass",
        "remarks": "Negative search test."
    },
    {
        "id": "TC019",
        "module": "Product Search",
        "scenario": "Verify search behavior with leading/trailing whitespace without trim",
        "preconditions": "Catalog is loaded",
        "steps": "1. Enter query with spaces: '  Camera  '.\n2. Press Enter to search.\n3. Observe search results.",
        "data": "Search Query: '  Camera  '",
        "expected": "Leading/trailing whitespace should be trimmed, showing '4K Action Sports Camera'.",
        "actual": "Search query was not trimmed before filtering, causing 0 products to match due to space mismatch.",
        "status": "Fail",
        "remarks": "Defect logged as BUG-003: Search query does not trim whitespace."
    },
    {
        "id": "TC020",
        "module": "Product Search",
        "scenario": "Verify clearing search input restores full product catalog",
        "preconditions": "Active search results displayed",
        "steps": "1. Click '×' clear button in search input.\n2. Verify catalog restores.",
        "data": "Clear search button",
        "expected": "Search input is cleared and all 12 products are displayed again.",
        "actual": "Search cleared; catalog restored to 12 products.",
        "status": "Pass",
        "remarks": "Search reset test."
    },
    {
        "id": "TC021",
        "module": "Product Filtering",
        "scenario": "Verify filtering products by 'Electronics' category",
        "preconditions": "Catalog is loaded with All Categories selected",
        "steps": "1. In sidebar, select 'Electronics' radio button.\n2. Verify filtered items.",
        "data": "Category: Electronics",
        "expected": "Only Electronics products (Headphones, Laptop, Smartwatch, Camera) displayed (4 items).",
        "actual": "4 electronics products displayed; count shows 'Showing 4 of 12 products'.",
        "status": "Pass",
        "remarks": "Category filter test."
    },
    {
        "id": "TC022",
        "module": "Product Filtering",
        "scenario": "Verify filtering products by 'Apparel' category",
        "preconditions": "Catalog is loaded",
        "steps": "1. Select 'Apparel' radio button.",
        "data": "Category: Apparel",
        "expected": "Only Apparel items (T-Shirt, Jeans, Fleece Jacket) displayed (3 items).",
        "actual": "3 apparel items displayed correctly.",
        "status": "Pass",
        "remarks": "Category filter test."
    },
    {
        "id": "TC023",
        "module": "Product Filtering",
        "scenario": "Verify filtering products by maximum price slider threshold",
        "preconditions": "Catalog is loaded",
        "steps": "1. Move price range slider to ₹2,000.\n2. Verify products displayed.",
        "data": "Max Price: ₹2,000",
        "expected": "Only products priced <= ₹2,000 (T-Shirt ₹699.00, Clean Code ₹999.00, Selenium Guide ₹1,299.00, Jeans ₹1,899.00) displayed.",
        "actual": "Exactly 4 products under ₹2,000 displayed; count shows 'Showing 4 of 12 products'.",
        "status": "Pass",
        "remarks": "Price boundary filtering test."
    },
    {
        "id": "TC024",
        "module": "Product Filtering",
        "scenario": "Verify combining category filter and price range filter simultaneously",
        "preconditions": "Catalog is loaded",
        "steps": "1. Select category 'Home & Kitchen'.\n2. Set price slider to ₹5,000.",
        "data": "Category: Home & Kitchen, Max Price: ₹5,000",
        "expected": "Only Home & Kitchen items with price <= ₹5,000 (Dutch Oven ₹3,499.00) displayed.",
        "actual": "Only Cast Iron Dutch Oven (₹3,499.00) displayed.",
        "status": "Pass",
        "remarks": "Multi-criteria filtering test."
    },
    {
        "id": "TC025",
        "module": "Product Filtering",
        "scenario": "Verify 'Reset All' button clears all category, price, and search filters",
        "preconditions": "Multiple filters actively applied",
        "steps": "1. Click 'Reset All' button in sidebar filter header.",
        "data": "Reset All action",
        "expected": "Category resets to 'All Categories', price slider resets to ₹1,00,000, search cleared, 12 items displayed.",
        "actual": "All filters reset to defaults and all 12 items displayed.",
        "status": "Pass",
        "remarks": "Filter reset test."
    },
    {
        "id": "TC026",
        "module": "Product Sorting",
        "scenario": "Verify sorting products by Price: Low to High",
        "preconditions": "Catalog is loaded",
        "steps": "1. Open 'Sort by' dropdown.\n2. Select 'Price: Low to High'.\n3. Verify order of items.",
        "data": "Sort: Price: Low to High",
        "expected": "Products ordered ascending by price (starting at ₹699.00 T-Shirt up to ₹79,999.00 Laptop).",
        "actual": "First product is ₹699.00 and last product is ₹79,999.00.",
        "status": "Pass",
        "remarks": "Sorting validation."
    },
    {
        "id": "TC027",
        "module": "Product Sorting",
        "scenario": "Verify sorting products by Customer Rating",
        "preconditions": "Catalog is loaded",
        "steps": "1. Select 'Customer Rating' from sort dropdown.",
        "data": "Sort: Customer Rating",
        "expected": "Products ordered descending by rating (top rating 4.9 first).",
        "actual": "Products with 4.9 rating (UltraBook, Clean Code) appear first.",
        "status": "Pass",
        "remarks": "Rating sort test."
    },
    {
        "id": "TC028",
        "module": "Shopping Cart",
        "scenario": "Verify adding a product to cart from product card in catalog",
        "preconditions": "Cart is initially empty (badge = 0)",
        "steps": "1. Click 'Add to Cart' on product #1 (Quantum Pro).\n2. Observe cart badge and toast notification.",
        "data": "Product ID: 1",
        "expected": "Cart badge updates to '1', toast notification 'Added \"Quantum Pro...\" to cart!' appears.",
        "actual": "Cart badge incremented to 1; confirmation toast displayed.",
        "status": "Pass",
        "remarks": "Core add-to-cart test."
    },
    {
        "id": "TC029",
        "module": "Shopping Cart",
        "scenario": "Verify adding multiple quantities of a product from details modal",
        "preconditions": "Cart badge = 1",
        "steps": "1. Open details for product #5 (T-Shirt).\n2. Set quantity to 3.\n3. Click 'Add to Cart'.",
        "data": "Product ID: 5, Quantity: 3",
        "expected": "Cart badge updates by 3 (total badge = 4).",
        "actual": "Cart badge updated to 4; toast displayed.",
        "status": "Pass",
        "remarks": "Bulk quantity addition test."
    },
    {
        "id": "TC030",
        "module": "Shopping Cart",
        "scenario": "Verify cart drawer displays all added items, quantities, and correct subtotal",
        "preconditions": "Cart contains items",
        "steps": "1. Click cart icon button in navbar.\n2. Verify list of items, item subtotals, tax, and order total.",
        "data": "Items: Product 1 (x1 = ₹4,999.00), Product 5 (x3 = ₹2,097.00)",
        "expected": "Subtotal = ₹7,096.00, GST (18%) = ₹1,277.28, Total = ₹8,373.28.",
        "actual": "Subtotal, tax, and total matched calculations exactly.",
        "status": "Pass",
        "remarks": "Cart calculation test."
    },
    {
        "id": "TC031",
        "module": "Shopping Cart",
        "scenario": "Verify incrementing item quantity using '+' button in cart drawer",
        "preconditions": "Cart drawer is open",
        "steps": "1. Click '+' button next to product #1.\n2. Observe quantity and totals.",
        "data": "Product #1 quantity from 1 to 2",
        "expected": "Quantity updates to 2, item subtotal updates to ₹9,998.00, cart badge increments to 5.",
        "actual": "Quantity updated to 2; subtotals recalculated automatically.",
        "status": "Pass",
        "remarks": "Cart quantity increment test."
    },
    {
        "id": "TC032",
        "module": "Shopping Cart",
        "scenario": "Verify decrementing item quantity using '-' button down to 1",
        "preconditions": "Product #1 has quantity 2",
        "steps": "1. Click '-' button next to product #1.",
        "data": "Quantity from 2 to 1",
        "expected": "Quantity updates to 1, totals decrease accordingly.",
        "actual": "Quantity decreased to 1 and totals updated.",
        "status": "Pass",
        "remarks": "Cart quantity decrement test."
    },
    {
        "id": "TC033",
        "module": "Shopping Cart",
        "scenario": "Verify manual input of negative or zero quantity in cart quantity field",
        "preconditions": "Cart contains items",
        "steps": "1. In cart drawer, click into quantity input for an item.\n2. Type '-2' or '0' and click away (blur event).\n3. Observe cart calculation.",
        "data": "Quantity input: -2",
        "expected": "System should reject negative/zero input, display error or clamp to minimum 1.",
        "actual": "System accepts negative value '-2', producing negative subtotal and corrupting cart total.",
        "status": "Fail",
        "remarks": "Defect logged as BUG-001: Cart accepts negative quantity on direct input."
    },
    {
        "id": "TC034",
        "module": "Shopping Cart",
        "scenario": "Verify removing a single product item from cart drawer",
        "preconditions": "Cart has multiple products",
        "steps": "1. Click 'Remove' button under product #5.\n2. Verify item removed and totals updated.",
        "data": "Remove Product #5",
        "expected": "Product #5 removed from list, cart count decrements, total updates.",
        "actual": "Item removed from cart; totals and badge updated.",
        "status": "Pass",
        "remarks": "Cart item deletion test."
    },
    {
        "id": "TC035",
        "module": "Shopping Cart",
        "scenario": "Verify clearing the entire cart using 'Clear Cart' button",
        "preconditions": "Cart contains items",
        "steps": "1. Click 'Clear Cart' button in cart drawer.\n2. Observe cart state.",
        "data": "Clear Cart action",
        "expected": "Cart empties, displays 'Your shopping cart is empty', badge resets to 0, Proceed to Checkout button is disabled.",
        "actual": "Cart emptied; empty state displayed; badge = 0; checkout disabled.",
        "status": "Pass",
        "remarks": "Clear cart test."
    },
    {
        "id": "TC036",
        "module": "Checkout",
        "scenario": "Verify 'Proceed to Checkout' button opens checkout modal with pre-filled totals",
        "preconditions": "Cart has at least 1 item",
        "steps": "1. Open cart drawer.\n2. Click 'Proceed to Checkout'.",
        "data": "Cart total > ₹0",
        "expected": "Cart drawer closes, Checkout modal opens, Total Payable displays correct cart total.",
        "actual": "Checkout modal opened displaying correct Total Payable amount.",
        "status": "Pass",
        "remarks": "Checkout initiation test."
    },
    {
        "id": "TC037",
        "module": "Checkout",
        "scenario": "Verify checkout form validation when submitting with all fields empty",
        "preconditions": "Checkout modal is open",
        "steps": "1. Leave all shipping inputs empty.\n2. Click 'Place Order' button.",
        "data": "Empty form submission",
        "expected": "Validation error messages appear under all required fields (Name, Email, Address, City, State, ZIP, Card fields).",
        "actual": "Inline error messages appeared under required fields; submission stopped.",
        "status": "Pass",
        "remarks": "Checkout required fields test."
    },
    {
        "id": "TC038",
        "module": "Checkout",
        "scenario": "Verify email field validation with invalid email format in checkout",
        "preconditions": "Checkout modal is open",
        "steps": "1. Enter 'invalid-email-address' into Email field.\n2. Fill other fields.\n3. Click 'Place Order'.",
        "data": "Email: 'invalid-email-address'",
        "expected": "Field validation error 'Enter a valid email address' displayed.",
        "actual": "Validation message 'Enter a valid email address' displayed; submission blocked.",
        "status": "Pass",
        "remarks": "Email format validation test."
    },
    {
        "id": "TC039",
        "module": "Checkout",
        "scenario": "Verify ZIP code field format validation when entering alphabetic characters",
        "preconditions": "Checkout modal is open",
        "steps": "1. Fill all valid details.\n2. In ZIP / Postal Code field, enter letters: 'ABCDE'.\n3. Click 'Place Order'.",
        "data": "ZIP: 'ABCDE'",
        "expected": "Field should validate numerical ZIP postal code format (e.g. 5 digits) and reject alphabetic string.",
        "actual": "Form accepts 'ABCDE' as valid ZIP because it only verifies non-empty without regex format validation.",
        "status": "Fail",
        "remarks": "Defect logged as BUG-002: ZIP code accepts non-numeric input without format check."
    },
    {
        "id": "TC040",
        "module": "Checkout",
        "scenario": "Verify toggling payment method between Credit Card and Cash on Delivery",
        "preconditions": "Checkout modal is open",
        "steps": "1. Select 'Cash on Delivery' radio option.\n2. Observe card details section.\n3. Re-select 'Credit / Debit Card'.",
        "data": "Payment option selection",
        "expected": "When COD selected, card inputs (card number, exp, cvv) are hidden; when Card selected, they reappear.",
        "actual": "Card input fields toggled visibility cleanly.",
        "status": "Pass",
        "remarks": "Payment method UI toggle test."
    },
    {
        "id": "TC041",
        "module": "Checkout",
        "scenario": "Verify credit card fields validation (card length, expiry, cvv)",
        "preconditions": "Credit Card payment selected",
        "steps": "1. Enter short card number '123'.\n2. Enter CVV '1'.\n3. Click 'Place Order'.",
        "data": "Card: '123', CVV: '1'",
        "expected": "Validation errors 'Card number format is incomplete' and 'CVV format is incomplete' displayed.",
        "actual": "Validation errors displayed under card number and CVV; order prevented.",
        "status": "Pass",
        "remarks": "Card format validation test."
    },
    {
        "id": "TC042",
        "module": "Order Confirmation",
        "scenario": "Verify successful order placement with complete valid checkout data",
        "preconditions": "Cart contains items; checkout modal open",
        "steps": "1. Fill Name: 'John Doe', Email: 'john@example.com', Address: '123 Test Way', City: 'Boston', State: 'MA', ZIP: '02115'.\n2. Select COD or valid mock card.\n3. Click 'Place Order'.",
        "data": "Complete valid customer data",
        "expected": "Checkout modal closes, Order Confirmation modal opens with unique Order ID (e.g. 'ORD-XXXXXX'), summary of ordered items, total paid, and recipient info.",
        "actual": "Order confirmed, unique Order ID generated, correct summary and recipient info displayed.",
        "status": "Pass",
        "remarks": "End-to-end order placement test."
    },
    {
        "id": "TC043",
        "module": "Order Confirmation",
        "scenario": "Verify shopping cart is automatically cleared upon successful order placement",
        "preconditions": "Order just placed successfully",
        "steps": "1. Inspect cart badge.\n2. Open cart drawer.",
        "data": "Post-order state",
        "expected": "Cart badge is 0, cart drawer shows empty state, localStorage cart is cleared.",
        "actual": "Cart badge reset to 0, drawer shows empty state.",
        "status": "Pass",
        "remarks": "Post-order state verification."
    },
    {
        "id": "TC044",
        "module": "Order Confirmation",
        "scenario": "Verify 'Continue Shopping' button resets UI and allows new purchases",
        "preconditions": "Order Confirmation modal is displayed",
        "steps": "1. Click 'Continue Shopping' button.\n2. Verify confirmation modal closes and user can browse catalog again.",
        "data": "Continue Shopping action",
        "expected": "Modal closes, catalog displays with all products ready for browsing.",
        "actual": "Modal closed cleanly, catalog ready for fresh purchases.",
        "status": "Pass",
        "remarks": "Post-order navigation test."
    }
]

# --- Real Discovered Bugs Data ---
BUG_REPORTS = [
    {
        "id": "BUG-001",
        "title": "Cart quantity field accepts negative or zero values on manual input, resulting in negative subtotal",
        "module": "Shopping Cart",
        "description": "When a shopper directly edits the quantity input field in the shopping cart drawer and types a negative number (e.g., -2) or 0, the application does not validate or clamp the input value to a positive integer. This causes the line item subtotal to become negative and distorts the total order calculation.",
        "preconditions": "At least one product is added to the shopping cart drawer.",
        "steps": "1. Add 'Quantum Pro Wireless Headphones' to cart.\n2. Open the cart drawer.\n3. Click directly inside the quantity input field for the product.\n4. Type '-2' and press Tab or click outside the input.\n5. Observe the item subtotal and overall Order Total.",
        "expected": "The application should reject negative and zero quantities, display an input validation alert or automatically reset/clamp the quantity to minimum 1.",
        "actual": "The quantity accepts -2, resulting in a subtotal of -₹9,998.00 and a negative Order Total.",
        "severity": "High",
        "priority": "High",
        "environment": "Windows 11, Google Chrome 157.0 (64-bit), Screen 1920x1080",
        "status": "Open",
        "evidence": "screenshots/bug-001-negative-cart-quantity.png"
    },
    {
        "id": "BUG-002",
        "title": "Checkout form accepts non-numeric alphabetic characters in ZIP/Postal Code field",
        "module": "Checkout Form",
        "description": "The ZIP/Postal Code input on the checkout modal does not enforce a numeric or valid postal code format. Submitting arbitrary alphabetic strings such as 'ABCDE' bypasses validation and proceeds with order placement.",
        "preconditions": "Cart has items and checkout modal is open.",
        "steps": "1. Proceed to checkout with valid items.\n2. Fill Name, Email, Street Address, City, and State with valid data.\n3. Enter 'ABCDE' in the 'ZIP / Postal Code' field.\n4. Select 'Cash on Delivery' and click 'Place Order'.",
        "expected": "Validation error message 'Please enter a valid numeric ZIP/postal code (e.g., 5 digits)' should appear and block submission.",
        "actual": "Form accepts 'ABCDE' without format validation and successfully triggers order confirmation.",
        "severity": "Medium",
        "priority": "Medium",
        "environment": "Windows 11, Google Chrome 157.0 (64-bit), Screen 1920x1080",
        "status": "Open",
        "evidence": "screenshots/bug-002-zipcode-validation.png"
    },
    {
        "id": "BUG-003",
        "title": "Search input fails to match valid products when search string contains leading or trailing whitespace",
        "module": "Product Search",
        "description": "The search function performs direct string matching without calling .trim() on the user input. Entering a valid search keyword with leading or trailing spaces (e.g. '  Camera  ') results in zero search results instead of matching existing products.",
        "preconditions": "Catalog page loaded with 12 products.",
        "steps": "1. Click in the search bar on the top navigation bar.\n2. Type '  Camera  ' (with leading and trailing spaces).\n3. Press Enter or click search button.",
        "expected": "The query should be trimmed automatically and display '4K Action Sports Camera'.",
        "actual": "0 matching products found; empty state screen displayed.",
        "severity": "Low",
        "priority": "Low",
        "environment": "Windows 11, Google Chrome 157.0 (64-bit), Screen 1920x1080",
        "status": "Open",
        "evidence": "screenshots/bug-003-search-whitespace.png"
    }
]

def style_excel_sheet(ws, title, is_bug_report=False):
    # Colors
    header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Dark Blue
    pass_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Light Green
    fail_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid") # Light Red
    high_fill = PatternFill(start_color="FFEDD5", end_color="FFEDD5", fill_type="solid") # Light Orange
    med_fill = PatternFill(start_color="FEF9C3", end_color="FEF9C3", fill_type="solid") # Light Yellow
    
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    data_font = Font(name="Calibri", size=10)
    bold_font = Font(name="Calibri", size=10, bold=True)
    
    thin_border = Border(
        left=Side(style="thin", color="CBD5E1"),
        right=Side(style="thin", color="CBD5E1"),
        top=Side(style="thin", color="CBD5E1"),
        bottom=Side(style="thin", color="CBD5E1")
    )
    
    # Header styling
    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    
    # Row styling
    for row in range(2, ws.max_row + 1):
        for col in range(1, ws.max_column + 1):
            cell = ws.cell(row=row, column=col)
            cell.font = data_font
            cell.border = thin_border
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            
            val = str(cell.value or "")
            if val == "Pass":
                cell.fill = pass_fill
                cell.font = Font(name="Calibri", size=10, bold=True, color="166534")
                cell.alignment = Alignment(horizontal="center", vertical="top")
            elif val == "Fail":
                cell.fill = fail_fill
                cell.font = Font(name="Calibri", size=10, bold=True, color="991B1B")
                cell.alignment = Alignment(horizontal="center", vertical="top")
            elif val in ["High", "Critical"]:
                cell.fill = high_fill
                cell.font = Font(name="Calibri", size=10, bold=True, color="C2410C")
                cell.alignment = Alignment(horizontal="center", vertical="top")
            elif val in ["Medium", "Open"]:
                cell.fill = med_fill
                cell.alignment = Alignment(horizontal="center", vertical="top")
            elif val in ["Low"]:
                cell.alignment = Alignment(horizontal="center", vertical="top")
            elif col == 1:
                cell.font = bold_font
                cell.alignment = Alignment(horizontal="center", vertical="top")

    # Set column widths
    ws.row_dimensions[1].height = 28
    for col in ws.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            val = str(cell.value or "")
            # check lines
            lines = val.split("\n")
            line_len = max([len(l) for l in lines]) if lines else 0
            if line_len > max_len:
                max_len = line_len
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 45)

def export_test_cases():
    headers = [
        "Test Case ID", "Module", "Test Scenario", "Preconditions",
        "Test Steps", "Test Data", "Expected Result", "Actual Result",
        "Status", "Remarks"
    ]
    
    # 1. Export CSV
    csv_path = "test-cases/test-cases.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for tc in TEST_CASES:
            writer.writerow([
                tc["id"], tc["module"], tc["scenario"], tc["preconditions"],
                tc["steps"], tc["data"], tc["expected"], tc["actual"],
                tc["status"], tc["remarks"]
            ])
    print(f"Exported: {csv_path}")

    # 2. Export Excel
    xlsx_path = "test-cases/test-cases.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Manual Test Cases"
    ws.append(headers)
    
    for tc in TEST_CASES:
        ws.append([
            tc["id"], tc["module"], tc["scenario"], tc["preconditions"],
            tc["steps"], tc["data"], tc["expected"], tc["actual"],
            tc["status"], tc["remarks"]
        ])
    
    style_excel_sheet(ws, "Manual Test Cases")
    wb.save(xlsx_path)
    print(f"Exported: {xlsx_path}")

    # 3. Export Execution Results (same data with execution tracking)
    exec_csv = "test-execution/execution-results.csv"
    with open(exec_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers + ["Executed By", "Execution Date"])
        for tc in TEST_CASES:
            writer.writerow([
                tc["id"], tc["module"], tc["scenario"], tc["preconditions"],
                tc["steps"], tc["data"], tc["expected"], tc["actual"],
                tc["status"], tc["remarks"], "QA Engineer", "2026-11-13"
            ])
    print(f"Exported: {exec_csv}")

    exec_xlsx = "test-execution/execution-results.xlsx"
    wb_exec = openpyxl.Workbook()
    ws_exec = wb_exec.active
    ws_exec.title = "Execution Results"
    ws_exec.append(headers + ["Executed By", "Execution Date"])
    for tc in TEST_CASES:
        ws_exec.append([
            tc["id"], tc["module"], tc["scenario"], tc["preconditions"],
            tc["steps"], tc["data"], tc["expected"], tc["actual"],
            tc["status"], tc["remarks"], "QA Engineer", "2026-11-13"
        ])
    style_excel_sheet(ws_exec, "Execution Results")
    wb_exec.save(exec_xlsx)
    print(f"Exported: {exec_xlsx}")

def export_bug_reports():
    headers = [
        "Bug ID", "Bug Title", "Module", "Description", "Preconditions",
        "Steps to Reproduce", "Expected Result", "Actual Result",
        "Severity", "Priority", "Environment", "Status", "Screenshot/Evidence"
    ]

    # 1. Export CSV
    csv_path = "bug-reports/bug-report.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for b in BUG_REPORTS:
            writer.writerow([
                b["id"], b["title"], b["module"], b["description"], b["preconditions"],
                b["steps"], b["expected"], b["actual"], b["severity"],
                b["priority"], b["environment"], b["status"], b["evidence"]
            ])
    print(f"Exported: {csv_path}")

    # 2. Export Excel
    xlsx_path = "bug-reports/bug-report.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Bug Reports"
    ws.append(headers)
    for b in BUG_REPORTS:
        ws.append([
            b["id"], b["title"], b["module"], b["description"], b["preconditions"],
            b["steps"], b["expected"], b["actual"], b["severity"],
            b["priority"], b["environment"], b["status"], b["evidence"]
        ])
    style_excel_sheet(ws, "Bug Reports", is_bug_report=True)
    wb.save(xlsx_path)
    print(f"Exported: {xlsx_path}")

if __name__ == "__main__":
    export_test_cases()
    export_bug_reports()
    print("All test artifacts generated successfully!")

