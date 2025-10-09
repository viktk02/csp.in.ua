# Practice Django Project

This is a Django-based web application for managing and displaying projects, posts, and related content for the Charitable Foundation "Center for Social Programs".

## Features
- Project listing and detail pages
- Posts with images and previews
- Smart pagination for project feeds
- Image lightbox/zoom functionality
- Scroll position saving and restoration for better UX
- Media and static file management
- Partner logos and information

## Project Structure
- `main/` — Main app for core site features
- `posts/` — Blog/news posts
- `projects/` — Projects management
- `practise/` — Django project settings
- `static/` — Static files (CSS, JS, images)
- `media/` — Uploaded media files
- `templates/` — HTML templates

## Example Requests (URLs)

### Projects
- `/projects/` — List all projects
- `/projects/<id>/` — Project detail page
- `/projects/?page=<n>` — Paginated project list

### Posts
- `/posts/` — List all posts
- `/posts/<id>/` — Post detail page

### Partners
- `/partners/` — Partner logos and info

### Static/Media
- `/static/...` — Static assets (CSS, JS, images)
- `/media/...` — Uploaded images and files

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start development server:
   ```bash
   python manage.py runserver
   ```

## Notable JavaScript Features
- `static/js/scroll-position.js`: Saves/restores scroll position when navigating between pages.
- `static/js/lightbox.js`: Zooms images in posts and restores scroll position after closing modal.

## Contact
For questions or contributions, contact the repository owner or open an issue.
