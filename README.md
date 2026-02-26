# ShopEase Cloud 2.0 - Prototype

> ⚠️ **TODO: Change the `APP_TITLE` variable in `app.py` from `"ChangeMe"` to your own project name!**

A simple Python/Flask web application prototype for the ShopEase Cloud 2.0 assignment.

## Features

- **Home page** – product listings
- **Login/Logout** – session-based authentication
- **Search** – filter products by name
- **Product detail** – with simulated AI recommendations
- **Shopping cart** – add items and simulate checkout/payment
- **Admin dashboard** – analytics stats (admin login only)

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

**Demo credentials:**
- `admin` / `password123` (has dashboard access)
- `user1` / `pass1`

## Deploying to Azure Web App

1. Push this repo to GitHub.
2. In Azure Portal, create a **Web App** (Python 3.11, Linux).
3. Under **Deployment Center**, connect your GitHub repo.
4. Set the **Startup Command** to:
   ```
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```
5. Azure will auto-deploy on every push to your main branch.

## Project Structure

```
app.py              # Main Flask application
requirements.txt    # Python dependencies
startup.txt         # Azure startup command reference
templates/
    base.html       # Shared layout
    index.html      # Home / product listing
    login.html      # Login form
    search.html     # Search results
    product.html    # Product detail + AI recommendations
    cart.html       # Shopping cart + checkout
    dashboard.html  # Admin analytics dashboard
```
