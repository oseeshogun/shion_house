# Shop CD Django Project

## Overview
This is a Django-based e-commerce project with multiple apps including home, shop, about, and contact functionalities.

## Project Structure
- `home/`: Main application handling the homepage
- `shop/`: E-commerce functionality
- `about/`: About page and related information
- `contact/`: Contact form and communication features
- `static/`: Static files (CSS, JavaScript, images)

## Technical Stack
- Django 5.1.5
- SQLite3 Database
- django-extensions (for additional development tools)

## Installation
1. Clone the repository
2. Install dependencies using Pipenv:
```bash
pipenv install
```
3. Activate the virtual environment:
```bash
pipenv shell
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```

## Database Visualization
The project uses django-extensions to generate database schema visualizations. To generate a database diagram:
```bash
./manage.py graph_models -a > db_graph.dot
```
This command creates a DOT file (`db_graph.dot`) containing the database schema visualization. To convert this to a viewable format, you'll need Graphviz installed and can use:
```bash
dot -Tpng db_graph.dot > db_schema.png
```

## Development
- Debug mode is currently enabled
- The project uses Django's built-in authentication system
- Static files are configured and served through Django's staticfiles app

## Security Notes
- Debug mode should be disabled in production
- Secret key should be changed in production
- Configure proper allowed hosts before deployment

## Apps Description
1. **Home App**: Main landing page and core functionality
2. **Shop App**: E-commerce features and product management
3. **About App**: Company/Project information pages
4. **Contact App**: User communication and feedback system

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Add your license information here]