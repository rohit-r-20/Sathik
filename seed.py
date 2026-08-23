#!/usr/bin/env python3
"""
Sathik Groups — Supabase Database Seeder
Seeds Supabase PostgreSQL with business verticals, categories, subcategories, authorized brands, sample products, and super admin user.
Run: python seed.py
"""

from app import create_app
from database.supabase import get_supabase
from services.user_service import UserService
from utils.constants import BUSINESSES, BRANDS_LIST, MOCK_CATEGORIES, MOCK_SUBCATEGORIES, MOCK_PRODUCTS

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
            for cat in MOCK_CATEGORIES:
                client.table('categories').upsert(cat, on_conflict='slug').execute()
            print(f"  - {len(MOCK_CATEGORIES)} Categories seeded")

            # 3. Seed Subcategories
            for sub in MOCK_SUBCATEGORIES:
                client.table('subcategories').upsert(sub, on_conflict='slug').execute()
            print(f"  - {len(MOCK_SUBCATEGORIES)} Subcategories seeded")

            # 4. Seed Brands
            for br in BRANDS_LIST:
                client.table('brands').upsert(br, on_conflict='slug').execute()
            print(f"  - {len(BRANDS_LIST)} Authorized Brands seeded")

            # 5. Seed Initial Products
            # Clear existing products to prevent leftover mock records
            client.table('products').delete().eq('business_slug', 'plumbing').execute()
            client.table('products').delete().eq('business_slug', 'hardware').execute()
            client.table('products').delete().eq('business_slug', 'bath-kitchen').execute()
            for p in MOCK_PRODUCTS:
                prod = p.copy()
                if '_id' in prod:
                    del prod['_id']
                client.table('products').upsert(prod, on_conflict='slug').execute()
            print(f"  - {len(MOCK_PRODUCTS)} Initial Catalogue Products seeded")

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
