import os
from datetime import datetime
from models.product import ProductModel
from models.category import CategoryModel
from models.brand import BrandModel
from utils.constants import BUSINESSES

BASE_URL = 'https://sathikgroups.com'

def get_sitemap_entries():
    """
    Compiles all canonical, real, publicly accessible pages that currently exist.
    Excludes admin, login, private, API, and redirect routes.
    """
    entries = []
    today = datetime.now().strftime('%Y-%m-%d')

    # 1. Main Static / Core Hub Pages
    entries.append({
        'loc': f"{BASE_URL}/",
        'lastmod': today,
        'changefreq': 'daily',
        'priority': '1.0'
    })
    entries.append({
        'loc': f"{BASE_URL}/products",
        'lastmod': today,
        'changefreq': 'daily',
        'priority': '0.9'
    })
    entries.append({
        'loc': f"{BASE_URL}/stores",
        'lastmod': today,
        'changefreq': 'weekly',
        'priority': '0.8'
    })
    entries.append({
        'loc': f"{BASE_URL}/brands",
        'lastmod': today,
        'changefreq': 'weekly',
        'priority': '0.8'
    })
    entries.append({
        'loc': f"{BASE_URL}/projects",
        'lastmod': today,
        'changefreq': 'monthly',
        'priority': '0.7'
    })

    # 2. Store Verticals (/stores/<business_slug>)
    for biz in BUSINESSES:
        slug = biz.get('slug')
        if slug:
            entries.append({
                'loc': f"{BASE_URL}/stores/{slug}",
                'lastmod': today,
                'changefreq': 'weekly',
                'priority': '0.8'
            })

    # 3. Store Categories (/stores/<business_slug>/<category_slug>)
    try:
        categories = CategoryModel.find_all()
        for cat in categories:
            biz_slug = cat.get('business_slug')
            cat_slug = cat.get('slug')
            if biz_slug and cat_slug:
                entries.append({
                    'loc': f"{BASE_URL}/stores/{biz_slug}/{cat_slug}",
                    'lastmod': today,
                    'changefreq': 'weekly',
                    'priority': '0.8'
                })
    except Exception as e:
        print(f"⚠️ Error compiling categories for sitemap: {e}")

    # 4. Brands (/brands/<slug>)
    try:
        brands = BrandModel.find_all()
        for brand in brands:
            slug = brand.get('slug')
            if slug:
                entries.append({
                    'loc': f"{BASE_URL}/brands/{slug}",
                    'lastmod': today,
                    'changefreq': 'weekly',
                    'priority': '0.7'
                })
    except Exception as e:
        print(f"⚠️ Error compiling brands for sitemap: {e}")

    # 5. Products (/products/<subcategory_slug>/<product_slug>)
    try:
        products, _ = ProductModel.find_all(limit=5000, active_only=True)
        for prod in products:
            sub_slug = prod.get('subcategory_slug')
            prod_slug = prod.get('slug')
            if sub_slug and prod_slug:
                # Use updated_at or created_at if available
                mod_date = today
                raw_date = prod.get('updated_at') or prod.get('created_at')
                if raw_date:
                    try:
                        if isinstance(raw_date, str) and len(raw_date) >= 10:
                            mod_date = raw_date[:10]
                    except Exception:
                        mod_date = today

                entries.append({
                    'loc': f"{BASE_URL}/products/{sub_slug}/{prod_slug}",
                    'lastmod': mod_date,
                    'changefreq': 'weekly',
                    'priority': '0.8'
                })
    except Exception as e:
        print(f"⚠️ Error compiling products for sitemap: {e}")

    # Deduplicate entries by loc while preserving order
    seen_locs = set()
    unique_entries = []
    for entry in entries:
        if entry['loc'] not in seen_locs:
            seen_locs.add(entry['loc'])
            unique_entries.append(entry)

    return unique_entries


def generate_sitemap_xml():
    """Generates standard XML sitemap compliant with sitemaps.org schema."""
    entries = get_sitemap_entries()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for e in entries:
        lines.append('  <url>')
        lines.append(f"    <loc>{e['loc']}</loc>")
        lines.append(f"    <lastmod>{e['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{e['changefreq']}</changefreq>")
        lines.append(f"    <priority>{e['priority']}</priority>")
        lines.append('  </url>')
    lines.append('</urlset>')
    return '\n'.join(lines) + '\n'


def build_static_sitemap_files(root_dir=None):
    """Writes sitemap.xml to both static/ and project root directory."""
    if not root_dir:
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    xml_content = generate_sitemap_xml()

    static_path = os.path.join(root_dir, 'static', 'sitemap.xml')
    with open(static_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)

    root_path = os.path.join(root_dir, 'sitemap.xml')
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)

    return static_path, root_path
