import streamlit as st

st.header("📚 Welcome to the Bookstore!")

# Initialize book data using session state
if "all_products" not in st.session_state:
    st.session_state.all_products = {
        1: {'title': 'Python Basics', 'stock': 20, 'price': 200},
        2: {'title': 'AI & ML', 'stock': 100, 'price': 30},
        3: {'title': 'Data Science', 'stock': 200, 'price': 5},
        4: {'title': 'Web Development', 'stock': 100, 'price': 10},
        5: {'title': 'Cyber Security', 'stock': 120, 'price': 50}
    }

# Sidebar menu
select = st.sidebar.selectbox("Select option:", ['Show All Books', 'Buy a Book', 'Add Book','Updated Book List', 'Exit'])

# Show all books
if select == "Show All Books":
    st.subheader("📖 Available Books")
    st.write("**SNO — Title — Stock — Price**")
    for i, item in st.session_state.all_products.items():
        st.write(f"{i} — {item['title']} — {item['stock']} — ₹{item['price']}")

# Buy a book
elif select == 'Buy a Book':
    st.subheader("🛒 Buy a Book")
    id = st.number_input("Enter Product ID to buy:", step=1, min_value=1)
    quantity = st.number_input("Enter quantity:", step=1, min_value=1)

    if id in st.session_state.all_products:
        item = st.session_state.all_products[id]
        st.write(f"Product: {item['title']}")
        st.write(f"Price: ₹{item['price']}")
        name = st.text_input("Enter Customer Name:")
        confirm = st.text_input(f"Do you want to buy {item['title']} for ₹{item['price']} each? (Y/N):").upper()
        if confirm == 'Y' and name:
            if st.button("Download Receipt"):
                st.text("\n------ Bill Generated ------")
                st.text("Bill No: 000000000")
                st.text("Date: 01-05-2025")
                st.text(f"Customer: {name}")
                st.text(f"Product: {item['title']}")
                st.text(f"Quantity: {quantity}")
                st.text(f"Amount: ₹{item['price'] * quantity}")
                st.subheader("✅ Thank you for your purchase!")
    else:
        st.error("Invalid Product ID")

# Add a book
elif select == 'Add Book':
    st.subheader("➕ Add a New Book")
    admin_name = st.text_input("Enter admin username:")
    admin_password = st.text_input("Enter admin password:", type="password")

    if admin_name == "admin" and admin_password == "1234":
        new_book = st.text_input("Enter new book title:")
        new_stock = st.text_input("Enter new book stock quantity:")
        new_price = st.text_input("Enter new book price:")

        if new_book and new_stock and new_price:
            new_id = max(st.session_state.all_products.keys()) + 1
            st.session_state.all_products[new_id] = {
                "title": new_book,
                "stock": new_stock,
                "price": new_price
            }
            st.success(f"✅ Book '{new_book}' added successfully with ID: {new_id}")
    else:
        if admin_name or admin_password:
            st.error("❌ Invalid admin credentials")

elif select == 'Updated Book List':           
        st.subheader("📚 Updated Book List")
        for i, book in st.session_state.all_products.items():
                st.write(f"{i} — {book['title']} — {book['stock']} — ₹{book['price']}")
# else:
#         if admin_name or admin_password:
#             st.error("❌ Invalid admin credentials")

# Exit
elif select == 'Exit':
    st.title("👋 Thank you for visiting the Python Book Store!")
