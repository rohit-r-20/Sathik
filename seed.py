#!/usr/bin/env python3
"""
Sathik Groups — Supabase Database Seeder
Seeds Supabase PostgreSQL with business verticals, categories, subcategories, authorized brands, sample products, and super admin user.
Run: python seed.py
"""

from app import create_app
from database.supabase import get_supabase
from services.user_service import UserService
from utils.constants import BUSINESSES, BRANDS_LIST

def seed_database():
    app = create_app()
    with app.app_context():
        client = get_supabase()
        if client is None:
            print("❌ Cannot seed: Supabase client is not connected or credentials missing in .env.")
            print("💡 Please configure SUPABASE_URL and SUPABASE_KEY in .env.")
            return

        print("🌱 Seeding Supabase PostgreSQL database...")

        try:
            # 1. Seed Businesses
            for b in BUSINESSES:
                client.table('businesses').upsert(b, on_conflict='slug').execute()
            print("  - 3 Business Verticals seeded")

            # 2. Seed Categories
            categories_data = [
                {'name': 'Pipes', 'slug': 'pipes', 'business_slug': 'plumbing', 'order': 1, 'is_active': True},
                {'name': 'Pipe Fittings', 'slug': 'pipe-fittings', 'business_slug': 'plumbing', 'order': 2, 'is_active': True},
                {'name': 'Valves', 'slug': 'valves', 'business_slug': 'plumbing', 'order': 3, 'is_active': True},
                {'name': 'Pumps', 'slug': 'pumps', 'business_slug': 'plumbing', 'order': 4, 'is_active': True},
                {'name': 'Sanitaryware', 'slug': 'sanitaryware', 'business_slug': 'bath-kitchen', 'order': 1, 'is_active': True},
                {'name': 'Faucets & Mixers', 'slug': 'faucets-mixers', 'business_slug': 'bath-kitchen', 'order': 2, 'is_active': True},
                {'name': 'Showers', 'slug': 'showers', 'business_slug': 'bath-kitchen', 'order': 3, 'is_active': True},
            ]
            for cat in categories_data:
                client.table('categories').upsert(cat, on_conflict='slug').execute()
            print("  - 7 Categories seeded")

            # 3. Seed Subcategories
            subcategories_data = [
                {'name': 'CPVC Pipes', 'slug': 'cpvc-pipes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'order': 1, 'is_active': True},
                {'name': 'UPVC Pipes', 'slug': 'upvc-pipes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'order': 2, 'is_active': True},
                {'name': 'SWR Pipes', 'slug': 'swr-pipes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'order': 3, 'is_active': True},
                {'name': 'CPVC Fittings', 'slug': 'cpvc-fittings', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'order': 1, 'is_active': True},
                {'name': 'Water Closets', 'slug': 'water-closets', 'category_slug': 'sanitaryware', 'business_slug': 'bath-kitchen', 'order': 1, 'is_active': True},
                {'name': 'Wash Basins', 'slug': 'wash-basins', 'category_slug': 'sanitaryware', 'business_slug': 'bath-kitchen', 'order': 2, 'is_active': True},
                {'name': 'Basin Mixers', 'slug': 'basin-mixers', 'category_slug': 'faucets-mixers', 'business_slug': 'bath-kitchen', 'order': 1, 'is_active': True},
            ]
            for sub in subcategories_data:
                client.table('subcategories').upsert(sub, on_conflict='slug').execute()
            print("  - 7 Subcategories seeded")

            # 4. Seed Brands
            for br in BRANDS_LIST:
                client.table('brands').upsert(br, on_conflict='slug').execute()
            print("  - 9 Authorized Brands seeded")

            # 5. Seed Initial Products
            products_data = [
                {
                    'name': 'Astral CPVC Pro Pipe SDR 11 (3/4 inch)',
                    'slug': 'astral-cpvc-pro-pipe-sdr-11-3-4-inch',
                    'sku': 'AST-CPVC-001',
                    'description': 'Astral CPVC Pro pipes are high-performance chlorinated polyvinyl chloride pipes designed for hot and cold water distribution. Tested to withstand high pressures up to 82°C.',
                    'short_description': 'High-performance CPVC plumbing pipe for hot and cold water distribution.',
                    'features': ['Suitable for hot and cold water (up to 82°C)', 'Lead-free & NSF certified', 'Corrosion & chemical resistant', 'Smooth inner surface for low friction'],
                    'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
                    'business_slug': 'plumbing',
                    'category_slug': 'pipes',
                    'subcategory_slug': 'cpvc-pipes',
                    'brand_slug': 'astral',
                    'brand_name': 'Astral',
                    'is_active': True,
                    'is_featured': True,
                    'is_new': True,
                    'price': None,
                    'stock': 100
                },
                {
                    'name': 'Jaquar Single Lever Basin Mixer (Kubix Prime)',
                    'slug': 'jaquar-single-lever-basin-mixer-kubix-prime',
                    'sku': 'JAG-KUB-01',
                    'description': 'Jaquar Kubix Prime single lever basin mixer with 450mm flexible hose. Crafted with high-purity brass for superior durability and finished in mirror-shine chrome.',
                    'short_description': 'Premium brass basin mixer with mirror-shine chrome finish and smooth ceramic cartridge.',
                    'features': ['High purity brass casting', 'Mirror-shine chrome plating', 'Advanced smooth ceramic cartridge', '10 years warranty'],
                    'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
                    'business_slug': 'bath-kitchen',
                    'category_slug': 'faucets-mixers',
                    'subcategory_slug': 'basin-mixers',
                    'brand_slug': 'jaquar',
                    'brand_name': 'Jaquar',
                    'is_active': True,
                    'is_featured': True,
                    'is_new': False,
                    'price': None,
                    'stock': 50
                },
                {
                    'name': 'Hindware Italian Collection Wall Hung Water Closet',
                    'slug': 'hindware-italian-collection-wall-hung-wc',
                    'sku': 'HIND-WC-99',
                    'description': 'Sleek Italian design rimless wall-hung water closet with soft-close seat cover and water-saving dual flush mechanism.',
                    'short_description': 'Rimless wall-hung ceramic closet with dual flush and soft-close seat.',
                    'features': ['Rimless hygienic flushing technology', 'Soft-close durable seat cover', 'Germ-block nano glaze coating'],
                    'images': [{'url': '/static/images/placeholder.jpg', 'is_primary': True}],
                    'business_slug': 'bath-kitchen',
                    'category_slug': 'sanitaryware',
                    'subcategory_slug': 'water-closets',
                    'brand_slug': 'hindware',
                    'brand_name': 'Hindware',
                    'is_active': True,
                    'is_featured': True,
                    'is_new': True,
                    'price': None,
                    'stock': 30
                }
            ]
            for p in products_data:
                client.table('products').upsert(p, on_conflict='slug').execute()
            print("  - 3 Initial Catalogue Products seeded")

            # 6. Seed Super Admin User
            admin_email = 'admin@sathikgroups.com'
            if not UserService.find_by_email(admin_email):
                UserService.create(
                    name='Super Admin',
                    email=admin_email,
                    password='ChangeMe@2024!',
                    role='super_admin',
                    permissions=['products:write', 'categories:write', 'brands:write', 'enquiries:read', 'settings:read']
                )
                print("  - Super Admin user created (admin@sathikgroups.com / ChangeMe@2024!)")

            print("\n✅ Supabase database seed completed successfully!")

        except Exception as e:
            print(f"⚠️ Seeding notice: {e}")

if __name__ == '__main__':
    seed_database()
