-- ==============================================================================
-- Sathik Groups - Supabase Schema
-- Run this script in the Supabase SQL Editor (https://app.supabase.com -> SQL Editor)
-- ==============================================================================

-- 1. Products Table
CREATE TABLE IF NOT EXISTS public.products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    sku TEXT,
    description TEXT,
    short_description TEXT,
    features JSONB DEFAULT '[]'::jsonb,
    images JSONB DEFAULT '[]'::jsonb,
    business_slug TEXT,
    category_slug TEXT,
    subcategory_slug TEXT,
    brand_slug TEXT,
    brand_name TEXT,
    available_brands JSONB DEFAULT '[]'::jsonb,
    available_brand_slugs JSONB DEFAULT '[]'::jsonb,
    hide_brand_badge BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_new BOOLEAN DEFAULT TRUE,
    specifications JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexing for fast search and filtering
CREATE INDEX IF NOT EXISTS idx_products_slug ON public.products(slug);
CREATE INDEX IF NOT EXISTS idx_products_business ON public.products(business_slug);
CREATE INDEX IF NOT EXISTS idx_products_category ON public.products(category_slug);
CREATE INDEX IF NOT EXISTS idx_products_subcategory ON public.products(subcategory_slug);
CREATE INDEX IF NOT EXISTS idx_products_brand ON public.products(brand_slug);
CREATE INDEX IF NOT EXISTS idx_products_active ON public.products(is_active);
CREATE INDEX IF NOT EXISTS idx_products_featured ON public.products(is_featured);

-- 2. Businesses Table
CREATE TABLE IF NOT EXISTS public.businesses (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    tagline TEXT,
    description TEXT,
    icon TEXT,
    accent_color TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Categories Table
CREATE TABLE IF NOT EXISTS public.categories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    business_slug TEXT,
    description TEXT,
    icon TEXT,
    image_url TEXT,
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Subcategories Table
CREATE TABLE IF NOT EXISTS public.subcategories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    category_slug TEXT,
    business_slug TEXT,
    description TEXT,
    sort_order INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Brands Table
CREATE TABLE IF NOT EXISTS public.brands (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    logo TEXT,
    description TEXT,
    website TEXT,
    businesses JSONB DEFAULT '[]'::jsonb,
    is_featured BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    country TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Users / Admin Table
CREATE TABLE IF NOT EXISTS public.users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'staff',
    permissions JSONB DEFAULT '[]'::jsonb,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Disable Row Level Security (RLS) or enable public read/write with anon key for this API
ALTER TABLE public.products ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.businesses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.categories ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.subcategories ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.brands ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

-- Allow anon and service_role full access to tables for the Flask backend
DO $$
BEGIN
    DROP POLICY IF EXISTS "Public access to products" ON public.products;
    CREATE POLICY "Public access to products" ON public.products FOR ALL USING (true) WITH CHECK (true);

    DROP POLICY IF EXISTS "Public access to businesses" ON public.businesses;
    CREATE POLICY "Public access to businesses" ON public.businesses FOR ALL USING (true) WITH CHECK (true);

    DROP POLICY IF EXISTS "Public access to categories" ON public.categories;
    CREATE POLICY "Public access to categories" ON public.categories FOR ALL USING (true) WITH CHECK (true);

    DROP POLICY IF EXISTS "Public access to subcategories" ON public.subcategories;
    CREATE POLICY "Public access to subcategories" ON public.subcategories FOR ALL USING (true) WITH CHECK (true);

    DROP POLICY IF EXISTS "Public access to brands" ON public.brands;
    CREATE POLICY "Public access to brands" ON public.brands FOR ALL USING (true) WITH CHECK (true);

    DROP POLICY IF EXISTS "Public access to users" ON public.users;
    CREATE POLICY "Public access to users" ON public.users FOR ALL USING (true) WITH CHECK (true);
END $$;
